# REPORT_FEATURE_PLAN.md

## Summary

Add the GitHub Issues reporting workflow to `hydrants_varna_merged.html` after Petar approval. This is the selected implementation target because it currently contains **6,070 hydrants**, is **1,203,986 bytes**, and remains under the **2 MB hard cap**.

Do not edit `hydrants_varna (7).html` except as an older reference. Replace the existing SMS/Web Share report modal with a structured volunteer flow that creates GitHub Issues containing YAML frontmatter plus Bulgarian human-readable Markdown.

Planned artifact location for this handoff:
`audit/run_<yyyyMMdd_HHmmss>_report_feature_plan/REPORT_FEATURE_PLAN.md`

## Key Interfaces

Add report constants near the existing script constants:

```js
const GITHUB_REPO_OWNER = "<TODO_PETAR_GITHUB_USERNAME>";
const GITHUB_REPO_NAME = "Varna_hydrants";
const GITHUB_PAT = "<TODO_FINE_GRAINED_PAT>";
const GITHUB_API_VERSION = "2026-03-10";
const APP_VERSION = "merged-2026-05-05";
```

Add localStorage keys:

```js
hydrants_reporter_name
hydrants_recent_reports
hydrants_pending_reports
```

Canonical report object:

```js
{
  report_id,
  report_type,
  timestamp,
  reporter,
  hydrant_ref,
  expected_coord,
  reported_coord,
  location_method,
  app_version,
  free_text,
  terrain_description,
  description,
  damage_description,
  hydrant_type_at_location,
  hydrant_type,
  operational
}
```

Submit issues with:

```js
POST https://api.github.com/repos/{owner}/{repo}/issues
Authorization: Bearer <GITHUB_PAT>
Accept: application/vnd.github+json
X-GitHub-Api-Version: 2026-03-10
```

Request body:

```js
{
  title,
  body,
  labels: ["report", "<type-label>", "pending-review"]
}
```

## Implementation Changes

Replace the static report modal markup and old `reportProblem()`/`navigator.share()` logic around lines 1127-1168 and 1653-1749 with a dynamic report controller.

Keep these functions as the implementation boundary:

```js
showReportModal(hydrant, reportType)
enterLocationPlacementMode(callback)
buildReportYAML(report)
buildIssueTitle(report)
submitReport(report)
queueReport(report)
retryQueuedReports()
getReporterName()
setReporterName(name)
```

Add one top-level right-side control beside the existing manual-position button:
`+` button, `id="addHydrantBtn"`, `title`/`aria-label="Добави хидрант"`, opens `new_hydrant` placement mode.

Update hydrant popups so `buildPopup()` includes a `Докладвай` button. Use popup event delegation, not inline handlers, to open the report type picker for the tapped hydrant.

Existing hydrant report type picker options:

- `exists_confirmed`: `Хидрантът е там`
- `missing`: `Хидрант липсва`
- `wrong_location`: `Грешна локация`
- `damaged`: `Повреден`

New hydrant flow starts only from `Добави хидрант`.

Location placement for `new_hydrant` and `wrong_location`:

- Show banner: `Задръж пръст върху картата където е хидрантът`
- Use Leaflet `contextmenu` plus custom `touchstart` timer of at least 500ms.
- Cancel long-press if touch moves more than 12px or ends early.
- Create a draggable `L.divIcon` marker with pulsing red styling.
- Bottom placement actions: `Изчисти`, `Продължи`, `Отказ`.
- `Продължи` disabled until marker exists.
- Store coordinates as `[lon, lat]`, fixed to 6 decimals.
- `Промени локация` returns to placement mode and preserves draft form values.

Reporter identity:

- Required field: `Твоето име или handle`, min 2, max 50 chars.
- Prefill from `hydrants_reporter_name`.
- Save valid name on submit.
- Header shows `Докладва: <name>` when saved.
- `Промени име` opens prompt and updates field/localStorage.

Report form fields:

- `exists_confirmed`: reporter, optional free text.
- `missing`: reporter, `hydrant_type_at_location` radio default `не знам`, optional terrain description.
- `new_hydrant`: reporter, `hydrant_type` radio default `не знам`, optional description.
- `wrong_location`: reporter, required description, required placed coordinate.
- `damaged`: reporter, required damage description, `operational` radio default `не съм проверявал, само видимо`.

YAML rules:

- Begin and end frontmatter with `---`.
- Use `null` for absent values.
- Use JSON-quoted strings for YAML safety.
- Use `[lon, lat]` numeric arrays for coordinates.
- Timestamp must include local offset, e.g. `2026-05-05T18:23:11+03:00`.

Submission behavior:

- `201`: show `Докладът е изпратен. Референтен номер: #<issue_number>. Благодаря!`
- Store last 50 successful reports in `hydrants_recent_reports`.
- Network error or offline: ask `Няма интернет. Запази локално и опитай пак?`; if yes, queue.
- `403` rate/secondary limit: show `Твърде много доклади. Опитай след 1 час.` and queue.
- `401`: show `Системна грешка. Свържи се с администратор.` and log details.
- `404`, `410`, unexpected `400/422/503`: show system error, log details; queue only for transient/network-like failures.
- If `422` is caused by missing labels, retry once without labels, log warning, and require label setup before acceptance.

Spam protection:

- Hidden honeypot input named `website`; if filled, silently discard without API call.
- In-memory submit rate limit: max 1 manual submit per 30 seconds.
- In-memory dedup for 5 minutes using normalized hash of `(report_type, hydrant_ref, reporter_name, reported_coord)`.
- On duplicate, show `Вече изпратен същия доклад` and allow explicit override.

## Manual Steps For Petar

1. Create a fine-grained PAT named `Varna_hydrants_reports`.
2. Repository access: only `Varna_hydrants`.
3. Permissions: Issues read/write, Metadata read.
4. Expiration: 1 year.
5. Paste owner, repo, and token into the constants.
6. Create labels before acceptance testing: `report`, `exists-confirmed`, `missing`, `new-hydrant`, `wrong-location`, `damaged`, `pending-review`.
7. Submit one real test report, verify issue title/body/labels, then close or delete the test issue if desired.

Security note: embedding a PAT in static HTML exposes it to every user and conflicts with GitHub credential-security guidance. This is an accepted project risk for this plan; keep permissions minimal and be ready to rotate the token if GitHub secret scanning or abuse invalidates it.

## Test Plan

Before final deploy, Claude Code verifies:

- App loads `hydrants_varna_merged.html` with 6,070 hydrants.
- Final file size remains under 2,000,000 bytes.
- Existing GPS, compass, manual position, follow mode, modes, clustering, and bottom sheet still work.
- Popup, list, and card report entry points open the new flow.
- `Добави хидрант` opens placement mode.
- Long-press places marker; marker is draggable; `Продължи` enables only after placement.
- `Промени локация` returns to placement with draft preserved.
- Reporter name persists across reloads.
- Each of the 5 report types validates required fields correctly.
- Generated issue body has parseable YAML frontmatter and Bulgarian Markdown body.
- Real GitHub issue is created with correct title, labels, and issue number confirmation.
- Offline/network failure queues report locally.
- Queued reports retry on next load or `online` event.
- Honeypot, 30-second rate limit, and duplicate warning all work.
- No new runtime or build-time dependencies are introduced.

## References

GitHub REST create issue docs: https://docs.github.com/en/rest/issues/issues#create-an-issue  
GitHub REST CORS docs: https://docs.github.com/en/rest/using-the-rest-api/using-cors-and-jsonp-to-make-cross-origin-requests  
GitHub rate limit docs: https://docs.github.com/en/rest/rate-limit/rate-limit  
GitHub credential security docs: https://docs.github.com/en/rest/authentication/keeping-your-api-credentials-secure

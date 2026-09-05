# МЯРКА · Условията на Уикимапия за данните (прочетено 06.09.2026, ~03:50, в браузъра от архитекта)

Цел: входът за `_meta.source_terms["wikimapia"]` по К17 (Кими) — цитат, URL, дата. Нищо тук не е присъда; присъдата е на Кими след прочит на този файл.

## 1 · Terms of Service — `http://wikimapia.org/terms_reference.html`
(Достига се от долния колонтитул „Wikimapia CC-BY-SA“ → `router.route('/terms_reference.html')`; `/terms_reference/` без `.html` връща 404.)

- **§1.F (лицензът):** „All User Submissions of all users and all Wikimapia Data are freely available for commercial and non-commercial use under Creative Commons license Attribution-ShareAlike through WikiMapia website, WikiMapia API and other current or future WikiMapia services.“
- **§1.G (условията при публична употреба):** „Public use of Wikimapia Data and it's derivatives requires special conditions: a. Link to Wikimapia data original url, if viewed from any web browser; b. Mention of "Wikimapia.org" (with a link to http://wikimapia.org, if viewed from any web browser)“.
- **§1.C.g и §1.C.j (натоварването):** „you will not impose an unreasonable load on WikiMapia's infrastructure or interfere with the proper working of WikiMapia“; „you will not use the Wikimapia services … in any other manner which could damage, impair, or overburden the Service“.
- **§1.B (правото на всеки потребител):** „You also hereby grant each user of the WikiMapia a non-exclusive license to access your User Submissions through the Service, and to use, reproduce, distribute, prepare derivative works of, display and perform such User Submissions as permitted through the functionality of Wikimapia and under these Terms of Service.“
- **§3 (юрисдикцията):** „The SERVICE is controlled and offered by WikiMapia from its facilities in the United States of America.“
- **§4:** условията се менят без известие; всяко приложение/услуга може да има допълнителни условия.
- Версията на лиценза (3.0 / 4.0) в ToS **не е посочена** — само „Attribution-ShareAlike“. Сайтът/API-документацията сочат CC BY-SA; версията остава отворена (в проекта дотук се приемаше 3.0 Unported — да се сверява при присъдата).

## 2 · API документацията — `https://wikimapia.org/api/`
- „Wikimapia Api is a system that allows you to receive data from our maps. You can easily integrate Wikimapia Geo Data into your external application or web site. And it's all free.“
- „We open Wikimapia data free for non-commercial use (as you mention the original data source, according to Wikimapia TOS).“ — **разминаване с ToS §1.F** („commercial and non-commercial“); нашата употреба е нетърговска и е покрита от двата текста.
- Ключове: „My keys / Create key“ — изисква акаунт в Уикимапия (създаването на акаунт е действие на Петър, не на агент). Ключът `example` е демонстрационният от примерите на страницата.
- Документирани функции и параметри: `place.getbyid` (data_blocks main, geometry, edit, location, …), `place.getbyarea` (bbox или lon_min…; `category`; count 5–100; page), `place.getnearest` (lat, lon; data_blocks **само** location, geometry; count 5–100; category), `place.search` (q; count; category), `category.getall`.

## 3 · About — `https://wikimapia.org/about/`
- „Our goal is to describe the whole world … and provide free access to our data for public domain.“ · „Wikimapia data is wholly made by Internet volunteers“.

## 4 · Измерено поведение с ключ `example` (05–06.09.2026)
| функция | резултат |
|---|---|
| `place.getbyid` (id 1851926, data_blocks main,geometry,location) | работи; полигон + категории (празни за Кайсиева) |
| `place.getnearest` (count 100, data_blocks geometry,location) | работи; `data_blocks=main` → грешка 1901; лимит ≈ 1 заявка/28 s („You need to wait for N seconds“) |
| `place.getnearest` + `category=4621` или `13328` | found 0 |
| `place.getbyarea` (lon_min…; или `coordsby=bbox&bbox=`; с/без category) | found 0 при всеки опит |
| `place.search` (q) | празен списък |
| `category.getall&name=квартал` | работи: 4621 „квартал“ (148 875 места), 13328 „квартал/микрорайон“ (64 851) |

Извод за метода: единственият списъчен път с демо ключа е `getnearest`; обходът е от точки (163 семена + мрежа 500 m), при 100 резултата на заявка; проверката за пълнота по код (Astra S14) е задължителна след обхода.

## 5 · Какво остава за Кими (присъдата)
- К15(а): операторът е в САЩ по собствените си условия → защита sui generis в ЕС по чл. 11 на Дир. 96/9 вероятно липсва — да се потвърди/обори.
- К17: обходът (≈670 заявки за ≈5 часа при 1/28 s, наложено от самия API) — „unreasonable load“ ли е по §1.C.g? Реален ключ (акаунт на Петър) сменя ли положението?
- К18: §1.G задава по-конкретни условия от CC §4(c): линк към оригиналния обект + „Wikimapia.org“ с линк, „if viewed from any web browser“ — важи ли за приложение, което публикува само име на квартал (не показва данните на Уикимапия)?

# Astra (GPT-6, ultra, 06.09.2026 ~01:35) · Владиславово/Кайсиева официални векторни планове, DWG четимост и CRS, портални полигони — T1–T4

Брифът: `granitsi_forumi_brief_astra.md`. Дословен отговор (финалният блок).

**Кайсиева градина has two confirmed vector PDFs and a downloadable DWG.** These are the strongest obtainable sources; an existing, correctly identified closed quarter polygon has **not yet been demonstrated**.

Checked 5 September 2026, read-only. Sizes below are measured response bytes; PDF structure was inspected in memory. Coverage here is whole-microdistrict material and useful supplementary maps, excluding individual-parcel amendments.

**Official files found**

The [AGUP publication page](https://agup.varna.bg/index.php/ustroistveni-planove/vlezli-v-sila-pup-011024) leads to the [Владиславово Drive directory](https://drive.google.com/drive/folders/1n5IKBzvTbbtNaWp4sVshc5HV3xj6rHmX). Its listing contains **I, II and IV**, with no III or V folder. AGUP describes downloads as informational; publication does not make them certified extracts.

| Coverage / exact download | Bytes | Verified content and georeferencing status |
|---|---:|---|
| [Кайсиева, 2016 PDF](https://vladislavovo.bg/wp-content/uploads/2016/04/KAISIEVA_GRADINA2.pdf) | 7,392,111 | One page; **72,736 vector paths, zero images**. Outlined labels; no extractable text or embedded georeferencing dictionary. |
| [Кайсиева, 2018 PDF](https://vladislavovo.bg/wp-content/uploads/2018/01/ПУП-ПРЗ-II-микрорайон-ж.к.-Кайсиева-градина.pdf) | 3,635,932 | One page; **33,953 vector paths, zero images**. Same georeferencing limitations. |
| [I микрорайон DWG](https://drive.google.com/uc?export=download&id=1B3bBa7TO3lS6NaiW-qX3E2iYQ7U7WFo5) | 1,216,629 | Valid `AC1014`/R14 signature; entities, CRS and boundary closure unverified. |
| [II микрорайон DWG](https://drive.google.com/uc?export=download&id=1lGmgz9CcAPU1CzLQ3r54A48XaJkFrxXZ) | 553,682 | R14; same limits. |
| [IV микрорайон DWG](https://drive.google.com/uc?export=download&id=1eXMLtIxo0huh34D0kY5febhf2NFZfiO5) | 1,690,569 | R14; same limits. |
| [Additional `zona_OD.dwg`, I folder](https://drive.google.com/uc?export=download&id=1mWE6MdzRVbS5n-mw29rt54nMgyEvUqLC) | 670,311 | Newly located; R14. Its actual geographic extent remains unread. |
| [III restructuring plan image](https://vladislavovo.bg/wp-content/uploads/2017/05/PUPIIMR.png) | 488,078 | **Raster PNG**, visually confirmed as III despite its filename. No vector geometry. |

Both Кайсиева PDF titles reference a source drawing named `…20_юли2010…`; their upload/export dates should **not** be treated as plan-approval dates. Neither provides machine-readable cadastral identifiers. A printed coordinate grid or usable `10135.*` anchors remains unverified; OCR did not complete.

Five additional **green-register maps** are confirmed CAD-derived vector PDFs, each also containing one raster image:

| Exact PDF | Bytes |
|---|---:|
| [I north](https://agup.varna.bg/zr/vlvarnenchik_d5/Vlad-I_Model.pdf) | 1,225,582 |
| [I south](https://agup.varna.bg/zr/vlvarnenchik_d5/Vlad-jug-Model.pdf) | 1,574,465 |
| [II](https://agup.varna.bg/zr/vlvarnenchik_d5/Vlad-II-Model.pdf) | 1,180,500 |
| [III](https://agup.varna.bg/zr/vlvarnenchik_d5/Vlad-III_Model.pdf) | 1,603,701 |
| [IV](https://agup.varna.bg/zr/vlvarnenchik_d5/Vlad-IV-Model.pdf) | 1,914,254 |

These contain 42,357–81,217 vector paths each, but their searchable text yielded no full cadastral identifiers or coordinate-grid values. They can support alignment through identifiable features; a closed microdistrict perimeter still needs inspection. Their [official classification is street greenery](https://agup.varna.bg/index.php/2014-12-22-07-43-48/ulichno-ozelenyavane), so they do not establish ПУП approval.

**V remains unconfirmed.** The five sheets represent I north, I south, II, III and IV. Searches found no published whole-V plan. For III, the [January 2026 ЕСУТ protocol](https://agup.varna.bg/attachments/article/1041/zzprot_902_21_01_26.pdf) confirms planning history, but supplies no whole-area vector drawing.

**What the municipality actually says about the boundary**

The [ИПГВР amendment, PDF page 14](https://www.varna.bg/upload/3961/ipvgr_izmenenie_dopulnenie.pdf) locates the Кайсиева/II improvement project between:

- north: бул. „Трети март“;
- east: ПЗ „Планова“;
- south: ул. „Д-р Петър Дертлиев“;
- west: ул. „Димитър Пешев“.

This is a **project-location description**, useful for checking the drawing; it does not independently establish a legally defined quarter polygon. The [cleaning order](https://varna.bg/upload/6054/zapoved_kmet_3660.pdf) combines **II plus industrial Планова**, producing a broader perimeter that must not be assigned to Кайсиева alone.

For III, the [district’s planning announcement](https://vladislavovo.bg/пуп-прз-iii-микрорайон/) explicitly identifies the project territory between „Св. Елена“, „Янко Мустаков“ and „Константин и Фружин“.

**Free DWG reading: recommendation**

Start with **QGIS’s DWG/DXF import** for the four checked files. Its bundled libdxfrw explicitly supports their R14 signature. This establishes version compatibility; successful entity decoding and complete layers still require a conversion check. [QGIS instructions](https://docs.qgis.org/3.40/en/docs/user_manual/managing_data_source/opening_data.html#importing-a-dxf-or-dwg-file), [reader implementation](https://raw.githubusercontent.com/qgis/QGIS/master/external/libdxfrw/libdwgr.cpp).

Available alternatives:

- [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter): free, proprietary Windows application; DWG→DXF2013 fallback.
- [LibreDWG](https://www.gnu.org/software/libredwg/): GPLv3+, linked Windows builds; `dwg2dxf` and `dwgread`; some advanced entities have limitations.
- [ezdxf’s ODA integration](https://ezdxf.readthedocs.io/en/stable/addons/odafc.html): invokes an installed ODA converter; ezdxf itself reads DXF.

No decoder was available on PATH, and nothing was installed. **The 15-file collection has not been decoded.**

For CRS, inspect declared metadata, GEODATA and title blocks first. **EPSG:7801 means BGS2005/CCS2005**; BGS2005 also has UTM variants. An independently checked illustrative position at 27.83°E, 43.25°N becomes approximately **E 689,191 / N 4,793,098 m** in 7801. Older КС1970 around Varna uses northeastern **K-7**, with eastings potentially around 9.4–9.7 million. Magnitudes only narrow candidates: verify units, axis order, offsets and distributed cadastral controls. [PROJ definitions](https://raw.githubusercontent.com/OSGeo/PROJ/master/data/sql/projected_crs.sql), [AGKK transformation instruction](https://www.cadastre.bg/sites/default/files/documents/regulation/instrukcii/instr_bgs2005_08_2012_dv63.pdf).

**Other machine-readable polygon sources**

| Provider / URL or API | Coverage and licence finding |
|---|---|
| [Geofabrik Bulgaria](https://download.geofabrik.de/europe/bulgaria.html) | OSM PBF, **ODbL**. Supplies quarter polygons only where contributors mapped them. Actual target coverage unverified: Overpass checks failed. |
| [Geoapify Boundaries API](https://apidocs.geoapify.com/docs/boundaries/) | GeoJSON boundary service, key required; underlying OSM data is ODbL, service terms apply. No target-quarter response verified. `geometry_1000` is unsuitable for street-precise comparison. |
| [Mapbox Boundaries](https://docs.mapbox.com/data/boundaries/reference/mapbox-boundaries-v4/) | District/quarter and neighbourhood layers exist; **proprietary licensed access**. Varna coverage at those levels unverified. |
| [Esri Bulgarian coverage](https://www.esri.com/content/dam/esri_content_doc/dbl/int/europe/2025/bgr-mbr-2025-release-notes.pdf) | Proprietary MBR dataset lists administrative/postal levels, **no quarters**. |
| [2GIS territorial data](https://docs.2gis.com/en/pro/data/built-in/territorial) | Proprietary; advertised country coverage **excludes Bulgaria**. |
| [Yandex Geocoder](https://yandex.ru/maps-api/docs/geocoder-api/response.html) | Proprietary; documented point and bounding envelope, no demonstrated Varna quarter-ring endpoint. |
| [HERE Geocode v7](https://docs.here.com/geocoding-and-search/docs/geocode) | Proprietary; position and map-view box, no demonstrated target boundary rings. |

Wikimapia, forums and property-portal network inspection remain with Kimi, as requested.

**Ranking for this week:** Кайсиева—**II DWG first**, then the two vector ПУП PDFs, then the green-register II map, checked against the municipal street description. I and IV—DWGs first, green-register maps second. III—green-register vector map first; the published restructuring image supplies visual corroboration only. V—no verified source.

The unresolved step is extracting an **existing, correctly identified perimeter**, establishing its CRS and confirming that it matches the commonly understood quarter. None of the researched commercial services supplies a verified shortcut to that result.

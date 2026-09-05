# Astra (GPT-6, ultra, 05.09.2026 ~23:50) · Общинският слой „Квартали“ (огледала) + районните администрации, ИПГВР, ОУП, ПУП DWG — R0–R6

Брифът: `granitsi_rayoni_brief_astra.md` + R0. Дословен отговор (финалният блок).

**Открих публичен кеш на метаданните за „Квартали“, работещи DWG изтегляния и векторни районни PDF карти. Пълен комплект жилищни квартални полигони, готов за импорт, не е потвърден.**

**R0. Официалният ArcGIS слой**

- **Кешът съществува:** [Hub dataset JSON](https://opendata.arcgis.com/api/v3/datasets/ce83fb2fc9d7416c9778d75f9a98e5dc_0). Проверени: `recordCount:52`, полигонна геометрия, EPSG:3857, статистика на `Name_bg`, включително **„Цветен квартал“**. „Виница“ и „Изгрев“ не се срещат като отделни имена. Полето `boundary` съдържа само правоъгълния обхват на слоя.
- **Корекция на датата:** `created:1751705878000` означава **05.07.2025**, не 2026. Кешът пази `lastSuccessAt` **05.07.2025, 10:27:33 UTC**. Това е успешно индексиране, не дата на изтичане на абонамента.
- **Геометрията остава недостъпна:** проверените [GeoJSON](https://varnagisportal-varnamun.hub.arcgis.com/api/download/v1/items/ce83fb2fc9d7416c9778d75f9a98e5dc/geojson?layers=0) и [Shapefile](https://varnagisportal-varnamun.hub.arcgis.com/api/download/v1/items/ce83fb2fc9d7416c9778d75f9a98e5dc/shapefile?layers=0) връщат HTTP 403, „Subscription is disabled“.
- Открити кандидати за вграждане: [„Карта – Зелена Система“](https://www.arcgis.com/home/item.html?id=8077f9ffcd834c8f9353d5c3a1365c39) и [Experience „Зелена система“](https://experience.arcgis.com/experience/947dfe39e13448ba878d0c73ddcc323a). Техният JSON също е блокиран; съдържанието не е потвърдено.
- Не намерих работещо огледало сред проверените чужди Web Maps, Living Atlas, GitHub и порталите за отворени данни. [Wayback CDX за Hub](https://web.archive.org/cdx/search/cdx?url=varnagisportal-varnamun.hub.arcgis.com/*&output=json&filter=statuscode:200&collapse=timestamp:6&fl=timestamp,original&limit=20) върна празен списък.
- **Оператор:** публичният [профил gisprojects4](https://www.arcgis.com/sharing/rest/community/users/gisprojects4?f=json) заявява единствено „ГИС Проекти“. [Организацията](https://www.arcgis.com/sharing/rest/portals/iUyRq1SRpOklUPak?f=json) е „Община Варна“. Не установих доказана фирма или конкретен отдел зад профила/портала.
- **Абонамент:** точната дата на прекъсване не се установи. **Лиценз:** `license:none`, празно `licenseInfo`; няма заявено разрешение за повторна употреба.

**R1. Петте районни администрации**

| Район | Конкретни находки · формат · обхват · проверка |
|---|---|
| **Одесос** | [ods-zrp.pdf](https://odesos.bg/odessos/ods-ut-maps/maps/ods-zrp.pdf), районна карта с отделна легенда за **граници/номера на микрорайони**. Проверена структура: 219 589 векторни графични обекта, без изображения. Не открих геореференция в проверените PDF структури; съответствието с жилищните квартали остава непроверено. |
| **Приморски** | Реалният [официален сайт е primorski.bg](https://primorski.bg/wps/portal/municipality-primorski/home). Проверени [местоположение](https://primorski.bg/wps/portal/municipality-primorski/municipality/municipality-characteristics/geographical.characteristics) и [планове](https://primorski.bg/wps/portal/municipality-primorski/administration/strategic-documents/plans). Не намерих конкретен квартален геофайл; динамичното съдържание ограничава отрицателния резултат. |
| **Младост** | [Описание на района](https://www.varna-mladost.com/new/ml-m-begin.php): изброява квартали/микрорайони, но не дава геометрия. [ОУП публикацията](https://www.varna-mladost.com/articles.php?lng=bg&pg=304&prt=2) не предостави проверим квартален файл; директният достъп беше нестабилен. |
| **Аспарухово** | Пет конкретни PDF: [Боровец–юг](https://asparuhovo.bg/documents/adm_maps/borovec-south.pdf), [Прибой 1](https://asparuhovo.bg/documents/adm_maps/priboj.pdf), [Прибой 2](https://www.asparuhovo.bg/documents/adm_maps/priboj2.pdf), [Зеленика](https://www.asparuhovo.bg/documents/adm_maps/zelenika.pdf), [Ракитника](https://asparuhovo.bg/documents/adm_maps/rakitnika.pdf). Боровец–юг, Прибой 2 и Зеленика са структурно проверени и съдържат векторна графика; геореференция не открих. Другите два останаха непрочетени. Покриват селищни образувания. [Регистърът на ПУП](https://www.asparuhovo.bg/documents/direkcii/ut/registri/ИЗДАДЕНИТЕ%20ЗАПОВЕДИ%20ЗА%20ОДОБРЯВАНЕ%20НА%20ПУП/Регистри%20одобрявам%20ПУП.pdf) е таблица на заповеди/имоти, потвърдена само чрез индекса. |
| **Владислав Варненчик** | [ПУП–ПРЗ II микрорайон, Кайсиева градина.pdf](https://vladislavovo.bg/wp-content/uploads/2018/01/ПУП-ПРЗ-II-микрорайон-ж.к.-Кайсиева-градина.pdf): проверени 33 953 векторни графични обекта, без изображения; геореференция не открих. [III микрорайон](https://vladislavovo.bg/пуп-прз-iii-микрорайон/) описва проектен обхват. [I микрорайон](https://vladislavovo.bg/micro1/) се отнася до междублоково обновяване. Обща схема **I–V не намерих**. |

За районните карти не намерих отделен изричен лиценз за повторна употреба.

**R2. ИПГВР 2014–2020**

[Официалната директория](https://agup.varna.bg/ipvgr/) съдържа:

- [MR4.zip](https://agup.varna.bg/ipvgr/MR4.zip), **23 779 895 B**: проверен архивен опис — 26 PDF, един XLS, един JPG.
- [MR5.zip](https://agup.varna.bg/ipvgr/MR5.zip), **17 528 608 B**: 17 PDF.

**Няма SHP/KML/GeoJSON/DWG в тези архиви.** Описите са прочетени чрез частични HTTP заявки. Социалната зона обединява Владиславово, Планова, Младост I–II, Възраждане I–III и 26-и подрайон; това не са отделни квартални полигони.

[Докладът от 2013 г.](https://agup.varna.bg/ipvgr/okonchatelen_doklad_ipvgr_varna_101213.pdf) удостоверява ArcGIS Server и исторически публичен модул на [ipgvr-varna.bg](http://www.ipgvr-varna.bg). Действащ REST адрес не установих. [Графично приложение 1](https://www.varna.bg/upload/2964/pril_1_reduced.pdf) е индексирано, но директното прочитане не успя. Отворен лиценз не намерих.

**R3. ОУП и уеб услуги**

Провереният HTML на [графичната част](https://agup.varna.bg/index.php/oup/grafichna-chast) не разкрива вграден ОУП viewer. [Директорията 1:10 000](https://agup.varna.bg/oup_downloads/1/) публикува три JPG: юг **28M**, среда **25M**, Златни пясъци **29M**. ArcGIS връзката в навигацията е към ремонтите на ВиК.

Има отделен [viewer „ОУП Варна“](https://varna.gisbulgaria.bg/bg/map/-2/qdjango/10/). [Началната страница](https://varna.gisbulgaria.bg/bg/) рекламира QGIS/OGC услуги, но не потвърдих конкретен WMS/WFS/WMTS endpoint, работещ слой, лиценз или общинско удостоверяване на оператора; директният HTTP достъп върна 403.

[„Варна ще има дигитален ОУП“](https://varnacouncil.bg/varna-shte-ima-digitalen-obsht-ustrojstven-plan/) е публикация от **2018 г.** [Новината от октомври 2025](https://varna.bg/bg/news/12109) е за достъп до цифрови регулационни планове. Самостоятелен нов квартален регистър/цифров ОУП download за 2023–2026 не установих.

**R4. Работещите DWG връзки**

Източник: [официалната страница](https://agup.varna.bg/index.php/ustroistveni-planove/vlezli-v-sila-pup-011024) → [Drive](https://drive.google.com/drive/folders/1oPc4e-D9oJTDsOZFL_IkJIoFXMpkwofK?usp=sharing). **Всички връзки отговориха HTTP 200 на HEAD с посочения размер; DWG съдържанието не е сваляно.** Имената на териториите са в папките.

| Папка | Файл — пряко изтегляне | Байтове |
|---|---|---:|
| Briz | [pup_2025.dwg](https://drive.google.com/uc?export=download&id=1LnY9lT_oSGxTXYnCDEV2f9cf_NMHIHcN) | 1 389 316 |
| Izgrev | [pur_pup_2025.dwg](https://drive.google.com/uc?export=download&id=17UXBU0o07IGLk9rGT1klxoUqzMx5U6zc) | 8 293 283 |
| Vinica | [pup_2025.dwg](https://drive.google.com/uc?export=download&id=1PK481Y6IjbttrHabcPtsaa5321jjgbct) | 5 327 412 |
| Vinica_sever | [pur_pup_.dwg](https://drive.google.com/uc?export=download&id=1B9Sau19G171q0S8FsEkSUqxN5lGGZupI) | 1 949 055 |
| Vuzrajdane_IV | [pup_2005.dwg](https://drive.google.com/uc?export=download&id=188fEPSukxV_VvWs7JBxkvTDuQ3ZfA2wc) | 606 941 |
| Владиславово / I_m.r | [pup_2025.dwg](https://drive.google.com/uc?export=download&id=1B3bBa7TO3lS6NaiW-qX3E2iYQ7U7WFo5) | 1 216 629 |
| Владиславово / I_m.r | [zona_OD.dwg](https://drive.google.com/uc?export=download&id=1mWE6MdzRVbS5n-mw29rt54nMgyEvUqLC) | 670 311 |
| Владиславово / II_m.r | [pup_2025.dwg](https://drive.google.com/uc?export=download&id=1lGmgz9CcAPU1CzLQ3r54A48XaJkFrxXZ) | 553 682 |
| Владиславово / IV_m.r | [pup_2025.dwg](https://drive.google.com/uc?export=download&id=1eXMLtIxo0huh34D0kY5febhf2NFZfiO5) | 1 690 569 |
| kv_Galata | [pup_2025.dwg](https://drive.google.com/uc?export=download&id=1UqxRmgryHG6r5NOnUuIPa5BJXiI8l4Ay) | 1 252 127 |
| Аспарухово / 28_m.r | [pup_2025.dwg](https://drive.google.com/uc?export=download&id=1L1tspWg7LkYKTXrdgskzXNzyt4d_b1B3) | 2 213 335 |
| Аспарухово / 29_m.r | [pup_2025.dwg](https://drive.google.com/uc?export=download&id=1CSTC18UFLPjCqyRrgyoFV2_ftm3YgmD9) | 2 844 169 |
| Младост / 16_m_r | [pup_2025.dwg](https://drive.google.com/uc?export=download&id=1qElywT_ElnzpacM0892g12RNRy3Mu1fA) | 2 277 075 |
| Младост / 26_m_r | [pup_2025.dwg](https://drive.google.com/uc?export=download&id=1d-bIjl3qOWCFCx-eIfwFH5egpPsiq-MR) | 811 774 |
| kk_Chaika | [pur_pup_.dwg](https://drive.google.com/uc?export=download&id=1ADFcA5vyTjqiY5yjrN1PSg_6e2rWyY74) | 5 958 864 |

`kk_Chaika` е **курортният комплекс**, не доказано ж.к. Чайка. Поименни папки за жилищните Чайка, Трошево, Левски и Победа не намерих. АГУП определя данните като информационни, извлеченията — като неофициални документи; отделен отворен лиценз не е заявен.

**R5. Решения и наредби**

Проверената [Наредба за именуване, редакция 06.02.2008](https://varnacouncil.bg/wp-content/uploads/2017/01/именуване-и-преименуване-на-обекти-с-общинско-значение-към-06.02.2008.pdf) урежда процедурата и изисква скица към предложенията. **Не съдържа квартален граничен регистър.** Конкретен публикуван акт с пълен граничен текст за търсените жилищни квартали не открих.

**R6. Пригодност**

- **ArcGIS „Квартали“:** полигонен слой, но геометрията е недостъпна; кешът не позволява импорт.
- **DWG таблицата:** потенциално извличане без чертане; координатната система, затворените контури и кварталният обхват са непроверени.
- **Одесос, Кайсиева градина, трите проверени Аспаруховски PDF:** векторни; необходимите геореференция и квартални контури не са доказани.
- **ОУП JPG:** изискват георефериране и проследяване на растера.
- **ИПГВР PDF:** инвестиционни зони; готови геореферирани квартални полигони не са потвърдени.
- **Наредбата, регистрите и съобщенията:** текстови източници.

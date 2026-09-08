kimi version 0.34.0
• I need to analyze files in the working directory (copy of the project). Read-only analysis, up to 800 words, verdict ГОДНО/НЕГОДНО with К37-1... checks. Cite paths relative to the project root `kimi_raioni` — but the files are in my temp working dir. The root is .../scratchpad/kimi_raioni. So I should cite paths like the files themselves (they're presumably at root of kimi_raioni). I need to read the JSON files. They may be large. Let me read them.

  Let me start by reading the main table and other files. They might be big — check sizes first.

• Първо ще прочета данните в копието.  8274 imot_bg_varna_areas_08.09.json
  4360 mirela_names.json
 20486 partition_v2_props.json
    34 raioni_imot_overlaps_08.09.json
 89716 raioni_table_08.09.json
 13015 signed60_props.json
 35237 K36_previous.md
171122 total


• The table is 3353 lines. I need the rest. Let me read it in chunks, or better, extract a compact summary with jq/python. Read-only analysis — running jq/python for reading is fine (no writes). Let me use python to dump a compact table.

• Ще извадя компактен изглед на таблицата с Python (само четене).Гръцка махала|gratska-mahala|adv=220|km2=0.34|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=0.7|gap=0|bld=821|notin=1.3|подрайон на Гръцката махала|нов район вътре в Гръцката махала
Фестивален комплекс|festivalen-kompleks|adv=42|km2=0.108|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=None|gap=0|bld=271|notin=2.6|подрайон на Гръцката махала|нов район вътре в Гръцката махала
Конфуто|konfuto|adv=34|km2=0.255|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=None|gap=0|bld=336|notin=5.2|подрайон на ж.к. Победа|нов район вътре в ж.к. Победа
к.к. Слънчев ден|k-k-slanchev-den|adv=111|km2=0.186|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=None|gap=0|bld=40|notin=7.5|подрайон на к.к. Св. Св. Константин и Елена|нов район вътре в к.к. Св. Св. Константин и Елена
м-т Боклук Тарла|m-t-bokluk-tarla|adv=8|km2=0.444|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=0.96|gap=0|bld=29|notin=0.1|подрайон на кв. Владиславово|нов район вътре в кв. Владиславово
Базар Левски|bazar-levski|adv=72|km2=0.169|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=0.59|gap=1|bld=143|notin=2.1|подрайон на кв. Левски|нов район вътре в кв. Левски
Зимно кино Тракия|zimno-kino-trakiya|adv=86|km2=0.269|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=0.3|gap=0|bld=690|notin=0.8|подрайон на кв. Тракия|нов район вътре в кв. Тракия
м-т Франга Дере|m-t-franga-dere|adv=4|km2=0.82|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=0.48|gap=0|bld=528|notin=4.5|подрайон на м-т Кокарджа|нов район вътре в м-т Кокарджа
Пристанище Варна|pristanishte-varna|adv=5|km2=2.276|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=0.31|gap=353|bld=355|notin=98.7|запълва дупка|нов район, запълва дупка
ВИНС-Червен площад|vins-cherven-ploshtad|adv=85|km2=0.144|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=None|gap=219|bld=219|notin=98.5|запълва дупка|нов район, запълва дупка
Чаталджа|chataldzha|adv=108|km2=0.2|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=0.73|gap=211|bld=238|notin=72.7|запълва дупка|нов район, запълва дупка
Гранд Мол|grand-mol|adv=174|km2=0.202|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=None|gap=190|bld=274|notin=78.4|запълва дупка|нов район, запълва дупка
м-т Планова|m-t-planova|adv=31|km2=1.52|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=0.43|gap=126|bld=186|notin=93.4|запълва дупка|нов район, запълва дупка
ЖП Гара|zhp-gara|adv=33|km2=0.204|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=None|gap=66|bld=218|notin=59.3|запълва дупка|нов район, запълва дупка
м-т Атанас Тарла|m-t-atanas-tarla|adv=4|km2=0.614|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=0.92|gap=45|bld=51|notin=73.1|запълва дупка|нов район, запълва дупка
Метро|metro|adv=17|km2=0.41|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=0.93|gap=39|bld=39|notin=99.9|запълва дупка|нов район, запълва дупка
Бизнес парк Варна|biznes-park-varna|adv=14|km2=0.263|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=None|gap=17|bld=26|notin=57.6|запълва дупка|нов район, запълва дупка
Летище|letishte|adv=29|km2=4.73|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=0.04|gap=16|bld=16|notin=100.0|запълва дупка|нов район, запълва дупка
в.з.Звездица|v-z-zvezditsa|adv=10|km2=0.676|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=None|gap=0|bld=0|notin=100.0|запълва дупка|нов район, запълва дупка
м-т Крушките|m-t-krushkite|adv=10|km2=0.888|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=None|gap=0|bld=0|notin=100.0|запълва дупка|нов район, запълва дупка
м-т Орехчето|m-t-orehcheto|adv=10|km2=0.356|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=None|gap=0|bld=0|notin=100.0|запълва дупка|нов район, запълва дупка
м-т Припек|m-t-pripek|adv=4|km2=0.533|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=None|gap=0|bld=0|notin=100.0|запълва дупка|нов район, запълва дупка
с. Звездица|s-zvezditsa|adv=108|km2=1.453|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=None|gap=0|bld=0|notin=100.0|запълва дупка|нов район, запълва дупка
с. Казашко|s-kazashko|adv=14|km2=0.314|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=None|gap=0|bld=0|notin=100.0|запълва дупка|нов район, запълва дупка
с. Каменар|s-kamenar|adv=7|km2=1.17|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=None|gap=0|bld=0|notin=100.0|запълва дупка|нов район, запълва дупка
с. Константиново|s-konstantinovo|adv=61|km2=1.578|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=None|gap=0|bld=0|notin=100.0|запълва дупка|нов район, запълва дупка
с. Тополи|s-topoli|adv=185|km2=1.492|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=None|gap=0|bld=0|notin=100.0|запълва дупка|нов район, запълва дупка
м-т Лазур|m-t-lazur|adv=7|km2=1.454|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=None|gap=0|bld=0|notin=100.0|запълва дупка|нов район, запълва дупка
Лятно кино Тракия|lyatno-kino-trakiya|adv=277|km2=0.499|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=0.15|gap=641|bld=1097|notin=45.9|пресича няколко наши|нов район, пресича няколко наши
ХЕИ|hei|adv=57|km2=0.272|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=0.29|gap=129|bld=326|notin=42.5|пресича няколко наши|нов район, пресича няколко наши
Автогара|avtogara|adv=53|km2=0.225|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=0.78|gap=6|bld=232|notin=15.0|пресича няколко наши|нов район, пресича няколко наши
Бизнес хотел|biznes-hotel|adv=37|km2=0.268|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=0.85|gap=0|bld=354|notin=1.7|пресича няколко наши|нов район, пресича няколко наши
Промишлена зона Тополи|promishlena-zona-topoli|adv=7|km2=0.777|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=None|gap=0|bld=0|notin=46.6|пресича няколко наши|нов район, пресича няколко наши
Централна поща|tsentralna-poshta|adv=115|km2=0.187|ours=None|iou=None|in_ours=None|ours_in=None|iou_m=0.78|gap=0|bld=482|notin=0.0|пресича няколко наши|нов район, пресича няколко наши
м-т Прибой|m-t-priboy|adv=119|km2=1.094|ours=с.о. Прибой|iou=0.76|in_ours=85.2|ours_in=88.0|iou_m=0.49|gap=59|bld=923|notin=14.7|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
м-т Ален мак|m-t-alen-mak|adv=573|km2=1.909|ours=м-т Ален Мак|iou=0.9|in_ours=90.2|ours_in=99.2|iou_m=0.31|gap=46|bld=2309|notin=7.5|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
Галата|galata|adv=383|km2=0.951|ours=кв. Галата|iou=0.67|in_ours=67.3|ours_in=99.8|iou_m=0.57|gap=40|bld=1863|notin=23.0|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
Виница|vinitsa|adv=1413|km2=2.648|ours=кв. Виница|iou=0.64|in_ours=63.8|ours_in=99.5|iou_m=0.5|gap=35|bld=3475|notin=18.2|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
Свети Никола|sveti-nikola|adv=163|km2=1.811|ours=м-т Свети Никола|iou=0.66|in_ours=66.6|ours_in=98.0|iou_m=0.01|gap=31|bld=2318|notin=4.9|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
к.к. Златни пясъци|k-k-zlatni-pyasatsi|adv=499|km2=1.947|ours=к.к. Златни пясъци|iou=0.71|in_ours=82.8|ours_in=83.9|iou_m=None|gap=28|bld=852|notin=11.0|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
Планова промишлена зона|planova-promishlena-zona|adv=6|km2=0.721|ours=ПЗ Планова|iou=0.83|in_ours=87.3|ours_in=94.5|iou_m=0.83|gap=26|bld=335|notin=11.2|подрайон на ПЗ Планова|съвпада с нашия (IoU ≥ 0,6)
Западна промишлена зона|zapadna-promishlena-zona|adv=178|km2=5.133|ours=Западна промишлена зона|iou=0.64|in_ours=72.0|ours_in=86.1|iou_m=0.75|gap=23|bld=1914|notin=14.3|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
м-т Ракитника|m-t-rakitnika|adv=54|km2=0.973|ours=местност Ракитника|iou=0.77|in_ours=88.1|ours_in=86.4|iou_m=0.85|gap=16|bld=1120|notin=7.0|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
м-т Боровец - север|m-t-borovets-sever|adv=104|km2=2.525|ours=с.о. Боровец-север|iou=0.81|in_ours=80.7|ours_in=99.7|iou_m=0.75|gap=14|bld=1972|notin=19.1|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
м-т Боровец - юг|m-t-borovets-yug|adv=223|km2=4.031|ours=с.о. Боровец-юг|iou=0.73|in_ours=77.8|ours_in=92.7|iou_m=0.55|gap=11|bld=2796|notin=16.9|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
Трошево|troshevo|adv=416|km2=1.092|ours=кв. Трошево|iou=0.62|in_ours=83.5|ours_in=70.1|iou_m=0.66|gap=10|bld=1841|notin=9.1|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
м-т Долна Трака|m-t-dolna-traka|adv=225|km2=0.761|ours=Долна Трака|iou=0.84|in_ours=94.8|ours_in=88.3|iou_m=None|gap=10|bld=904|notin=3.9|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
м-т Ментешето|m-t-mentesheto|adv=34|km2=1.047|ours=с.о. Ментеше|iou=0.81|in_ours=86.1|ours_in=93.2|iou_m=0.82|gap=9|bld=832|notin=13.8|подрайон на с.о. Ментеше|съвпада с нашия (IoU ≥ 0,6)
м-т Зеленика|m-t-zelenika|adv=109|km2=1.03|ours=м-т Зеленика|iou=0.92|in_ours=93.2|ours_in=98.9|iou_m=0.85|gap=7|bld=1117|notin=6.8|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
м-т Телевизионна кула|m-t-televizionna-kula|adv=2|km2=0.143|ours=местност Телевизионна кула|iou=0.83|in_ours=85.9|ours_in=95.6|iou_m=None|gap=6|bld=205|notin=14.1|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
Аспарухово|asparuhovo|adv=744|km2=2.342|ours=кв. Аспарухово|iou=0.63|in_ours=96.3|ours_in=64.4|iou_m=0.89|gap=5|bld=4929|notin=3.7|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
Чайка|chayka|adv=187|km2=0.795|ours=кв. Чайка|iou=0.88|in_ours=91.9|ours_in=95.3|iou_m=0.89|gap=5|bld=279|notin=8.1|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
м-т Сълзица|m-t-salzitsa|adv=35|km2=0.996|ours=Сълзица|iou=0.71|in_ours=82.9|ours_in=83.5|iou_m=0.27|gap=5|bld=641|notin=3.0|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
Бриз|briz|adv=902|km2=0.999|ours=ж.к. Бриз|iou=0.63|in_ours=94.1|ours_in=65.9|iou_m=0.31|gap=3|bld=733|notin=3.9|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
Възраждане 4|vazrazhdane-4|adv=135|km2=0.129|ours=ж.к. Възраждане 4|iou=0.69|in_ours=92.5|ours_in=72.6|iou_m=None|gap=2|bld=183|notin=3.6|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
Христо Ботев|hristo-botev|adv=83|km2=0.531|ours=кв. Христо Ботев|iou=0.69|in_ours=90.8|ours_in=74.2|iou_m=0.57|gap=2|bld=2851|notin=2.7|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
Цветен квартал|tsveten-kvartal|adv=329|km2=0.613|ours=Цветен квартал|iou=0.86|in_ours=86.2|ours_in=99.6|iou_m=0.89|gap=2|bld=1241|notin=4.6|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
м-т Перчемлията|m-t-perchemliyata|adv=88|km2=0.987|ours=с.о. Перчемлията|iou=0.87|in_ours=97.0|ours_in=89.3|iou_m=None|gap=2|bld=191|notin=3.0|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
м-т Добрева чешма|m-t-dobreva-cheshma|adv=62|km2=1.508|ours=с.о. Добрева чешма|iou=0.82|in_ours=87.9|ours_in=92.7|iou_m=None|gap=2|bld=1184|notin=12.1|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
Островна промишлена зона|ostrovna-promishlena-zona|adv=8|km2=1.745|ours=Островна промишлена зона|iou=0.97|in_ours=98.1|ours_in=98.4|iou_m=0.92|gap=1|bld=595|notin=1.9|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
м-т Балам Дере|m-t-balam-dere|adv=20|km2=0.42|ours=с.о. Балъм дере|iou=0.76|in_ours=97.3|ours_in=77.7|iou_m=0.85|gap=1|bld=188|notin=2.4|подрайон на с.о. Балъм дере|съвпада с нашия (IoU ≥ 0,6)
м-т Кочмар|m-t-kochmar|adv=9|km2=0.414|ours=с.о. Кочмар|iou=0.76|in_ours=83.2|ours_in=89.5|iou_m=0.0|gap=1|bld=483|notin=8.0|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
Възраждане 1|vazrazhdane-1|adv=409|km2=0.455|ours=ж.к. Възраждане 1|iou=0.86|in_ours=98.2|ours_in=87.3|iou_m=None|gap=0|bld=360|notin=0.9|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
Възраждане 2|vazrazhdane-2|adv=107|km2=0.415|ours=ж.к. Възраждане 2|iou=0.97|in_ours=96.9|ours_in=99.8|iou_m=None|gap=0|bld=157|notin=0.2|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
Възраждане 3|vazrazhdane-3|adv=318|km2=0.209|ours=ж.к. Възраждане 3|iou=0.92|in_ours=92.2|ours_in=100.0|iou_m=None|gap=0|bld=74|notin=2.7|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
Завод Дружба|zavod-druzhba|adv=22|km2=0.3|ours=Завод Дружба|iou=0.69|in_ours=69.8|ours_in=99.4|iou_m=0.51|gap=0|bld=293|notin=2.4|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
Изгрев|izgrev|adv=436|km2=2.926|ours=кв. Изгрев|iou=0.76|in_ours=99.9|ours_in=75.9|iou_m=0.18|gap=0|bld=2806|notin=0.1|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
Кайсиева градина|kaysieva-gradina|adv=832|km2=0.48|ours=кв. Кайсиева градина|iou=0.87|in_ours=87.6|ours_in=99.6|iou_m=0.94|gap=0|bld=287|notin=0.3|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
Колхозен пазар|kolhozen-pazar|adv=401|km2=0.222|ours=Колхозен пазар|iou=0.72|in_ours=99.2|ours_in=71.9|iou_m=0.72|gap=0|bld=1129|notin=0.4|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
Младост 2|mladost-2|adv=169|km2=0.666|ours=ж.к. Младост 2|iou=0.84|in_ours=84.2|ours_in=100.0|iou_m=None|gap=0|bld=384|notin=1.0|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
Спортна зала|sportna-zala|adv=59|km2=0.171|ours=Спортна зала|iou=0.96|in_ours=99.0|ours_in=97.0|iou_m=0.38|gap=0|bld=206|notin=1.0|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
к.к. Св.Св. Константин и Елена|k-k-sv-sv-konstantin-i-elena|adv=610|km2=1.264|ours=к.к. Св. Св. Константин и Елена|iou=0.7|in_ours=95.9|ours_in=71.7|iou_m=None|gap=0|bld=671|notin=3.7|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
м-т Кантара|m-t-kantara|adv=18|km2=0.71|ours=Местност Кантара|iou=0.87|in_ours=95.4|ours_in=90.8|iou_m=None|gap=0|bld=557|notin=4.0|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
м-т Пчелина|m-t-pchelina|adv=291|km2=0.784|ours=с.о. Пчелина|iou=0.87|in_ours=98.5|ours_in=88.4|iou_m=0.56|gap=0|bld=774|notin=1.2|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
Младост 1|mladost-1|adv=431|km2=0.376|ours=ж.к. Младост 1|iou=0.64|in_ours=91.1|ours_in=68.8|iou_m=0.3|gap=0|bld=265|notin=1.6|същият квартал, друго чертане|съвпада с нашия (IoU ≥ 0,6)
в.з.Виница - север|v-z-vinitsa-sever|adv=1|km2=0.303|ours=с.о. Добрева чешма|iou=0.0|in_ours=0.0|ours_in=0.0|iou_m=None|gap=2|bld=294|notin=2.2|подрайон на с.о. Добрева чешма|същото име, различно чертане (IoU 0.00)
к.к. Чайка|k-k-chayka|adv=373|km2=1.394|ours=кв. Чайка|iou=0.0|in_ours=0.0|ours_in=0.0|iou_m=0.0|gap=1|bld=1360|notin=0.8|същият квартал, друго чертане|същото име, различно чертане (IoU 0.00)
Владислав Варненчик 2|vladislav-varnenchik-2|adv=108|km2=0.982|ours=кв. Кайсиева градина|iou=0.0|in_ours=0.0|ours_in=0.0|iou_m=0.92|gap=0|bld=1219|notin=0.7|подрайон на кв. Владиславово|същото име, различно чертане (IoU 0.00)
Операта|operata|adv=84|km2=0.284|ours=Операта|iou=0.01|in_ours=0.7|ours_in=100.0|iou_m=0.84|gap=0|bld=898|notin=0.0|подрайон на Център|същото име, различно чертане (IoU 0.01)
Стадион Спартак|stadion-spartak|adv=4|km2=0.235|ours=Стадион Спартак|iou=0.09|in_ours=9.3|ours_in=100.0|iou_m=0.8|gap=172|bld=346|notin=56.0|запълва дупка|същото име, различно чертане (IoU 0.09)
м-т Горна Трака|m-t-gorna-traka|adv=269|km2=2.896|ours=с.о. Горна Трака|iou=0.15|in_ours=15.0|ours_in=85.1|iou_m=None|gap=27|bld=3617|notin=9.0|пресича няколко наши|същото име, различно чертане (IoU 0.15)
Левски 1|levski-1|adv=537|km2=0.524|ours=кв. Левски|iou=0.24|in_ours=96.0|ours_in=24.6|iou_m=None|gap=1|bld=446|notin=4.0|подрайон на кв. Левски|същото име, различно чертане (IoU 0.24)
Владислав Варненчик 1|vladislav-varnenchik-1|adv=911|km2=0.833|ours=кв. Владиславово|iou=0.24|in_ours=96.5|ours_in=24.3|iou_m=None|gap=0|bld=474|notin=0.6|подрайон на кв. Владиславово|същото име, различно чертане (IoU 0.24)
Максуда|maksuda|adv=3|km2=0.654|ours=Максуда|iou=0.29|in_ours=30.3|ours_in=85.2|iou_m=0.14|gap=2|bld=4145|notin=3.4|пресича няколко наши|същото име, различно чертане (IoU 0.29)
Левски 2|levski-2|adv=161|km2=0.678|ours=кв. Левски|iou=0.33|in_ours=99.4|ours_in=33.0|iou_m=0.61|gap=0|bld=785|notin=0.0|подрайон на кв. Левски|същото име, различно чертане (IoU 0.33)
Център|tsentar|adv=823|km2=0.837|ours=Център|iou=0.37|in_ours=56.6|ours_in=51.3|iou_m=0.1|gap=257|bld=1648|notin=16.7|същият квартал, друго чертане|същото име, различно чертане (IoU 0.37)
Победа|pobeda|adv=145|km2=0.358|ours=ж.к. Победа|iou=0.41|in_ours=80.1|ours_in=46.2|iou_m=0.36|gap=9|bld=272|notin=11.6|същият квартал, друго чертане|същото име, различно чертане (IoU 0.41)
м-т Евксиноград|m-t-evksinograd|adv=163|km2=0.864|ours=Евксиноград|iou=0.44|in_ours=91.4|ours_in=45.6|iou_m=0.0|gap=0|bld=1381|notin=5.7|същият квартал, друго чертане|същото име, различно чертане (IoU 0.44)
м-т Манастирски рид|m-t-manastirski-rid|adv=246|km2=4.093|ours=с.о. Манастирски рид|iou=0.47|in_ours=48.3|ours_in=94.1|iou_m=None|gap=126|bld=3256|notin=10.9|пресича няколко наши|същото име, различно чертане (IoU 0.47)
Погреби|pogrebi|adv=357|km2=0.229|ours=Погребите|iou=0.47|in_ours=54.0|ours_in=79.2|iou_m=0.51|gap=0|bld=1037|notin=7.7|пресича няколко наши|същото име, различно чертане (IoU 0.47)
м-т Салтанат|m-t-saltanat|adv=22|km2=0.856|ours=м-т Салтанат|iou=0.51|in_ours=58.1|ours_in=80.0|iou_m=None|gap=1|bld=272|notin=13.8|пресича няколко наши|същото име, различно чертане (IoU 0.51)
м-т Акчелар|m-t-akchelar|adv=134|km2=0.855|ours=м-т Акчелар|iou=0.54|in_ours=78.7|ours_in=63.8|iou_m=0.75|gap=13|bld=946|notin=14.8|същият квартал, друго чертане|същото име, различно чертане (IoU 0.54)
Окръжна болница-Генерали|okrazhna-bolnitsa-generali|adv=171|km2=0.272|ours=Генералите|iou=0.55|in_ours=55.5|ours_in=100.0|iou_m=None|gap=2|bld=438|notin=7.5|пресича няколко наши|същото име, различно чертане (IoU 0.55)
м-т Фичоза|m-t-fichoza|adv=14|km2=0.564|ours=м-т Фичоза|iou=0.57|in_ours=82.9|ours_in=64.7|iou_m=0.25|gap=26|bld=368|notin=17.1|същият квартал, друго чертане|същото име, различно чертане (IoU 0.57)
м-т Сотира|m-t-sotira|adv=76|km2=1.858|ours=м-т Сотира|iou=0.59|in_ours=61.0|ours_in=93.9|iou_m=0.75|gap=117|bld=1826|notin=17.7|същият квартал, друго чертане|същото име, различно чертане (IoU 0.59)


• Now I have the full table. I need additional data: partition_v2_props.json, signed60_props.json, imot_bg_varna_areas_08.09.json, mirela_names.json, K36_previous.md. Also need overlaps detail for specific rows (Владислав Варненчик 2, к.к. Чайка, в.з.Виница-север) to determine correct pairs. Let me extract overlaps for those rows plus check areas of parent cells (Левски, Владиславово, Възраждане) from partition/signed props.

• Сега останалите файлове и детайлите за ключовите редове.Базар Левски -> None | overlaps: [('кв. Левски', 97.4, 11.5, 'подписан'), ('Завод Дружба', 0.5, 0.4, 'предложен (Wikimapia 34550221)')]
м-т Планова -> None | overlaps: [('ж.к. Възраждане 4', 2.7, 25.2, 'подписан'), ('ПЗ Планова', 2.2, 5.0, 'подписан'), ('с.о. Балъм дере', 1.6, 4.5, 'подписан'), ('ж.к. Възраждане', 0.1, 4.3, 'подписан'), ('Сълзица', 0.1, 0.1, 'предложен (Wikimapia 15278589)')]
Метро -> None | overlaps: [('кв. Владиславово', 0.1, 0.0, 'подписан')]
Възраждане 4 -> ж.к. Възраждане 4 | overlaps: [('ж.к. Възраждане 4', 92.5, 72.6, 'подписан'), ('ж.к. Възраждане', 3.8, 15.6, 'подписан')]
Цветен квартал -> Цветен квартал | overlaps: [('Цветен квартал', 86.2, 99.6, 'предложен (Wikimapia 6805503)'), ('ж.к. Победа', 5.1, 5.1, 'подписан'), ('кв. Левски', 3.8, 1.6, 'подписан'), ('м-т Кокарджа', 0.1, 0.1, 'подписан'), ('кв. Изгрев', 0.1, 0.0, 'подписан')]
Възраждане 1 -> ж.к. Възраждане 1 | overlaps: [('ж.к. Възраждане 1', 97.5, 87.3, 'подписан'), ('ж.к. Младост 1', 1.1, 1.0, 'подписан'), ('ж.к. Възраждане', 0.5, 6.9, 'подписан'), ('ж.к. Младост', 0.0, 0.0, 'подписан')]
Възраждане 2 -> ж.к. Възраждане 2 | overlaps: [('ж.к. Възраждане 2', 96.9, 99.8, 'подписан'), ('ж.к. Възраждане', 1.7, 21.9, 'подписан'), ('ж.к. Възраждане 1', 1.1, 0.9, 'подписан'), ('ж.к. Младост', 0.0, 0.1, 'подписан'), ('ж.к. Младост 2', 0.0, 0.0, 'подписан')]
Възраждане 3 -> ж.к. Възраждане 3 | overlaps: [('ж.к. Възраждане 3', 92.2, 100.0, 'подписан'), ('ж.к. Възраждане', 5.0, 32.9, 'подписан'), ('с.о. Пчелина', 0.1, 0.0, 'подписан'), ('ж.к. Младост', 0.0, 0.0, 'подписан')]
Завод Дружба -> Завод Дружба | overlaps: [('Завод Дружба', 69.8, 99.4, 'предложен (Wikimapia 34550221)'), ('Център', 15.9, 2.5, 'предложен (разширен Център)'), ('кв. Левски', 11.3, 2.4, 'подписан'), ('Спортна зала', 0.3, 0.5, 'предложен (Wikimapia 10798113)'), ('кв. Чайка', 0.3, 0.1, 'подписан')]
в.з.Виница - север -> с.о. Добрева чешма | overlaps: [('с.о. Добрева чешма', 95.6, 16.5, 'подписан'), ('кв. Виница', 2.2, 0.4, 'подписан')]
к.к. Чайка -> кв. Чайка | overlaps: [('к.к. Чайка', 98.3, 81.8, 'подписан'), ('к.к. Св. Св. Константин и Елена', 0.8, 0.8, 'подписан'), ('м-т Ален Мак', 0.1, 0.1, 'подписан')]
Владислав Варненчик 2 -> кв. Кайсиева градина | overlaps: [('кв. Владиславово', 99.2, 39.6, 'подписан'), ('с.о. Балъм дере', 0.1, 0.1, 'подписан')]
Операта -> Операта | overlaps: [('Център', 97.0, 14.6, 'предложен (разширен Център)'), ('Гръцката махала', 2.3, 1.4, 'подписан'), ('Операта', 0.7, 100.0, 'OSM way 176509102 (building=civic, №1; вътре са OSM възлите „Държавна опера - Варна“ 13106376246 и „Драматичен театър „Стоян Бъчваров““ 13106376247; до него „Шадравана до Операта“)')]
Стадион Спартак -> Стадион Спартак | overlaps: [('Център', 34.5, 4.3, 'предложен (разширен Център)'), ('Стадион Спартак', 9.3, 100.0, 'Wikimapia 5548944 „Стадион „Спартак““ (41 точки); същият контур в OSM way 1305399349 leisure=stadium (Wikidata Q5245085)'), ('кв. Левски', 0.3, 0.0, 'подписан')]
м-т Горна Трака -> с.о. Горна Трака | overlaps: [('Евксиноград', 29.6, 49.6, 'подписан'), ('Селищно образувание Фатрико дере', 26.5, 98.8, 'предложен (Wikimapia 20340098)'), ('Средна Трака', 19.4, 98.6, 'подписан'), ('с.о. Горна Трака', 15.0, 85.1, 'подписан'), ('Селищно образувание Сава', 0.3, 0.7, 'предложен (Wikimapia 5306518)'), ('м-т Акчелар', 0.0, 0.1, 'подписан')]
Левски 1 -> кв. Левски | overlaps: [('кв. Левски', 96.0, 35.0, 'подписан')]
Владислав Варненчик 1 -> кв. Владиславово | overlaps: [('кв. Владиславово', 94.3, 32.0, 'подписан'), ('с.о. Балъм дере', 5.1, 8.1, 'подписан')]
Максуда -> Максуда | overlaps: [('кв. Св. Иван Рилски', 61.7, 62.3, 'подписан'), ('Максуда', 30.3, 85.2, 'подписан'), ('кв. Христо Ботев', 4.4, 4.4, 'подписан'), ('Западна промишлена зона', 0.3, 0.0, 'подписан')]
Левски 2 -> кв. Левски | overlaps: [('кв. Левски', 99.3, 46.8, 'подписан'), ('кв. Изгрев', 0.6, 0.1, 'подписан'), ('Цветен квартал', 0.2, 0.2, 'предложен (Wikimapia 6805503)')]
Център -> Център | overlaps: [('Център', 80.9, 35.9, 'предложен (разширен Център)'), ('кв. Тракия', 1.2, 2.0, 'подписан'), ('Гръцката махала', 0.9, 1.6, 'подписан'), ('Общината', 0.3, 100.0, 'OSM way 983640688 „Община Варна“ (amenity=townhall, кулата, 15 етажа) ∪ OSM way 47704367 (building=government, 3 етажа) — двете на бул. 8-ми Приморски полк 43')]


• Now I need signed60_props.json (codes/relationships), mirela_names.json, imot_bg_varna_areas_08.09.json, and K36_previous.md briefly. Also note the interesting fact: "Център" overlaps show only 80.9% in expanded Център but pct_imot_in_ours=56.6 in the compact table — the overlaps listing shows only top overlaps; 56.6 might include other cells? Actually overlaps list for Център shows Център 80.9 pct_of_imot, pct_of_ours 35.9. Hmm but row said in_ours=56.6/ours_in=51.3. Wait the overlaps show pct_of_imot=80.9 into Център, but row field pct_imot_in_ours=56.6? Inconsistency — maybe pct_imot_in_ours is against best single ours polygon... Actually for Център row: iou=0.37, in_ours=56.6, ours_in=51.3. But overlap entry says 80.9% of imot is in our Център and 35.9% of ours. Hmm, discrepancy. Maybe overlaps rounded/only polygon area vs the row stats computed differently? Let me not worry; note it as a data quality flag maybe (К37 checks). Actually wait — maybe overlaps list is truncated? It showed only top entries. For Център: entries sum 80.9+1.2+0.9+0.3 = 83.3, leaving ~16.7% not in ours = matches notin=16.7. So pct_imot_in_ours=56.6 doesn't match 80.9. That's an inconsistency in the table itself! Hmm. Or pct_imot_in_ours might be "weighted centroid" or computed on buildings rather than area. Note: IoU 0.37 with in 56.6/ours_in 51.3 is consistent: IoU = in*ours_in/(in+ours_in-in*ours_in)... check: intersection = 56.6% of imot. ours_in=51.3% means intersection=51.3% of ours. IoU=0.566*A/(A+...) fine. But overlaps entry says 80.9% of imot in Център and 35.9% of ours in imot. Then IoU would be different. So there IS an internal inconsistency between row-level pct fields and overlaps arrays for Център. Interesting — worth flagging. Actually maybe overlaps percentages are computed on a different geometry (buffered?) Hmm. For other rows: Възраждане 4: row in_ours=92.5, ours_in=72.6; overlaps: 92.5/72.6 — matches. Левски 1: row in_ours=96.0, ours_in=24.6; overlaps: 96.0/35.0 — pct_of_imot matches, pct_of_ours differs (24.6 vs 35.0)! Hmm. Център: row 56.6/51.3 vs overlaps 80.9/35.9 — both differ. Maybe row pct fields use different ours polygon version than overlaps. This is a data-quality flag for the gate (К37-?). Let me check a few more: Кайсиева: row 87.6/99.6. Not in my overlaps print. Погреби: row 54.0/79.2. Let me verify against overlaps. I'll extract overlaps for the 20 "същото име" rows.

  Also need signed60_props.json for parent-child (Левски children: Базар Левски? Завод Дружба parent kv_levski, Цветен квартал parent kv_levski). And task 4: does Левски 1+2+Базар Левски+Завод Дружба+Цветен квартал cover our кв. Левски (area 1.437 km², lost 29.5%)? Sum imot areas: Левски 1: 0.524*0.96 in Левски? pct_of_ours: Левски 1 covers 35.0% (overlaps) or 24.6% (row) of our Левски; Левски 2: 46.8/33.0. Завод Дружба: 11.3% of imot in кв. Левски = 2.4% of ours; but Завод Дружба our cell has parent kv_levski and is inside? Цветен квартал: 3.8% of imot in Левски=1.6% of ours, but our Цветен квартал cell (0.53 km², parent kv_levski). Hmm — our partition: kv_levski area 1.437, lost_pct 29.5 (probably lost to children Цветен квартал + Завод Дружба which were carved out). So total Levski-ish = 1.437 + 0.53 + 0.211 = 2.178? And imot Левски1+2 = 0.524+0.678=1.202, mostly inside кв. Левски (96%/99.4%). Coverage of our кв. Левски by imot children: 35.0+46.8 (if non-overlapping) = 81.8% + Базар Левски 11.5% + Завод Дружба 2.4% + Цветен 1.6% ≈ 97%? But imot children may overlap each other? Overlaps file says 0 pairs among all 95 imot polygons, so no mutual overlap. But careful: pct_of_ours values 35.0 (Левски 1) + 46.8 (Левски 2) + 11.5 (Базар) + 2.4 (Завод) + 1.6 (Цветен) = 97.3% — but that uses overlaps pct_of_ours; row-level says 24.6+33.0=57.6. Inconsistency again. Sum area check: our кв. Левски 1.437 km². imot pieces inside: Л1 0.524*0.96=0.503, Л2 0.678*0.994=0.674, Базар 0.169*0.974=0.165, Завод 0.30*0.113=0.034 (only 11.3% of Завод imot is in Левски — rest in Център 15.9%, etc. — actually Завод Дружба imot overlaps our Завод Дружба 69.8%), Цветен 0.613*0.038=0.023. Sum ≈ 1.399 / 1.437 = 97.4%. OK consistent with overlaps pct. So Левски 1+2+Базар ≈ cover ~93% of кв. Левски; remainder ~3%. Good.

  Възраждане: our cells: ж.к. Възраждане (0.032, lost 97.5%), Възр 1 (0.508), 2 (0.403), 3 (0.192), 4 (0.164). imot: Възраждане 1 (0.455): 97.5% in Възр1 covering 87.3% of it; Възр2 (0.415): 96.9% in, covers 99.8%; Възр3 (0.209): 92.2% covers 100%; Възр4 (0.129): 92.5% covers 72.6% + 3.8% in ж.к. Възраждане parent covering 15.6%. Also Възр2 overlaps parent Възраждане 1.7% covering 21.9%, Възр3 5.0% covering 32.9%. Parent ж.к. Възраждане area 0.032: covered 15.6+21.9+32.9 = 70.4% by imot children. Hmm interesting.

  Владиславово: our кв. Владиславово 2.459 (lost 25.8% — carved Кайсиева 0.422). imot Владислав Варненчик 1 (0.833): 94.3% in Владиславово, covers 32.0%; ВВ2 (0.982): 99.2% in Владиславово, covers 39.6%; Боклук Тарла (0.444): 99.5% in, covers 17.9%. Sum 32.0+39.6+17.9 = 89.5% coverage of Владиславово. Remainder ~10%. Also Кайсиева imot (0.48): 87.6% in Кайсиева covering 99.6%.

  Key finding for task 1: The ALIAS mapping Владислав Варненчик 2 → Кайсиева градина is WRONG: overlaps show ВВ2 is 99.2% inside кв. Владиславово (39.6% of it), iou_mirela=0.92 — wait, iou_m=0.92 with mirela! And Кайсиева imot separately matches Кайсиева with IoU 0.87 and mirela 0.94. So correct pair: Владислав Варненчик 2 → кв. Владиславово (subdistrict), same as ВВ1. And mirela's "Владислав Варненчик 2" presumably matches too.

  к.к. Чайка: row says ours=кв. Чайка with IoU 0.0, but overlaps show imot к.к. Чайка is 98.3% inside OUR к.к. Чайка (chaika_kk, 1.675 km²), covering 81.8%. So the alias resolution picked the wrong Chaika — correct pair: к.к. Чайка → к.к. Чайка (chaika_kk), IoU would be ~0.79. Meanwhile imot "Чайка" (0.795) → кв. Чайка (chaika_kv) IoU 0.88, correct. So at imot "Чайка" = the квартал, "к.к. Чайка" = the resort; at us: chaika_kv = квартал, chaika_kk = курорт. The mapping bug: name matcher mapped "к.к. Чайка"→"кв. Чайка" (probably normalized stripping к.к./кв. prefixes).

  в.з.Виница - север → mapped to с.о. Добрева чешма IoU 0.0; overlaps: 95.6% in Добрева чешма covering 16.5%, 2.2% in Виница. The ALIAS said Виница-север→Добрева чешма. Hmm — is that wrong? imot's в.з.Виница-север lies almost entirely inside our Добрева чешма cell. Our partition has no "Виница-север" cell. So as a geometric match it's actually "подрайон на с.о. Добрева чешма" — the alias is geometrically right, the verdict label "същото име, различно чертане (IoU 0.00)" is wrong (it's not same-name-different-drawing; it's a new subdistrict inside Добрева чешма). Also mirela? iou_m=None. Whether imot's Виница-север is correct vs our Добрева чешма boundary — mirela has no opinion. Area 0.303, only 1 advert.

  Операта: ours=Операта (our landmark 0.002 km², just the building). imot Операта 0.284 km² — a neighborhood around the Opera, 97% inside Център. So it's a "нов район вътре в Център", not same-name. Our Операта is an ориентир (building). The comparison is apples-to-oranges.

  Планова промишлена зона → ПЗ Планова IoU 0.83 — alias Планова ПЗ→ПЗ Планова correct. Метро→ПЗ Метро: ours=None! Row shows ours=None, gap=39, 99.9% not in ours. Wait — ALIAS said Метро→ПЗ Метро. But table shows ours=null and verdict "нов район, запълва дупка". Do we have a "ПЗ Метро" cell? partition_v2_props has no Метро. signed60? Need to check. iou_m=0.93 — mirela has Метро with IoU 0.93 agreement. Our partition lacks it entirely (it's a gap). So alias Метро→ПЗ Метро maps to a non-existent ours? Check signed60_props.json.

  Окръжна болница-Генерали → Генералите: row iou=0.55, ours_in=100%, in_ours=55.5%, cls "пресича няколко наши". Our Генералите is 0.151 km² Wikimapia zone. imot's is 0.272. mirela iou None. Overlaps? Not printed. Alias seems plausible (100% of ours inside imot's).

  Погреби → Погребите: iou 0.47, in 54.0, ours_in 79.2, mirela 0.51. Both ours and mirela are ~0.156-ish? Our Погребите 0.156 km²; imot 0.229. mirela IoU with imot 0.51 — so three-way partial agreement. Alias fine.

  Now task 2: the 20 "същото име, различно чертане" rows with rule-based adjudication. List them with numbers:

  1. в.з.Виница-север 0.00 — misclassified (new subdistrict), see above.
  2. к.к. Чайка 0.00 — wrong alias, real IoU ~0.79 → our + imot agree.
  3. Владислав Варненчик 2 0.00 — wrong alias; it's subdistrict of Владиславово, mirela 0.92 agrees with imot → our Владиславово boundary NOT in question (imot ВВ1+ВВ2 both ⊂ our Владиславово 96-99%).
  4. Операта 0.01 — ours is a building landmark; imot's is a micro-district inside Център; imot right for market use; mirela 0.84 supports imot? iou_m=0.84 means imot vs mirela agree → ours (building-only) not comparable.
  5. Стадион Спартак 0.09 — ours is the stadium polygon (0.022 km², ориентир); imot's is a neighborhood 0.235 km² with gap=172 buildings, 56% not in ours; mirela 0.8 agrees with imot → imot/mirela right as district; ours is just the stadium.
  6. м-т Горна Трака 0.15 — imot 2.896 km² spans Евксиноград 29.6%, Фатрико дере 26.5%, Средна Трака 19.4%, Горна Трака 15.0%. imot's "Горна Трака" = whole Traka ridge; ours is a sub-piece. mirela None. Our finer partition arguably better; imot too coarse (swallows 4 signed cells).
  7. Левски 1 0.24, 8. Левски 2 0.33 — subdistricts of кв. Левски, not alternatives; our parent stays, imot adds granularity. mirela: Л2 0.61.
  9. Владислав Варненчик 1 0.24 — same pattern.
  10. Максуда 0.29 — imot 0.654 km²: 61.7% in Св. Иван Рилски, 30.3% in Максуда (85.2% of ours covered), 4.4% Ботев. mirela 0.14 low. Our Максуда small (0.232). imot's Максуда spills into Rilski — but note our Rilski lost_pct 12.3. Hmm. mirela disagrees with imot (0.14). Two-agency rule: mirela IoU <0.7 → imot not confirmed; our boundary plausible; imot overexpanded north/west. Also Максуда gap=2 only.
  11. Център 0.37 — ours is "предложен (разширен Център)" 1.887 km² vs imot 0.837. mirela 0.1 (very low — mirela's Център differs from both?). gap=257. ours_in 51.3, in_ours 56.6. Also internal inconsistency (overlaps say 80.9% of imot in our Център). mirela IoU 0.1 → no second agency support for imot. Hmm, but mirela low against imot means mirela disagrees with imot too. Our expanded Център absorbs Чаталджа etc. Judgment: unresolved; imot's tighter core + separate microdistricts (ЖП Гара, ХЕИ, Централна поща, Операта, Бизнес хотел) is more granular and consistent; our expanded Център is a proposal, unsigned. So imot likely better here, with microdistricts as children.
  12. Победа 0.41 — ours 0.62 vs imot 0.358; in_ours 80.1, ours_in 46.2; mirela 0.36 (low). imot smaller; Конфуто+Гранд Мол carved out of our Победа (Конфуто 94.8% in Победа covering 39%; Гранд Мол 21.3% in Победа). So our Победа = imot Победа + Конфуто + parts. imot more granular; mirela doesn't confirm either (0.36). Gap 9.
  13. Евксиноград 0.44 — ours 1.73 vs imot 0.864; imot ⊂ ours 91.4%, covers 45.6%; mirela 0.0 — mirela's Евксиноград totally different (or the palace park?). Our cell lost 0.2%. imot Горна Трака takes 29.6% of our Евксиноград (49.6% of imot GT). So the dispute: our Евксиноград includes what imot calls Горна Трака. mirela supports neither. Hmm.
  14. Манастирски рид 0.47 — ours 1.929 vs imot 4.093 (!); imot covers 94.1% of ours but is 2x bigger, gap=126, mirela None. imot overexpanded? Our children (Дилбер чешма, Кокодива, etc. proposed inside). imot's 4.09 km² with 48.3% in ours — the rest spills to...? cls "пресича няколко наши". Probably imot includes Фатрико дере/Сава direction? Need overlaps. Not critical; rule: no mirela confirmation + huge size discrepancy + crosses many cells → imot's contour unreliable; keep ours.
  15. Погреби 0.47 — mirela 0.51 (medium). Three-way partial; ours 0.156 smallest; imot 0.229; in_ours 54%, ours_in 79.2%. mirela agrees with imot at 0.51 only — below 0.7 → unresolved, lean ours (signed? ours is "предложен (Wikimapia)" — actually Погребите is предложен, not signed). Both weak; imot has 357 adverts and mirela closer to imot than to ours → lean imot.
  16. Салтанат 0.51 — ours 0.622 vs imot 0.856; in 58.1/80.0; mirela None; crosses several. No confirmation → keep ours (signed), investigate.
  17. Акчелар 0.54 — ours 1.055 vs imot 0.855; in 78.7/63.8; mirela 0.75 ≥0.7 → imot & mirela agree → ours (signed but too big?) under question. Note Акчелар Горна Трака overlap.
  18. Окръжна болница-Генерали 0.55 — ours 0.151 ⊂ imot 100%, imot bigger (0.272); mirela None. Ours is Wikimapia proposal; imot's includes болница area; crosses several cells. Lean imot (ours too small), but no second confirmation.
  19. Фичоза 0.57 — ours 0.723 vs imot 0.564; in 82.9/64.7; mirela 0.25 low; gap 26. mirela disagrees → keep ours; imot smaller.
  20. Сотира 0.59 — ours 1.207 vs imot 1.858; in 61.0/93.9; mirela 0.75 ≥0.7 → mirela confirms imot → ours under question (ours too small / imot includes surroundings).

  Rule formulation: mirela IoU ≥0.7 with imot + ours IoU <0.6 → our contour suspect (Акчелар, Сотира; and via alias fixes к.к. Чайка where ours actually agrees). mirela <0.4 + ours signed → keep ours, imot over/under-expanded (Максуда, Фичоза, Център, Победа, Евксиноград, Изгрев...). Ours=ориентир (building) → not comparable, imot defines the microdistrict (Операта, Стадион Спартак, Общината). Subdistricts (Левски 1/2, ВВ 1/2) → not competing, add as children.

  Task 3: 34 new districts table with code, kind, district, parent, class "обект". The 34 "нов район" verdicts: 6 "пресича няколко наши" + 20 "запълва дупка" + 1 Левски + 2 Гръцка махала + 1 Победа + 1 Кокарджа + 1 Тракия + 1 Константин и Елена + 1 Владиславово = 34. Let me enumerate:

  пресича няколко наши (6): Лятно кино Тракия, ХЕИ, Автогара, Бизнес хотел, Промишлена зона Тополи, Централна поща.
  запълва дупка (20): Пристанище Варна, ВИНС-Червен площад, Чаталджа, Гранд Мол, м-т Планова, ЖП Гара, м-т Атанас Тарла, Метро, Бизнес парк Варна, Летище, в.з.Звездица, м-т Крушките, м-т Орехчето, м-т Припек, с. Звездица, с. Казашко, с. Каменар, с. Константиново, с. Тополи, м-т Лазур.
  вътре в: Гръцка махала, Фестивален комплекс (Гръцката махала); Конфуто (Победа); к.к. Слънчев ден (К и Е); м-т Боклук Тарла (Владиславово); Базар Левски (Левски); Зимно кино Тракия (Тракия); м-т Франга Дере (Кокарджа) = 8. Total 6+20+8=34 ✓.

  Need: код (snake_case), вид (район/зона/м-т/с.), район на общината (одесос/приморски/младост/аспарухово/владислав варненчик/аврен?), родител, клас "обект" for Гранд Мол, Бизнес хотел, Летище, Пристанище, Бизнес парк.

  Districts: с. Звездица, в.з.Звездица — Звездица is in Аспарухово district? Actually Звездица is part of Аспарухово район. Казашко, Каменар, Константиново, Тополи — Аврен/Аксаково municipalities, not Варна! с. Казашко, с. Каменар, с. Константиново, с. Тополи are in община Аврен/Аксаково — outside Варна municipality. м-т Припек, м-т Крушките, м-т Орехчето, м-т Лазур — these are near Звездица/Тополи area (Припек is м-т near Звездица). Hmm, м-т Лазур... near Каменар? I should be careful. Within the scope of this analysis (no internet), I can note they fall outside our partition entirely (100% not in ours, 0 buildings in our address base) and likely outside град Варна — flag for scope decision rather than assert exact municipality. Тополи/Казашко/Каменар/Константиново are села in община Аврен (Тополи, Казашко, Каменар?) — actually Казашко is община Ветрино? Hmm. Казашко is in община Ветрино? No... Казашко — община Аврен? I recall Казашко is in община Аврен? There's Казашко near Варна in община Аврен... Actually с. Казашко is община Провадия? Let me not assert. I'll say "извън гр. Варна (общини Аврен/Аксаково — да се потвърди)". K36_previous.md might mention. Should check K36 and mirela_names and imot_bg areas files. Also signed60_props for codes.

  Buildings=0 for these villages — because our address base covers only Варна. gap=0. So they're outside our scope.

  Task 5: gate checks. Straightforward.

  Also check imot_bg_varna_areas_08.09.json (95 areas, total 93.1 km²) and K36_previous.md and mirela_names.json quickly. Also signed60_props.json for codes (chaika_kk/chaika_kv codes) and relationships.

  Let me read signed60_props.json and mirela_names.json and imot_bg_varna_areas_08.09.json, and skim K36_previous.md.

• Сега останалите три файла и сутрешната съпоставка.

• Now K36_previous.md — skim quickly for the morning's mapping (aliases). Let me grep for key alias mentions rather than reading all 35KB.

• Последно — сутрешната съпоставка К36 за алиасите.

• I have enough. A few more data checks worth doing quickly:

  1. For task 4 compute sums precisely.
  2. Check internal inconsistency between row pct fields and overlaps arrays for Левски 1/2, Център — flag as data quality issue for the gate (К37-?). Let me verify quickly across rows whether row pct_imot_in_ours equals max overlaps pct_of_imot.

• Една последна проверка — вътрешна съгласуваност на числата в таблицата.--- несъответствия ред vs overlaps ---
Виница: ред 63.8/99.5 vs overlaps 63.1/99.6
к.к. Златни пясъци: ред 82.8/83.9 vs overlaps 81.3/83.7
Западна промишлена зона: ред 72.0/86.1 vs overlaps 69.8/85.7
Трошево: ред 83.5/70.1 vs overlaps 79.8/69.2
Аспарухово: ред 96.3/64.4 vs overlaps 87.9/62.3
м-т Добрева чешма: ред 87.9/92.7 vs overlaps 87.9/75.1
Възраждане 1: ред 98.2/87.3 vs overlaps 97.5/87.3
Изгрев: ред 99.9/75.9 vs overlaps 99.2/91.6
к.к. Св.Св. Константин и Елена: ред 95.9/71.7 vs overlaps 76.1/66.8
в.з.Виница - север: ред 0.0/0.0 vs overlaps 95.6/16.5
Левски 1: ред 96.0/24.6 vs overlaps 96.0/35.0
Владислав Варненчик 1: ред 96.5/24.3 vs overlaps 94.3/32.0
Левски 2: ред 99.4/33.0 vs overlaps 99.3/46.8
Център: ред 56.6/51.3 vs overlaps 80.9/35.9
м-т Манастирски рид: ред 48.3/94.1 vs overlaps 45.4/96.4
--- Левски покритие ---
Левски 1 0.524 [{'pct_of_imot': 96.0, 'pct_of_ours': 35.0, 'ours': 'кв. Левски', 'src': 'подписан'}]
Левски 2 0.678 [{'pct_of_imot': 99.3, 'pct_of_ours': 46.8, 'ours': 'кв. Левски', 'src': 'подписан'}]
Базар Левски 0.169 [{'pct_of_imot': 97.4, 'pct_of_ours': 11.5, 'ours': 'кв. Левски', 'src': 'подписан'}]
Завод Дружба 0.3 [{'pct_of_imot': 11.3, 'pct_of_ours': 2.4, 'ours': 'кв. Левски', 'src': 'подписан'}]
Цветен квартал 0.613 [{'pct_of_imot': 3.8, 'pct_of_ours': 1.6, 'ours': 'кв. Левски', 'src': 'подписан'}]
--- Владиславово ---
Владислав Варненчик 1 0.833 [('кв. Владиславово', 32.0)]
Владислав Варненчик 2 0.982 [('кв. Владиславово', 39.6)]
м-т Боклук Тарла 0.444 [('кв. Владиславово', 17.9), ('кв. Кайсиева градина', 0.4)]
м-т Атанас Тарла 0.614 [('кв. Владиславово', 6.7)]
Метро 0.41 [('кв. Владиславово', 0.0)]
Кайсиева градина 0.48 [('кв. Кайсиева градина', 99.6), ('кв. Владиславово', 2.3)]
--- Възраждане ---
Възраждане 1 0.455 [('ж.к. Възраждане 1', 97.5, 87.3), ('ж.к. Младост 1', 1.1, 1.0), ('ж.к. Възраждане', 0.5, 6.9), ('ж.к. Младост', 0.0, 0.0)]
Възраждане 2 0.415 [('ж.к. Възраждане 2', 96.9, 99.8), ('ж.к. Възраждане', 1.7, 21.9), ('ж.к. Възраждане 1', 1.1, 0.9), ('ж.к. Младост', 0.0, 0.1), ('ж.к. Младост 2', 0.0, 0.0)]
Възраждане 3 0.209 [('ж.к. Възраждане 3', 92.2, 100.0), ('ж.к. Възраждане', 5.0, 32.9), ('с.о. Пчелина', 0.1, 0.0), ('ж.к. Младост', 0.0, 0.0)]
Възраждане 4 0.129 [('ж.к. Възраждане 4', 92.5, 72.6), ('ж.к. Възраждане', 3.8, 15.6)]
обща площ 95-те: 93.1


• Now I have everything. Compose the ≤800-word answer in Bulgarian with verdict ГОДНО/НЕГОДНО and checks К37-1…. Cite paths relative to kimi_raioni root: `raioni_table_08.09.json`, etc.

  Verdict: the data are ГОДНИ условно? The task says "Присъда ГОДНО/НЕГОДНО с К37-1…" — i.e., give verdict with numbered checks. The dataset has two alias bugs (к.к. Чайка, Вл. Варненчик 2) plus row-vs-overlaps inconsistencies → the table as-is is not fully trustworthy, but fixable. I'd say: ГОДНО с условия — or since verdict must be binary: the imot layer itself is ГОДНО; the matching table has 2 wrong aliases and pct inconsistencies → verdict on the table: НЕГОДНО без поправки? The question is "гейт за приемане на външен плочков слой" — the присъда likely refers to the К37 analysis/data. I'll rule: полигоните на imot — ГОДНО за приемане като справочен слой; raioni_table_08.09.json — НЕГОДНО в текущия вид (2 грешни алиаса + несъответстващи %-ове), годно след К37-1 поправки. Overall: ГОДНО условно. Let me structure with К37-1…К37-6 checks.

  Word limit 800. Structure:

  (1) Алиаси: wrong ones:
  - к.к. Чайка→кв. Чайка ГРЕШНО: overlaps 98.3% ⊂ нашия к.к. Чайка (81.8% покритие) → вярна двойка k-k-chayka→chaika_kk; голото „Чайка"→chaika_kv (IoU 0.88) е вярно. При нас chaika_kk=курорт, chaika_kv=квартал — същото деление като imot.
  - Вл. Варненчик 2→Кайсиева ГРЕШНО: 99.2% ⊂ кв. Владиславово (39.6%); Кайсиева има собствен ред (IoU 0.87, mirela 0.94). Вярно: vv1 и vv2 → подрайони на vladislavovo; mirela също има „Владислав Варненчик 2" и „Владиславово" отделно, iou_m=0.92.
  - в.з.Виница-север→Добрева чешма: геометрически вярно (95.6% ⊂ dobreva), но verdict-ът „същото име, различно чертане" е грешен — това е нов подрайон; нямаме клетка Виница-север.
  - Операта/Стадион Спартак/Общината: нашите са ориентири-сгради (0.002–0.022 km²) → не са съпоставими; imot очертава микрорайон.
  - Верните: Погреби→pogrebite, Окр. болница→generalite, Планова ПЗ→pz_planova вярно (0.83+0.83 mirela), Левски1/2→kv_levski като родител вярно. Метро→pz_metro: в partition_v2_props.json няма pz_metro (само в registry от K36) — таблицата правилно го отчита като дупка (99.9% not_in_ours, mirela 0.93) → да се добави pz_metro.

  (2) Правило: R1: iou_m≥0.7 & iou_ours<0.6 → нашият под въпрос; R2: iou_m≤0.4 & нашият подписан → imot е по-вероятно грешен; R3: нашият е ориентир/сграда → imot по дефиниция; R4: imot ⊂ нашия ≥90% и покрива <50% → imot е подрайон, не конкурент; R5: нашият „предложен" (неподписан) vs imot с mirela потвърждение → imot.

  Apply:
  - Под въпрос наши: Акчелар (m 0.75), Сотира (m 0.75) → преначертай нашите; Стадион Спартак (m 0.80, R3+R5) → imot; Операта (m 0.84, R3) → imot като микрорайон ⊂ Център; Център: нашият е „предложен (разширен)", imot по-тесен + 5 микрорайона в дупката (ЖП Гара, ХЕИ, Поща, Операта, Бизнес хотел с m 0.78–0.85) → imot-версията + деца по-надеждна (R5); Окр. болница-Генерали: ours_in=100%, нашият е 4-точков Wikimapia правоъгълник 0.151 vs imot 0.272 и Петър „сбъркан" → imot (R5).
  - Нашите ок, imot раздут/орязан: Максуда (m 0.14, imot 61.7% в Св. Ив. Рилски), Фичоза (m 0.25), Горна Трака (imot поглъща 4 подписани клетки: Евксиноград 29.6%, Фатрико дере 26.5%, Средна Трака 19.4%, Горна Трака 15%), Манастирски рид (imot 4.09 vs наш 1.93 km², без mirela), Евксиноград (m 0.0), Победа (m 0.36; imot е по-малък + Конфуто/Гранд Мол отделно), Салтанат (без mirela, пресича), Погреби (m 0.51 — под прага; и двете слаби, нашето неподписано → нерешено, леко към imot).
  - Левски 1/2, ВВ 1/2 → R4 подрайони, не конкуренти.

  (3) 34-те нови: compact table. Group. With родител where ⊂.

  (4) Левски: 35.0+46.8+11.5 = 93.3% + Цветен 1.6 + Завод 2.4 ≈ 97% покритие на kv_levski; остава ~3%. But note imot Завод Дружба само 11.3% в Левски. Децата не се застъпват (0 двойки). So imot Левски1+2+Базар покриват ~93% от нашия kv_levski; остатък ~3–7% (вероятно ивицата към Център/Спортна зала). Възраждане: децата покриват Възр1 87.3%, Възр2 99.8%, Възр3 100%, Възр4 72.6% (+родител ж.к. Възраждане 70% сумарно) — почти изцяло, липсва ~27% от Възр4 (към м-т Планова, която е 25.2% от Възр4). Владиславово: ВВ1 32.0 + ВВ2 39.6 + Боклук Тарла 17.9 = 89.5% + Кайсиева 2.3 ≈ 92%; остатък ~8–10% (Атанас Тарла 6.7% → ~98%). Метро не е във Владиславово (0.0).

  (5) Гейт К37-G checks.

  Verdicts К37-1..: 
  - К37-1 алиаси: 2 грешни от 9 → поправими.
  - К37-2: правило и класификация.
  - К37-3: 34 нови — приеми 27, обекти 5, села извън обхват 6...? Let me count: села+в.з.: с. Звездица, с. Казашко, с. Каменар, с. Константиново, с. Тополи, в.з.Звездица, м-т Крушките, Орехчето, Припек, Лазур — 10 с 0 сгради в нашата база → извън градския адресен обхват; отложи. Hmm Лазур: K36 says near Чайка/Траката. buildings=0 notin=100 → outside our cells. Since our address base covers the city, 0 buildings means empty/outside. Отбележи.
  - К37-4 родителски суми ок.
  - К37-5 вътрешна консистентност: редови pct vs overlaps разминавания в 15 реда (Център 56.6/51.3 vs 80.9/35.9!) → таблицата да се регенерира преди употреба. That's why verdict on table НЕГОДНО as-is.
  - Overall: imot слой ГОДНО (95 полигона, 0 застъпвания, 93.1 km², площите съвпадат със сумата), таблицата НЕГОДНО без регенерация.

  Districts for task 3 table: use K36: Звездица/Казашко→mladost? K36 line 107: „Звездица и Казашко → район Младост; Константиново → Владислав Варненчик; Тополи → Аспарухово; Каменар → Аспарухово". I'll cite that.

  Build the 34-row table compactly: name | код | вид | район | родител/бележка. Keep tiny.

  Classes "обект": Гранд Мол, Бизнес хотел, Летище, Пристанище Варна, Бизнес парк Варна → вид „обект".

  Districts (община): Одесос: Гръцка махала, Фестивален, ВИНС-Червен площад, Чаталджа, ЖП Гара, Пристанище, Централна поща, Операта (вече ориентир), ХЕИ?, Бизнес хотел, Лятно кино? Тракия is odesos: Зимно кино Тракия, Лятно кино Тракия → odesos. ХЕИ: пресича Център/Левски → odesos/primorski — each overlaps: ХЕИ 48.9% Център + 8.6% Левски → odesos. Бизнес хотел: Център/Колхозен/Погребите → odesos. Автогара: Рилски/Ботев → mladost/odesos; K36 said mladost. Гранд Мол: Победа → mladost. Конфуто → mladost. Метро → vladislav_varnenchik. Атанас Тарла, Боклук Тарла → vladislav_varnenchik. м-т Планова → vladislav_varnenchik. ПЗ Тополи → mladost (ЗПЗ). Бизнес парк → mladost (ЗПЗ). Летище → mladost? Airport is in район Младост? Varna airport is in район Приморски? Hmm — Летище Варна is in район Младост? Actually airport is northwest, municipality район... Aksakovo? Varna Airport is on territory of район Младост? I believe it's in община Аксаково/район... Don't assert strongly: „mladost/извън мрежата". K36 said „Летището е извън градската мрежа". I'll mark mladost (по съседство със ЗПЗ) с бележка. Базар Левски, к.к. Слънчев ден, Франга Дере → primorski. ВИНС, Чаталджа, ЖП Гара, Пристанище, Поща → odesos.

  Parents: Гръцка махала ⊂ grackata_mahala (97.5%) — parent; Фестивален ⊂ grackata_mahala; Конфуто ⊂ pobeda; Слънчев ден ⊂ kk_konstantin_elena; Боклук Тарла ⊂ vladislavovo; Базар Левски ⊂ kv_levski; Зимно кино ⊂ trakia; Франга Дере ⊂ kokardzha_generic (79%); Чаталджа — частично Център 26.5% → parent tsentar? It's a gap-filler; родител: няма (граничи с Център). Лятно кино Тракия пресича trakia+tsentar → без единен родител. Автогара пресича rilski+botev. Бизнес хотел пресича tsentar/kolhozen/pogrebite. ПЗ Тополи ⊂ zpz 53.4%→ parent zpz (46.6% извън — не е чисто дете). Метро — няма родител у нас (дупка; mirela го има). Атанас Тарла — съсед на vladislavovo (26.9%). м-т Планова — съсед на pz_planova/Възр4.

  Word budget ~800. Need compactness. Use tables sparingly — a 34-row table is heavy but required. Make columns minimal.

  Write the answer now. Count words roughly; Bulgarian words. Aim ~780.

• # К37 · imot.bg (95) срещу нашите — анализ

  Източници: `raioni_table_08.09.json`, `partition_v2_props.json`, `signed60_props.json`, `imot_bg_varna_areas_08.09.json`, `mirela_names.json`, `K36_previous.md`.

  ## (1) Алиаси име→име

  **Грешни (2):**
  - **к.к. Чайка → кв. Чайка** — грешно. В `overlaps`: imot „к.к. Чайка" е 98,3% в нашия **к.к. Чайка** (`chaika_kk`), покривайки 81,8% от него. Значи при imot „Чайка"=кварталът, „к.к. Чайка"=курортът — същото деление като нашето `chaika_kv`/`chaika_kk` (потвърждава coord_rule от К36). Вярно: `k-k-chayka→chaika_kk` (IoU≈0,79), `chayka→chaika_kv` (0,88 — вече е вярно).
  - **Владислав Варненчик 2 → Кайсиева градина** — грешно. 99,2% от imot-полигона е в **кв. Владиславово** (39,6% от него), а Кайсиева има собствен imot-ред (IoU 0,87, mirela 0,94). Вярно: `vladislav-varnenchik-1` и `-2` → подрайони на `vladislavovo` (mirela също ги дели така; iou_m=0,92).

  **Преквалифициране, не грешка:** в.з.Виница-север лежи 95,6% в `dobreva` — нямаме клетка „Виница-север", така че това е *нов подрайон на Добрева чешма*, не „същото име, друго чертане". Операта/Стадион Спартак: нашите са ориентири-сгради (0,002/0,022 km²) — несравними с imot-микрорайоните. Метро→pz_metro: `pz_metro` липсва в `partition_v2_props.json` (само в регистъра от К36) — таблицата правилно отчита дупка (99,9% not_in_ours, mirela 0,93). Верни: Погреби→pogrebite, Окр.болница→generalite, Планова ПЗ→pz_planova (0,83/0,83), Левски 1/2→kv_levski.

  ## (2) Двадесетте „различно чертане" — правило

  R1: iou_m ≥ 0,7 и IoU_наш < 0,6 → нашият е под въпрос. R2: iou_m ≤ 0,4 и нашият е подписан → imot е раздут/орязан. R3: нашият е ориентир-сграда → imot дефинирай районa. R4: imot ⊂ нашия ≥90% с покритие <50% → подрайон, не конкурент. R5: нашият е „предложен" (неподписан) + mirela подкрепя imot → imot.

  - **Преначертае нашите (R1/R5):** Акчелар (m 0,75), Сотира (m 0,75); Стадион Спартак (m 0,80, R3); Операта (m 0,84, R3 → микрорайон ⊂ Център); Окр.болница-Генерали (нашият 0,151 km² е 100% в imot и Петър „сбъркан"; R5); Център — нашият е неподписан „разширен", а imot-корът + 5 потвърдени микрорайона в дупката (ЖП Гара, ХЕИ, Поща, Операта, Бизнес хотел — m 0,78–0,85) е по-надеждната схема.
  - **Нашите стоят, imot е сбъркан (R2):** Максуда (m 0,14; 61,7% от imot е в Св. Ив. Рилски), Фичоза (0,25), Евксиноград (0,0), Победа (0,36), Горна Трака (imot поглъща 4 подписани клетки), Манастирски рид (imot 4,09 vs наш 1,93 km², без mirela), Салтанат (без mirela).
  - **Нерешено:** Погреби (m 0,51 — под прага; и двете слаби; леко към imot).
  - **Подрайони (R4):** Левски 1/2, Вл.Варненчик 1/2.

  ## (3) 34-те нови района

  | име | код | вид | район | родител/бел. |
  |---|---|---|---|---|
  | Гръцка махала | gratska_mahala_m | район | odesos | ⊂ grackata_mahala |
  | Фестивален комплекс | festivalen_kompleks | зона | odesos | ⊂ grackata_mahala |
  | Конфуто | konfuto | район | mladost | ⊂ pobeda |
  | к.к. Слънчев ден | slanchev_den | кк | primorski | ⊂ kk_konstantin_elena |
  | м-т Боклук Тарла | bokluk_tarla | м-т | vladislav_varnenchik | ⊂ vladislavovo |
  | Базар Левски | bazar_levski | зона | primorski | ⊂ kv_levski |
  | Зимно кино Тракия | zimno_kino_trakiya | зона | odesos | ⊂ trakia |
  | м-т Франга Дере | franga_dere | м-т | primorski | ⊂ kokardzha_generic |
  | Чаталджа | chataldzha | район | odesos | дупка, съсед tsentar |
  | ВИНС-Червен площад | vins_cherven_ploshtad | район | odesos | дупка |
  | ЖП Гара | zhp_gara | зона | odesos | дупка |
  | Лятно кино Тракия | lyatno_kino_trakiya | зона | odesos | пресича trakia+tsentar |
  | ХЕИ | hei | район | odesos | пресича tsentar+kv_levski |
  | Автогара | avtogara | зона | mladost | пресича rilski+botev |
  | Централна поща | tsentralna_poshta | зона | odesos | ⊂ tsentar |
  | Гранд Мол | grand_mol | **обект** | mladost | дупка при pobeda |
  | Бизнес хотел | biznes_hotel | **обект** | odesos | пресича 3 клетки |
  | Летище | letishte | **обект** | mladost | извън мрежата |
  | Пристанище Варна | pristanishte_varna | **обект** | odesos | дупка (353 сгради) |
  | Бизнес парк Варна | biznes_park_varna | **обект** | mladost | ⊂ zpz (42%) |
  | Промишлена зона Тополи | pz_topoli | зона | mladost | ⊂ zpz (53%) |
  | Метро | pz_metro | зона | vladislav_varnenchik | дупка, mirela 0,93 |
  | м-т Планова | mt_planova | м-т | vladislav_varnenchik | съсед pz_planova |
  | м-т Атанас Тарла | atanas_tarla | м-т | vladislav_varnenchik | съсед vladislavovo |
  | с. Звездица / в.з.Звездица | zvezditsa / vz_zvezditsa | с. | mladost | извън адр. обхват |
  | с. Казашко | kazashko | с. | mladost | извън обхват |
  | с. Каменар | kamenar | с. | asparuhovo (?) | извън обхват |
  | с. Константиново | konstantinovo | с. | vladislav_varnenchik | извън обхват |
  | с. Тополи | topoli | с. | asparuhovo | извън обхват |
  | м-т Крушките, Орехчето, Припек, Лазур | krushkite, orehcheto, pripek, lazur | м-т | — | 0 сгради, отложи |

  ## (4) Покриват ли децата родителите

  Да, почти изцяло (взаимни застъпвания: 0). **кв. Левски**: Левски 1 (35,0%) + Левски 2 (46,8%) + Базар Левски (11,5%) = 93,3%; +Цветен 1,6% +Завод Дружба 2,4% ≈ 97%; остават ~3% (ивица към Център/Спортна зала). **Възраждане 1–4**: 87,3/99,8/100/72,6% + 70% от остатъка `vazrazhdane`; липсата във Възр4 е м-т Планова (25,2% от клетката). **Владиславово**: ВВ1 32,0 + ВВ2 39,6 + Боклук Тарла 17,9 = 89,5% (+Кайсиева 2,3, Атанас Тарла 6,7) ≈ 98%.

  ## (5) Гейт за външен плочков слой

  G1 хеш на снапшота (95 slug-а, дата, SHA-256) — отхвърли тихи промени. G2 Σ площи = площ на обединението ±0,1% (тук 93,1 km² потвърдена) и 0 двойки застъпване >1% (`raioni_imot_overlaps_08.09.json`: 0). G3 всяка наша сграда ∈ точно един imot-полигон (вътре в общия им обхват). G4 имена 1:1 с речник, нормализирани (к.к./кв./м-т префиксите НЕ се режат — това счупи Чайка). G5 вътрешна консистентност: ред ↔ overlaps; **тук гърми** — 15 реда с разминавания (Център: 56,6/51,3 vs 80,9/35,9; К.и Елена: 95,9 vs 76,1).

  **Присъда: ГОДНО условно.** К37-1 алиаси: 2 грешни, поправими по `overlaps` ✔. К37-2 правило R1–R5 приложимо ✔. К37-3 нови: 24 приемай, 5 обекта, 10 извън обхвата отложи ✔. К37-4 родителски суми ≈ покрити ✔. К37-5 самата `raioni_table_08.09.json` — НЕГОДНА без регенерация (К37-5 несъответствия); след фикс на К37-1+К37-5 слоят е годен за плочки.

To resume this session: kimi -r session_c977572d-906d-4b69-b505-98aab115745e

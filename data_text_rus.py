#!/usr/bin/env python3
# -*- coding: utf-8 -*-


###############################################################################
# LevelGenerator text data
RUS_ROOM_TEXTS = [
                  ['                     W', 'Используй A S D', 'чтобы двигаться.',
                   ' Используй мышь чтобы', 'целиться, держи левую', 'кнопку мыши чтобы',
                   'стрелять.', 'Попытайся выйти из', 'этого пузыря...'],

                  ['Ты перешел в', 'новое бульбополе!',
                   'Уничтожь врагов', 'бульбо-танков',
                   'чтобы забрать у', 'них бульбы и', 'ВЫРАСТИ!'],

                  ['Получение урона от', 'вражеских танков ',
                   'будет делать твой', 'танк слабее.', 'Если ты повержен,',
                   'ты перенесешься в', 'ближайшее', 'безопасное', 'бульбополе.'],

                  ['Иногда самый лучший', ' способ это', 'просто убежать!', '', '', '',
                   '', 'Нажми "p" для паузы'],

                  ['Чем дальше ты', 'уйдешь от', 'начального',
                   'бульбополя, тем', 'сложнее будут', 'враги!',
                   'Поэтому будь', 'осторожен и...', 'УДАЧИ!'],

                  ['Теперь тебе доступно', 'еще одно умение!',
                   'Чтобы активировать', 'это умение,', 'нажми "ПРОБЕЛ"']]
###############################################################################
# StartMenu text data
RUS_START_MENU_CAPTION = 'Подводные битвы'
RUS_PLAY_LABEL = 'ИГРАТЬ'
###############################################################################
# PauseMenu text data
RUS_STATSWINDOW_CAPTIONS = ['Статистика', 'Основное оружие', 'Второе оружие']
RUS_MAPWINDOW_CAPTION = 'Карта'
RUS_OPTIONSWINDOW_CAPTION = 'Опции'
RUS_OPTIONSWINDOW_LABEL_1 = 'Музыка'
RUS_OPTIONSWINDOW_LABEL_2 = 'Звук'
RUS_OPTIONSWINDOW_BUTTONS_TEXTS = ['ВКЛ.', 'ВЫКЛ.', 'В МЕНЮ']
RUS_PAUSEMENU_CAPTION = 'ПАУЗА'
RUS_STATSBUTTON_NAME = 'Статистика'
RUS_MAPBUTTON_NAME = 'Карта'
RUS_OPTIONSBUTTON_NAME = 'Опции'
###############################################################################
# UpgradeMenu text data
upg_text_00 = 'Базовый танк', ['Базовая пушка'], ['Нет'], ['Это твой стартовый танк.'],\
              ['Стреляет обычными бульбами.'], ['-']

upg_text_10 = 'Охотник #1', ['Пулемет'], ['Нет'], \
              ['Маленький, быстрый и', 'маневренный танк', 'с высокой', 'скорострельностью.'],\
              ['Стреляет обычными бульбами', 'с высокой скоростью.'], ['-']

upg_text_11 = 'Сбалансированный #1', ['2 параллельных', 'выстрела'], ['Нет'], \
              ['Баланс между скоростью и', 'прочностью.'], \
              ['Стреляет 2 бульбами, идущими', 'рядом друг с другом.'], ['-']

upg_text_12 = 'Тяжелый #1', ['Тяжелая пушка'], ['Нет'], \
              ['Немного медленный и', 'менее маневренный, но', 'наносит более мощные', 'удары.'],\
              ['Стреляет обычными,', 'тяжелыми бульбами, которые', 'наносят ощутимый урон.'], ['-']

upg_text_20 = 'Охотник #2', ['3 бульбы в разброс'], ['Броня'], \
              ['Улучшенная версия охотника,', 'его особенности - это', 'скорость и маневренность.'],\
              ['Стреляет 3 бульбами', 'в разброс.'],\
              ['Броня может быть вызвана в', 'виде быстрой вспышки, чтобы', 'защитить тебя от всяческих', 'повреждений.']

upg_text_21 = 'Сбалансир. Охотник #1', ['3 параллельных', 'выстрела'], ['Броня'], \
              ['У сбалансированного танка', 'немного больше скорости', 'и маневренности.'],\
              ['Стреляет 3 бульбами, идущими', 'рядом друг с другом.'], \
              ['Броня может быть вызвана в', 'в виде быстрой вспышки, чтобы',
               'защитить тебя от всяческих', 'повреждений.']

upg_text_22 = 'Сбалансир. Тяжелый #1', ['3 параллельных', 'выстрела'], ['Мины'], \
              ['У сбалансированного танка', 'немного тяжелее', 'вооружение, но легче,', 'чем у Тяжелого Танка.'],\
              ['Стреляет 3 бульбами, идущими', 'рядом друг с другом.'],\
              ['Мины могут быть установлены', 'и принесут большой урон, когда', 'враг пройдет по ним.']

upg_text_23 = 'Тяжелый #2', ['5 параллельных', 'выстрелов'], ['Мины'], \
              ['Большой и медленный танк,', 'но хорошо вооружен.'], ['Стреляет обычными бульбами.'], ['-']

upg_text_30 = 'Снайпер #1', ['Проникающий', 'выстрел'], ['Телепорт'], \
              ['Шустрый охотник, который', 'стреляет обычными,', 'мощными пузырями.'],\
              ['Проникающий выстрел долго', 'перезаряжается, но наносит',
               'огромный урон и проходит', 'сквозь нескольких противников.'],\
              ['Нажатие пробела мгновенно', 'телепортирует тебя туда, где', 'находится курсор мыши.']

upg_text_31 = 'Охотник #3', ['Улучшенный пулемет'], ['Самонаводящиеся', 'снаряды'], \
              ['3-е поколение охотников.', 'Сфокусировано на', 'скорости и маневренности.'],\
              ['Улучшенный пулемет с очень', 'высокой скорострельностью',
               'и наносит больший урон,', 'чем обычный пулемет.'],\
              ['Запусти 2 пузыре-ракеты,', 'которые разыщут и последуют', 'за твоими врагами.']

upg_text_32 = 'Сбалансир. Охотник #2', ['5 бульб в разброс'], ['Выстрел оглушающим', 'взрывом'], \
              ['У сбалансированного танка', 'немного больше скорости и', 'маневренности.'],\
              ['Стреляет 5 бульбами', 'в разброс.'],\
              ['Импульс исходит из танка,', 'который застрял в окружении',
               'врагов, и оглушает их', 'на некоторое время.']

upg_text_33 = 'Сбалансир. Тяжелый #2', ['5 бульб в разброс'], ['Территориальный взрыв'], \
              ['У сбалансированного танка', 'немного легче', 'вооружение, но легче,', 'чем у Тяжелого танка.'],\
              ['Стреляет 5 бульбами', 'в разброс.'],\
              ['Взрыв исходит из танка и', 'поражает всех окружающих', 'врагов.']

upg_text_34 = 'Тяжелый #3', ['2 больших пушки'], ['Липкая пушка'], \
              ['Большой и медленный танк,', 'который может гордиться', 'мощным оружием и грубой', 'силой.'],\
              ['Стреляет 2 большими', 'пузырями одновременно.'],\
              ['Нажатие пробела запускает', 'липкие пузыри, которые', 'сделают цель неподвижной.']

upg_text_35 = 'БЗТ #1', ['1 Б. Пушка, 2 М. авто'], ['Самонаводящиеся', 'снаряды'], \
              ['Очень большой и', 'медленный танк, который', 'ищет врагов, чтобы', 'уничтожить их.'], \
              ['Ты управляешь большой', 'пушкой, пока 2 маленькие',
               'пушки будут искать врагов', 'и стрелять автоматически.'],\
              ['Запусти 4 пузыре-ракеты,', 'которые разыщут и последуют', 'за твоими врагами.']

upg_text_40 = 'Снайпер #2', ['Мощный проникающий', 'выстрел'], ['Улучшенный телепорт'], \
              ['Шустрый охотник, который', 'стреляет обычными,', 'мощными пузырями.'],\
              ['Проникающий выстрел долго', 'перезаряжается, но наносит',
               'огромный урон и проходит', 'сквозь нескольких противников.'],\
              ['Нажатие пробела мгновенно', 'телепортирует тебя туда, где', 'находится курсор мыши.']

upg_text_41 = 'Охотник #4', ['2-х стрельный пулемет'], ['Пушка "взрыв-звезда"'], \
              ['Маленький, быстрый и', 'маневренный танк', 'с высокой', 'скорострельностью.'],\
              ['2 маленьких пузыря, идущих', 'рядом друг с другом в быстрой', 'последовательности.'],\
              ['Cтреляет снарядом, который', 'взрывается через некоторое',
               'время и разбрасывает', 'осколки на 360 градусов.']

upg_text_42 = 'Сбалансир. Охотник #3', ['2 М., 1 Б. Пушка'], ['Самонаводящиеся', 'снаряды'], \
              ['Танк среднего размера.', 'Быстрый и мощный.'],\
              ['Стреляют 2 маленькие', 'пушки и 1 большая пушка', 'одновременно.'],\
              ['Запусти 3 пузыре-ракеты,', 'которые разыщут и последуют', 'за твоими врагами.']

upg_text_43 = 'Сбалансир. Тяжелый #3', ['2 больших пулемета'], ['Территориальный взрыв'], \
              ['У сбалансированного танка', 'немного легче', 'вооружение, но легче,', 'чем у Тяжелого танка.'],\
              ['Стреляют 2 большие пушки', 'с высокой скоростью.'],\
              ['Выстреливает большим', 'пузырем, который взрывается',
               'от контакта с врагом,', 'повреждая окружающих.']

upg_text_44 = 'Тяжелый #4', ['2 Б. пушки, 2 М. авто'], ['Липкий взрыв'], \
              ['Большой и медленный танк,', 'который может гордиться', 'мощным оружием и грубой', 'силой.'],\
              ['Ты управляешь 2 большими', 'пушками, пока 2 маленькие',
               'будут искать врагов и', 'стрелять автоматически.'],\
              ['Много липких пузырей', 'запускаются из танка в',
               'разные стороны и делают', 'врагов неподвижными.']

upg_text_45 = 'БЗТ #2', ['2 Б. пушки, 3 М. авто'], ['Большой оглушающий взрыв'], \
              ['Очень большой и', 'медленный танк, который', 'оглушает и убивает.'],\
              ['Стреляет обычными бульбами.'], ['-']

upg_text_50 = 'Снайпер-призрак', ['Взрывающийся ', 'проникающий выстрел'], ['Разобраться'], \
              ['Очень быстрый и проворный танк,', 'который может разбиться на части и', 'собраться обратно.'],\
              ['Долгая перезарядка, но очень', 'сильный урон, взрывается при',
               'контакте и может пройти', 'сквозь несколько целей.'],\
              ['Держи пробел, чтобы танк', 'разбился на части, став',
               'непобедимым, но тогда', 'теряется возможность стрелять.']

upg_text_51 = 'Супер Охотник', ['3 пулемета'], ['Орбитальные', 'самонаводящиеся снаряды'], \
              ['Маленький и проворный', 'танк, который имеет',
               'высокую скорострельность и', 'самонаводящиеся снаряды.'],\
              ['3 маленьких пузыря, идущих', 'рядом друг с другом в быстрой', 'последовательности.'],\
              ['Сюрикены автоматически', 'появляются и окружают тебя.',
               'Они покинут тебя и повредят', 'врагов, которые подошли.']

upg_text_52 = 'Танк вампир', ['Высасывающие пузыри'], ['Пузыри-вирусы'], \
              ['Этот танк высасывает', 'жизнь из врагов и может', 'заразить их вирусом.'],\
              ['Стреляет обычными бульбами.'], ['-']

upg_text_53 = 'Танк-трутень', ['Митозные', 'самонаводяшки'], ['Конвертация трутней'], \
              ['Этот танк - мастер', 'самонаводящихся снарядов.'], ['Стреляет обычными бульбами.'], ['-']

upg_text_54 = 'Супер Тяжелый', ['2 В. П, 6 М. А, 1 БП'], ['Огромная пушка'], \
              ['Здоровенный монстр', 'бульботанк.'], ['Стреляет обычными бульбами.'], ['-']

upg_text_55 = 'БЗТ перевозчик', ['1 Б. П, 4 М. А, 1 БП'], ['Вызвать союзников'], \
              ['Гигантский танк, который выпускает', 'толпу охотников.'], ['Стреляет обычными бульбами.'], ['-']

RUS_UPGRADE_TEXT = {(0, 0): upg_text_00,
                    (1, 0): upg_text_10,
                    (1, 1): upg_text_11,
                    (1, 2): upg_text_12,
                    (2, 0): upg_text_20,
                    (2, 1): upg_text_21,
                    (2, 2): upg_text_22,
                    (2, 3): upg_text_23,
                    (3, 0): upg_text_30,
                    (3, 1): upg_text_31,
                    (3, 2): upg_text_32,
                    (3, 3): upg_text_33,
                    (3, 4): upg_text_34,
                    (3, 5): upg_text_35,
                    (4, 0): upg_text_40,
                    (4, 1): upg_text_41,
                    (4, 2): upg_text_42,
                    (4, 3): upg_text_43,
                    (4, 4): upg_text_44,
                    (4, 5): upg_text_45,
                    (5, 0): upg_text_50,
                    (5, 1): upg_text_51,
                    (5, 2): upg_text_52,
                    (5, 3): upg_text_53,
                    (5, 4): upg_text_54,
                    (5, 5): upg_text_55}

RUS_UPGRADEMENU_LABELS = ['Улучшение!', '- Основное оружие -', '- Второе оружие -']
RUS_UPGRADEMENU_CAPTION = 'Выбирай улучшение...'
###############################################################################
# VictoryMenu text data
RUS_VICTORYMENU_CAPTION = 'ПОЗДРАВЛЯЕМ!'
RUS_VICTORYMENU_TEXT = 'Ты прошел игру!'
RUS_VICTORYMENU_BUTTON = 'Назад в меню'
###############################################################################
# CooldownWindow text data
RUS_WINDOW_COOLDOWN_LABELS = ['О:', 'В']
###############################################################################
# HealthWindow text data
RUS_TANK_NAMES = {(0, 0): 'Базовый танк',
                  (1, 0): 'Охотник #1',
                  (1, 1): 'Сбалансированный',
                  (1, 2): 'Тяжелый #2',
                  (2, 0): 'Охотник #2',
                  (2, 1): 'Сбалансир. Охотник #1',
                  (2, 2): 'Сбалансир. Тяжелый #1',
                  (2, 3): 'Тяжелый #2',
                  (3, 0): 'Снайпер #1',
                  (3, 1): 'Охотник #3',
                  (3, 2): 'Сбалансир. Охотник #2',
                  (3, 3): 'Сбалансир. Тяжелый #2',
                  (3, 4): 'Тяжелый #3',
                  (3, 5): 'БЗТ #1',
                  (4, 0): 'Снайпер #2',
                  (4, 1): 'Охотник #4',
                  (4, 2): 'Сбалансир. Охотник #3',
                  (4, 3): 'Сбалансир. Тяжелый #3',
                  (4, 4): 'Тяжелый #4',
                  (4, 5): 'БЗТ #2',
                  (5, 0): 'Снайпер-призрак',
                  (5, 1): 'Супер Охотник',
                  (5, 2): 'Танк вампир',
                  (5, 3): 'Танк-трутень',
                  (5, 4): 'Супер Тяжелый',
                  (5, 5): 'БЗТ перевозчик'}

RUS_BUBBLES_TEXTS = (' пузырей осталось', 'Максимальный танк')
###############################################################################

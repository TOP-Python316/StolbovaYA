1. Лысые злодеи 90х годов
    - Описание: Отобразите имя, первое появление, частота появления. Выведите только тех персонажей, у которых Bald и они злодеи. Год появления между 1990 и 1999
    - Выборка: Имя, год первого появления, количество появлений; где прическа — Bald, align — Bad Characters, и год первого появления между 1990 и 1999.
    - Количество строк: 94


SELECT
    name,
    FIRST_APPEARANCE,
    APPEARANCES
FROM MarvelCharacters
WHERE hair = 'Bald'
   AND  align  = 'Bad Characters'
   AND Year BETWEEN 1990 AND 1999;
# 7. Персонажи, появившиеся в определённое десятилетие
#     - Описание: Вывести имя и год первого появления. Найти персонажей, первое появление которых приходится на 1960-е годы.
#     - Выборка: Имя, год первого появления; где год первого появления между 1960 и 1969.
#     - Количество строк: 1306

SELECT
    name,
    FIRST_APPEARANCE
FROM MarvelCharacters
WHERE year BETWEEN 1960 AND 1969;
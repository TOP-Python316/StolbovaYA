# 15. Злодеи с нестандартными физическими характеристиками
#      - Описание: Вывести имя и описание пола. Найти злодеев, у которых пол не является стандартным (не Male, не Female).
#      - Выборка: Имя, описание пола; где align — Bad Characters и пол не Male и не Female.
#      - Количество строк: 20

SELECT
    name,
    sex
FROM MarvelCharacters
WHERE align = 'Bad Characters'
    AND sex NOT IN ('Male Characters','Female Characters');

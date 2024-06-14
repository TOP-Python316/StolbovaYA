# 4. Женские персонажи с редким цветом глаз
#     - Описание: Вывести имена и цвет глаз. Отфильтровать женских персонажей с цветом глаз Gold или Amber.
#     - Выборка: Имя, цвет глаз; где пол — женский и цвет глаз Gold или Amber.
#     - Количество строк: 5

SELECT
    name,
    eye
FROM MarvelCharacters
WHERE sex = 'Female Characters'
    AND eye in ('Gold Eyes','Amber Eyes')
ORDER BY name;
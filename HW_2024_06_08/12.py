# 12. Персонажи с самыми редкими цветами глаз
#      - Описание: Вывести имя и цвет глаз. Найти персонажей с цветом глаз Magenta, Pink, или Violet.
#      - Выборка: Имя, цвет глаз; где цвет глаз Magenta, Pink, или Violet.
#      - Количество строк: 34


SELECT
    name,
    eye
FROM MarvelCharacters
WHERE eye IN ('Magenta Eyes','Pink Eyes','Violet Eyes');
# 17. Название: Сравнение популярности персонажей по цвету волос и глаз
#      - Описание: Сравнение общего количества появлений персонажей в зависимости от комбинации цвета волос и глаз. Необходимо сгруппировать данные по этим двум признакам и подсчитать общее количество появлений для каждой комбинации.
#      - Выборка: Группировка по цвету волос и глаз, подсчет количества появлений для каждой комбинации. Используйте SUM для подсчета общего количества появлений.
#      - Количество строк: 196

SELECT  hair,
    eye ,
    SUM(Appearances) as Appearances
FROM MarvelCharacters
WHERE  hair IS NOT NULL
    AND eye IS NOT NULL
    AND appearances NOT NULL
GROUP BY hair, eye;
--Задание 1.

SELECT living_status.living_status AS status,
    COUNT(marvel_characters.id) AS count
FROM marvel_characters
INNER JOIN living_status ON marvel_characters.alive_id = living_status.id
GROUP BY living_status.living_status;


--Задание 2.

SELECT eye_color.eye_color AS eye_color,
    ROUND(AVG(marvel_characters.appearances), 0) AS avg_appearances
FROM marvel_characters
INNER JOIN eye_color ON marvel_characters.eye_id = eye_color.id
GROUP BY eye_color.eye_color;

--Задание 3.

SELECT hair_color.hair_color AS hair_color,
    MAX(marvel_characters.appearances) AS max_appearances
FROM marvel_characters
INNER JOIN hair_color ON marvel_characters.hair_id = hair_color.id
GROUP BY hair_color.hair_color;

--Задание 4

SELECT identify.identify AS identity,
    MIN(marvel_characters.appearances) AS min_appearances
FROM marvel_characters
INNER JOIN identify ON marvel_characters.identify_id = identify.id
GROUP BY identify.identify;

--Задание 5

SELECT sex.sex, count(marvel_characters.id) as quty_sex
FROM marvel_characters
INNER JOIN sex ON marvel_characters.sex_id = sex.id
GROUP BY sex.sex;


--Задание 6: Средний год первого появления персонажей с различным типом личности


SELECT identify.identify, AVG(year) as avg_year
FROM marvel_characters
INNER JOIN identify ON marvel_characters.identify_id = identify.id
GROUP BY identify.identify;

--Задание 7:

SELECT eye_color.eye_color, COUNT(marvel_characters.id) as count_color
FROM marvel_characters
INNER JOIN eye_color ON marvel_characters.eye_id = eye_color.id
INNER JOIN living_status ON marvel_characters.alive_id = living_status.id
    AND living_status.living_status = 'Living Characters'
GROUP BY eye_color.eye_color;


--Задание 8: Максимальное и минимальное количество появлений среди персонажей с определенным цветом волос


SELECT hair_color.color AS color,
    MAX(marvel_characters.appearances) AS max_appearances,
    MIN(marvel_characters.appearances) AS min_appearances
FROM marvel_characters
INNER JOIN hair_color ON marvel_characters.hair_id = hair_color.hair_id
GROUP BY hair_color.hair_id;

--Задание 9: Количество персонажей с различным типом личности среди умерших

SELECT identify.identify,
    COUNT(marvel_characters.id)
FROM marvel_characters
INNER JOIN identify ON marvel_characters.identify_id = identify.id
INNER JOIN living_status ON marvel_characters.alive_id = living_status.id
    AND living_status.living_status = 'Deceased Characters'
GROUP BY identify.identify;


--Задание 10: Средний год первого появления персонажей с различным цветом глаз


SELECT eye_color.eye_color,
    AVG(year)
FROM marvel_characters
INNER JOIN eye_color ON marvel_characters.eye_id = eye_color.id
GROUP BY eye_color.eye_color;


--Задание 11: Персонаж с наибольшим количеством появлений

SELECT name , appearances
FROM marvel_characters
WHERE appearances= (SELECT MAX(appearances) AS max_appearances
                    FROM marvel_characters);



--Задание 12: Персонажи, впервые появившиеся в том же году, что и персонаж с максимальными появлениями


SELECT name, year
FROM marvel_characters
WHERE year = (SELECT year
              FROM marvel_characters
              WHERE appearances = (SELECT MAX(appearances)
                                  FROM marvel_characters));

--Задание 13: Персонажи с наименьшим количеством появлений среди живых


SELECT name, appearances
FROM marvel_characters
INNER JOIN living_status ON marvel_characters.alive_id = living_status.id
WHERE appearances = (SELECT MIN(appearances)
                     FROM marvel_characters
                     INNER JOIN living_status ON marvel_characters.alive_id = living_status.id
                         AND living_status.living_status = 'Living Characters')
AND living_status.living_status = 'Living Characters';

--Задание 14: Персонажи с определенным цветом волос и максимальными появлениями среди такого цвета

SELECT name,
    hair_color.hair_color,
    max(appearances) as appearances
FROM marvel_characters
INNER JOIN hair_color on marvel_characters.hair_id = hair_color.id
WHERE appearances in (
    SELECT
       max(appearances)
    FROM marvel_characters
    INNER JOIN hair_color on marvel_characters.hair_id = hair_color.id
    WHERE hair_color.hair_color = 'Blond Hair')
AND hair_color.hair_color = 'Blond Hair';


--Задание 15: Персонажи с публичной личностью и наименьшим количеством появлений


SELECT name,
    identify.identify,
    appearances
FROM marvel_characters
INNER JOIN identify on marvel_characters.identify_id = identify.id
WHERE appearances in (
    SELECT
       min(appearances)
    FROM marvel_characters
    INNER JOIN identify on marvel_characters.identify_id = identify.id
    WHERE identify.identify = 'Public Identity')
AND identify.identify = 'Public Identity';

--Задание 16: Обновление статуса персонажей


BEGIN;

UPDATE marvel_characters set alive_id = (SELECT id FROM living_status WHERE living_status =  "Living Characters")
WHERE alive_id = (SELECT id FROM living_status WHERE living_status =  "Deceased Characters");

--UPDATE marvel_characters set alive_id = 2 WHERE alive_id = 1;


--ROLLBACK;
COMMIT;

--Задание 17: Добавление нового персонажа

BEGIN;

INSERT INTO
marvel_characters(page_id, name, urlslug, identify_id, align_id, eye_id, hair_id, sex_id, gsm_id, alive_id, appearances,
                  first_appearance, year)
VALUES(55555, "Чебурашка", "Чебурашка", 2, 1, 3, 1, 3, NULL, 1, 5, "Mar-69", 1969);

--ROLLBACK;
COMMIT;

--Задание 18: Удаление персонажей с нулевыми появлениями


BEGIN;

DELETE FROM  marvel_characters WHERE appearances = 0;

--ROLLBACK;
COMMIT;

--Задание 19: Обновление цвета волос персонажей


BEGIN;

UPDATE marvel_characters set hair_id = (SELECT id FROM hair_color WHERE hair_color =  "Blond Hair")
WHERE hair_id = (SELECT id FROM hair_color WHERE hair_color =  "Strawberry Blond Hair");

--UPDATE marvel_characters set hair_id = 4 WHERE hair_id = 13;


--ROLLBACK;
COMMIT;

--Задание 20: Добавление нового статуса

BEGIN;

INSERT INTO living_status (living_status) VALUES ("Unknown Status");

--ROLLBACK;
COMMIT;

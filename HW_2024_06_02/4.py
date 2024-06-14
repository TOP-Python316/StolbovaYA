# --4. Вывести имя и год появления всех голубоглазых блондинов 60-х и 80-х годов отсортированных по году по возрастанию [140 записей]
SELECT
    name,
    year
FROM MarvelCharacters
WHERE hair  = 'Blond Hair'
    AND eye = 'Blue Eyes'
    AND (year BETWEEN 1960 AND 1969 OR year BETWEEN 1980 AND 1989)
ORDER BY year
# --3. Вывести все уникальные сочетания цветов волос в алфавитном порядке и глаз в алафавитном порядке исключяя не заполненные данные (т. е. не должно быть NULL ни в одном из двух столбцов) [201 запись]
SELECT DISTINCT
    (hair,
     eye)
FROM MarvelCharacters
WHERE hair  NOT NULL
    AND eye NOT NULL
ORDER BY hair, eye
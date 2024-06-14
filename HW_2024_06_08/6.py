# 6. Герои и злодеи с необычными прическами
#     - Описание: Вывести имя, align, и описание прически. Найти персонажей с прическами, не являющимися стандартными (не Brown, Black, Blond, Red), а также их сторону (align) где align Good Characters или Bad Characters.
#     - Выборка: Имя, align, описание прически; где прическа не Brown, Black, Blond, или Red.
#     - Количество строк: 2744

SELECT
    name,
    align,
    hair
FROM MarvelCharacters
WHERE hair NOT IN ('Brown Hair','Black Hair','Blond Hair','Red Hair')
    AND align IN ('Good Characters','Bad Characters');
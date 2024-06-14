2. Герои с тайной идентичностью и необычными глазами
    - Описание: Вывести имя, год первого появления, и цвет глаз. Выбрать персонажей с тайной идентичностью (Secret Identity) и цветом глаз не из обычного спектра (не Blue, Brown, Green).
    - Выборка: Имя, год первого появления, цвет глаз; где идентификация — Secret Identity, и цвет глаз не Blue, Brown, или Green.
    - Количество строк: 1080

SELECT
    name,
    FIRST_APPEARANCE,
    eye
FROM MarvelCharacters
WHERE identify = 'Secret Identity'
   AND  eye  NOT IN ('Blue Eyes','Brown Eyes','Green Eyes');
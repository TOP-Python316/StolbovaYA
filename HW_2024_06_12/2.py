

# --3.Выведите все данные из таблицы "Students".
SELECT * FROM Students;

# --4. Выведите только имена и средние баллы студентов из таблицы "Students".
SELECT name,
       GPA
FROM Students;

# --5. Выведите всех студентов, которые изучают "Computer Science".
SELECT * FROM Students
WHERE major = 'Computer Science';

# --6.Выведите всех студентов, средний балл которых превышает 3.5.

SELECT * FROM Students
WHERE GPA > 3.5;

# -- 7. Обновите средний балл студента с ID 1 на 3.6.

BEGIN;
UPDATE Students SET GPA = 3.6
WHERE id = 1;

--ROLLBACK;
COMMIT;

# -- 8. Обновите специальность всех студентов, средний балл которых ниже или равен 3.4, на "Undecided".

BEGIN;
UPDATE Students SET major = 'Undecided'
WHERE GPA <= 3.4;

--ROLLBACK;
COMMIT;

# -- 9. Удалите студента с ID 5 из таблицы "Students".

BEGIN;
DELETE FROM Students WHERE id = 5;

--ROLLBACK;
COMMIT;

# -- 10. Удалите всех студентов, которые изучают "Economics".

BEGIN;
DELETE FROM Students WHERE major = 'Economics';

--ROLLBACK;
COMMIT;

# -- 11. Выведите количество студентов в таблице "Students".

SELECT COUNT(*) as count_students
FROM Students;

# -- 12. Выведите средний возраст студентов в таблице "Students".

SELECT AVG(age) as age
FROM Students;

# -- 13. Выведите имена и средние баллы всех студентов, отсортированных по среднему баллу в порядке убывания.

SELECT name,
       GPA
FROM Students
ORDER BY GPA DESC;

# -- 14. Выведите всех студентов, средний балл которых выше среднего по таблице.

SELECT * FROM Students
WHERE GPA > (
    SELECT AVG(GPA) as avg_gpa FROM Students);


# -- 15. Выведите имена и средние баллы всех студентов, специальность которых начинается на "C", отсортированных по имени в порядке возрастания.

SELECT name, GPA
FROM Students
WHERE major LIKE 'C%'
ORDER BY name;


# -- 16. Обновите специальность всех студентов на "Advanced", средний балл которых выше или равен 3.8.

BEGIN;
UPDATE Students SET major = 'Advanced'
WHERE GPA >= 3.8;

--ROLLBACK;
COMMIT;

# -- 17. Обновите специальность студента с ID 1 на "Mathematics".

BEGIN;
UPDATE Students SET major = 'Mathematics'
WHERE id = 1;

--ROLLBACK;
COMMIT;

# -- 18. Обновите имена всех студентов, средний балл которых выше 3.5, добавив к их имени префикс "Top student".

BEGIN;
UPDATE Students
SET name = "Top student " || name
WHERE GPA > 3.5;

--ROLLBACK;
COMMIT;

# -- 19. Удалите всех студентов, возраст которых ниже 18 лет.

BEGIN;
DELETE FROM Students WHERE age < 18;

--ROLLBACK;
COMMIT;

# -- 20. Удалите всех студентов, средний балл которых ниже 2.0.

BEGIN;
DELETE FROM Students WHERE GPA < 2.0;

--ROLLBACK;
COMMIT;

# -- 21. Измените таблицу "Students", добавив поле "Email" типа TEXT.


ALTER TABLE Students
ADD COLUMN Email TEXT;

# -- 22. Измените таблицу "Students", переименовав поле "major" в "Specialization".

ALTER TABLE Students RENAME COLUMN major TO Specialization;


# -- 23. Измените таблицу "Students", удалив поле "Email".

ALTER TABLE Students DROP COLUMN Email;

CREATE TABLE IF NOT EXISTS MarvelCharacters_new ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    page_id          INTEGER,  
    name             TEXT,  
    urlslug          TEXT,  
    identify         TEXT,  
    ALIGN            TEXT,  
    EYE              TEXT,  
    HAIR             TEXT,  
    SEX              TEXT,  
    GSM              TEXT,  
    ALIVE            TEXT,  
    APPEARANCES      INTEGER,  
    FIRST_APPEARANCE TEXT,  
    Year             INTEGER  
);

BEGIN;

INSERT INTO MarvelCharacters_new (
    page_id,
    name,
    urlslug,
    identify,
    align,
    eye,
    hair,
    sex,
    GSM,
    alive,
    appearances,
    first_appearance,
    year)
    
SELECT
    page_id,
    name,
    urlslug,
    identify,
    align,
    eye,
    hair,
    sex,
    GSM,
    alive,
    appearances,
    first_appearance,
    year
FROM
    MarvelCharacters;

DROP TABLE MarvelCharacters;

COMMIT;
/*ROLLBACK;*/

ALTER TABLE MarvelCharacters_new RENAME TO MarvelCharacters;

BEGIN;

CREATE TABLE IF NOT EXISTS identify (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    identify TEXT UNIQUE  
);

CREATE TABLE IF NOT EXISTS alignment (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    alignment TEXT UNIQUE  
);

CREATE TABLE IF NOT EXISTS eye_color (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    eye_color TEXT UNIQUE  
);

CREATE TABLE IF NOT EXISTS hair_color (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    hair_color TEXT UNIQUE  
);

CREATE TABLE IF NOT EXISTS sex (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    sex TEXT UNIQUE  
);

CREATE TABLE IF NOT EXISTS GSM (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    gsm TEXT UNIQUE  
);

CREATE TABLE IF NOT EXISTS living_status (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    living_status TEXT UNIQUE  
);

COMMIT;

BEGIN;

INSERT INTO identify (identify)
SELECT DISTINCT identify
FROM marvelcharacters
WHERE identify IS NOT NULL AND identify != '';

INSERT INTO alignment (alignment)
SELECT DISTINCT align
FROM marvelcharacters
WHERE align IS NOT NULL AND align != '';

INSERT INTO eye_color (eye_color)
SELECT DISTINCT eye
FROM marvelcharacters
WHERE eye IS NOT NULL AND eye != '';

INSERT INTO hair_color (hair_color)
SELECT DISTINCT hair
FROM marvelcharacters
WHERE hair IS NOT NULL AND hair != '';

INSERT INTO sex (sex)
SELECT DISTINCT sex
FROM marvelcharacters
WHERE sex IS NOT NULL AND sex != '';

INSERT INTO GSM (gsm)
SELECT DISTINCT gsm
FROM marvelcharacters
WHERE gsm IS NOT NULL AND gsm != '';

INSERT INTO living_status (living_status)
SELECT DISTINCT alive
FROM marvelcharacters
WHERE alive IS NOT NULL AND alive != '';

COMMIT;
/*ROLLBACK;*/

DROP TABLE marvel_characters_temp;

CREATE TABLE IF NOT EXISTS marvel_characters_temp (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    page_id          INTEGER,
    name             TEXT,
    urlslug          TEXT,
    identify_id      INTEGER,
    align_id         INTEGER,
    eye_id           INTEGER,
    hair_id          INTEGER,
    sex_id           INTEGER,
    gsm_id           INTEGER,
    alive_id         INTEGER,
    appearances      INTEGER,
    first_appearance TEXT,
    year             INTEGER
    
);

BEGIN;
INSERT INTO marvel_characters_temp (
    page_id,
    name,
    urlslug, 
    identify_id,
    align_id,
    eye_id,
    hair_id,
    sex_id,
    gsm_id,
    alive_id,
    appearances,
    first_appearance,
    year
)  
SELECT
    mc.page_id,
    mc.name,
    mc.urlslug,
    i.id,
    a.id,
    ec.id,
    hc.id,
    s.id,
    g.id,
    ls.id,
    mc.appearances,
    mc.first_appearance,
    mc.year 
FROM
    marvelcharacters mc  
        LEFT JOIN identify i ON mc.identify = i.identify
        LEFT JOIN alignment a ON mc.align = a.alignment
        LEFT JOIN eye_color ec ON mc.eye = ec.eye_color
        LEFT JOIN hair_color hc ON mc.hair = hc.hair_color
        LEFT JOIN sex s ON mc.sex = s.sex
        LEFT JOIN GSM g ON mc.GSM = g.gsm
        LEFT JOIN living_status ls ON mc.alive = ls.living_status;
COMMIT;
/*ROLLBACK;*/

DROP TABLE MarvelCharacters;
ALTER TABLE marvel_characters_temp RENAME TO marvel_characters;

SELECT mc.name, s.sex as sex
FROM marvel_characters mc
   JOIN sex s ON mc.id = s.id;
   

   
SELECT mc.name, ec.eye_color as eye_color
FROM marvel_characters mc
    JOIN eye_color ec ON mc.eye_id = ec.id;
    

    
SELECT mc.name, hc.hair_color as hair_color, ls.living_status as living_status
FROM marvel_characters mc
   JOIN hair_color hc ON mc.hair_id = hc.id
   JOIN living_status ls ON mc.alive_id = ls.id;
   

   
SELECT mc.name, id.identify as identity, al.alignment as alignment
FROM marvel_characters mc
    JOIN identify id ON mc.identify_id = id.id
    JOIN alignment al ON mc.align_id = al.id;
    

SELECT 
    mc.name,
    mc.appearances,
    mc.first_appearance,
    mc.year,
    s.sex AS sex,
    ec.eye_color AS eye_color,
    hc.hair_color AS hair_color, 
    al.alignment AS alignment,
    ls.living_status AS living_status, 
    id.identify AS identity
FROM marvel_characters mc
    JOIN sex s ON mc.sex_id = s.id
    JOIN eye_color ec ON mc.eye_id = ec.id
    JOIN hair_color hc ON mc.hair_id = hc.id
    JOIN alignment al ON mc.align_id = al.id
    JOIN living_status ls ON mc.alive_id = ls.id
    JOIN identify id ON mc.identify_id = id.id;
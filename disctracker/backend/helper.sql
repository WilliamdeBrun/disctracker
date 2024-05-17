INSERT INTO course (coursename, location, description) VALUES
('Hammarens DiscGolfPark', 'Mariefred', 'A beginner-friendly course'),
('Rydskogens DGC', 'Linköping', 'A somewhat tricky course that fits all levels of players');

INSERT INTO holes (courseid, holenr, par) VALUES
(1, 1, 3),
(1, 2, 3),
(1, 3, 3),
(1, 4, 3),
(1, 5, 3),
(1, 6, 3),
(1, 7, 3),
(1, 8, 3),
(1, 9, 4),
(1, 10, 3),
(1, 11, 4),
(1, 12, 3),
(1, 13, 3),
(1, 14, 3),
(1, 15, 3),
(1, 16, 3),
(1, 17, 3),
(1, 18, 3);

INSERT INTO holes (courseid, holenr, par) VALUES
(2, 1, 3),
(2, 2, 4),
(2, 3, 4),
(2, 4, 3),
(2, 5, 3),
(2, 6, 3),
(2, 7, 3),
(2, 8, 5),
(2, 9, 3),
(2, 10, 3),
(2, 11, 4),
(2, 12, 3),
(2, 13, 5),
(2, 14, 3),
(2, 15, 3),
(2, 16, 3),
(2, 17, 4),
(2, 18, 3);


-- Inserting some users for testing:
INSERT INTO users (username, realname, email, passwd, gender) VALUES 
('wille1', 'wille', 'wille1@example.com', 'wille1', 'male'),
('matte1011', 'matte', 'matte1011@example.com', '123', 'male'),
('john_doe', 'John Doe', 'john.doe@example.com', 'password1', 'male'),
('jane_smith', 'Jane Smith', 'jane.smith@example.com', 'password2', 'female'),
('alexander_wang', 'Alexander Wang', 'alexander.wang@example.com', 'password3', 'male'),
('emily_jones', 'Emily Jones', 'emily.jones@example.com', 'password4', 'female'),
('david_brown', 'David Brown', 'david.brown@example.com', 'password5', 'male'),
('sophia_clark', 'Sophia Clark', 'sophia.clark@example.com', 'password6', 'female'),
('william_taylor', 'William Taylor', 'william.taylor@example.com', 'password7', 'male'),
('olivia_miller', 'Olivia Miller', 'olivia.miller@example.com', 'password8', 'female'),
('james_wilson', 'James Wilson', 'james.wilson@example.com', 'password9', 'male'),
('emma_white', 'Emma White', 'emma.white@example.com', 'password10', 'female');

-- Inserting some friendships for testing
INSERT INTO friends (uid1, uid2) VALUES 
(1,2), (1,3), (1,4), (1,5), (1,6),(1,7),(1,8),(1,9),
(2,3), (2,4), (2,5), (2,6), (2,7), (2,8),(2,9),
(3,4), (3,5), (3,6), (3,7), (3,8),(3,9),
(4,5), (4,6), (4,7), (4,8),(4,9),
(5,6), (5,7), (5,8),(5,9),
(6,7), (6,8),(6,9),
(7,8),(7,9),
(8,9);


INSERT INTO rounds VALUES (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ();

-- Add scores for roundid 1 (Course 1)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    1 AS uid, -- User ID for 'wille1'
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    1 AS roundid
FROM
    holes
WHERE
    courseid = 1
LIMIT 18; -- Two scores for each hole on an 18-hole course

-- Add scores for roundid 2 (Course 2)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    1 AS uid, -- User ID for 'wille1'
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    2 AS roundid
FROM
    holes
WHERE
    courseid = 2
LIMIT 18; -- Two scores for each hole on an 18-hole course

-- Add scores for roundid 3 (Course 1)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    1 AS uid, -- User ID for 'wille1'
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    3 AS roundid
FROM
    holes
WHERE
    courseid = 1
LIMIT 18; -- Two scores for each hole on an 18-hole course

-- Add scores for roundid 4 (Course 2)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    1 AS uid, -- User ID for 'wille1'
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    4 AS roundid
FROM
    holes
WHERE
    courseid = 2
LIMIT 18; -- Two scores for each hole on an 18-hole course


-- Add scores for user with uid=2 and roundid 5 (Course 1)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    2 AS uid, -- User ID for the new user
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    5 AS roundid
FROM
    holes
WHERE
    courseid = 1
LIMIT 18; -- Two scores for each hole on an 18-hole course

-- Add scores for user with uid=2 and roundid 6 (Course 2)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    2 AS uid, -- User ID for the new user
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    6 AS roundid
FROM
    holes
WHERE
    courseid = 2
LIMIT 18; -- Two scores for each hole on an 18-hole course

-- Add scores for user with uid=2 and roundid 7 (Course 1)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    2 AS uid, -- User ID for the new user
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    7 AS roundid
FROM
    holes
WHERE
    courseid = 1
LIMIT 18; -- Two scores for each hole on an 18-hole course

-- Add scores for user with uid=2 and roundid 8 (Course 2)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    2 AS uid, -- User ID for the new user
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    8 AS roundid
FROM
    holes
WHERE
    courseid = 2
LIMIT 18; -- Two scores for each hole on an 18-hole course


-- Add scores for user with uid=3 and roundid 9 (Course 1)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    3 AS uid, -- User ID for the new user
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    9 AS roundid
FROM
    holes
WHERE
    courseid = 1
LIMIT 18; -- Two scores for each hole on an 18-hole course

-- Add scores for user with uid=3 and roundid 10 (Course 2)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    3 AS uid, -- User ID for the new user
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    10 AS roundid
FROM
    holes
WHERE
    courseid = 2
LIMIT 18; -- Two scores for each hole on an 18-hole course

-- Add scores for user with uid=3 and roundid 11 (Course 1)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    3 AS uid, -- User ID for the new user
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    11 AS roundid
FROM
    holes
WHERE
    courseid = 1
LIMIT 18; -- Two scores for each hole on an 18-hole course

-- Add scores for user with uid=3 and roundid 12 (Course 2)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    3 AS uid, -- User ID for the new user
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    12 AS roundid
FROM
    holes
WHERE
    courseid = 2
LIMIT 18; -- Two scores for each hole on an 18-hole course


-- Add scores for user with uid=4 and roundid 13 (Course 1)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    4 AS uid, -- User ID for the new user
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    13 AS roundid
FROM
    holes
WHERE
    courseid = 1
LIMIT 18; -- Two scores for each hole on an 18-hole course

-- Add scores for user with uid=4 and roundid 14 (Course 2)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    4 AS uid, -- User ID for the new user
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    14 AS roundid
FROM
    holes
WHERE
    courseid = 2
LIMIT 18; -- Two scores for each hole on an 18-hole course

-- Add scores for user with uid=4 and roundid 15 (Course 1)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    4 AS uid, -- User ID for the new user
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    15 AS roundid
FROM
    holes
WHERE
    courseid = 1
LIMIT 18; -- Two scores for each hole on an 18-hole course

-- Add scores for user with uid=4 and roundid 16 (Course 2)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    4 AS uid, -- User ID for the new user
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    16 AS roundid
FROM
    holes
WHERE
    courseid = 2
LIMIT 18; -- Two scores for each hole on an 18-hole course


-- Add scores for user with uid=5 and roundid 17 (Course 1)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    5 AS uid, -- User ID for the new user
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    17 AS roundid
FROM
    holes
WHERE
    courseid = 1
LIMIT 18; -- Two scores for each hole on an 18-hole course

-- Add scores for user with uid=5 and roundid 18 (Course 2)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    5 AS uid, -- User ID for the new user
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    18 AS roundid
FROM
    holes
WHERE
    courseid = 2
LIMIT 18; -- Two scores for each hole on an 18-hole course

-- Add scores for user with uid=5 and roundid 19 (Course 1)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    5 AS uid, -- User ID for the new user
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    19 AS roundid
FROM
    holes
WHERE
    courseid = 1
LIMIT 18; -- Two scores for each hole on an 18-hole course

-- Add scores for user with uid=5 and roundid 20 (Course 2)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    5 AS uid, -- User ID for the new user
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    20 AS roundid
FROM
    holes
WHERE
    courseid = 2
LIMIT 18; -- Two scores for each hole on an 18-hole course


-- Add scores for user with uid=6 and roundid 21 (Course 1)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    6 AS uid, -- User ID for the new user
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    21 AS roundid
FROM
    holes
WHERE
    courseid = 1
LIMIT 18; -- Two scores for each hole on an 18-hole course

-- Add scores for user with uid=6 and roundid 22 (Course 2)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    6 AS uid, -- User ID for the new user
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    22 AS roundid
FROM
    holes
WHERE
    courseid = 2
LIMIT 18; -- Two scores for each hole on an 18-hole course

-- Add scores for user with uid=6 and roundid 23 (Course 1)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    6 AS uid, -- User ID for the new user
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    23 AS roundid
FROM
    holes
WHERE
    courseid = 1
LIMIT 18; -- Two scores for each hole on an 18-hole course

-- Add scores for user with uid=6 and roundid 24 (Course 2)
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    6 AS uid, -- User ID for the new user
    courseid,
    holeid,
    FLOOR(1 + RAND() * 8) AS score, -- Random score between 1 and 8
    24 AS roundid
FROM
    holes
WHERE
    courseid = 2
LIMIT 18; -- Two scores for each hole on an 18-hole course

INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    6 AS uid, -- User ID for 'wille1'
    courseid,
    holeid,
    FLOOR(1 + RAND() * 3) AS score, -- Random score between 1 and 8
    35 AS roundid
FROM
    holes
WHERE
    courseid = 1
    AND holeid BETWEEN 10 AND 18
LIMIT 9; -- One score for each hole on holes 10-18
INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    6 AS uid, -- User ID for 'wille1'
    courseid,
    holeid,
    FLOOR(1 + RAND() * 4) AS score, -- Random score between 1 and 8
    36 AS roundid
FROM
    holes
WHERE
    courseid = 2
    AND holeid BETWEEN 19 AND 27
LIMIT 9; -- One score for each hole on holes 10-18

INSERT INTO score (uid, courseid, holeid, score, roundid)
SELECT
    6 AS uid, -- User ID for 'wille1'
    courseid,
    holeid,
    FLOOR(1 + RAND() * 4) AS score, -- Random score between 1 and 8
    36 AS roundid
FROM
    holes
WHERE
    courseid = 2
    AND holeid BETWEEN 28 AND 36
LIMIT 9; -- One score for each hole on holes 10-18


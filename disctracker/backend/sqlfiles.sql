
ALTER TABLE holes DROP FOREIGN KEY fk_course;
ALTER TABLE friends DROP FOREIGN KEY fk_user1;
ALTER TABLE friends DROP FOREIGN KEY fk_user2;
ALTER TABLE score DROP FOREIGN KEY fk_user;
ALTER TABLE score DROP FOREIGN KEY fk_hole;
ALTER TABLE score DROP FOREIGN KEY fk_course_score;
ALTER TABLE score DROP FOREIGN KEY fk_round;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS friends;
DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS holes;
DROP TABLE IF EXISTS score;
DROP TABLE IF EXISTS rounds;


-- Create the users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    realname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    passwd VARCHAR(255) NOT NULL,
    gender VARCHAR(255) NOT NULL,
    CONSTRAINT unique_username UNIQUE (username), -- Ensure usernames are unique
    CONSTRAINT unique_email UNIQUE (email) -- Ensure emails are unique
);

-- Create the friends table
CREATE TABLE friends (
    friendshipid INT AUTO_INCREMENT PRIMARY KEY,
    uid1 INT NOT NULL,
    uid2 INT NOT NULL,
    CONSTRAINT fk_user1 FOREIGN KEY (uid1) REFERENCES users(id),
    CONSTRAINT fk_user2 FOREIGN KEY (uid2) REFERENCES users(id),
    CONSTRAINT unique_friendship UNIQUE(uid1, uid2),
    CONSTRAINT check_different_users CHECK (uid1 <> uid2) -- Ensure users are different
);

-- Create the course table
CREATE TABLE course (
    courseid INT AUTO_INCREMENT PRIMARY KEY,
    coursename VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL, -- Make location mandatory
    description TEXT,
    CONSTRAINT unique_coursename UNIQUE (coursename) -- Ensure course names are unique
);

-- Create the holes table with a foreign key reference to courseid
CREATE TABLE holes (
    holeid INT AUTO_INCREMENT PRIMARY KEY,
    courseid INT NOT NULL,
    holenr INT NOT NULL,
    par INT,
    CONSTRAINT fk_course FOREIGN KEY (courseid) REFERENCES course(courseid)
);

CREATE TABLE rounds(
    roundid INT AUTO_INCREMENT PRIMARY KEY
);
-- Create the score table with foreign key references to user id and course id
CREATE TABLE score (
    scoreid INT AUTO_INCREMENT PRIMARY KEY,
    uid INT NOT NULL,
    courseid INT NOT NULL,
    holeid INT NOT NULL,
    score INT,
    roundid INT NOT NULL,
    CONSTRAINT fk_round FOREIGN KEY (roundid) REFERENCES rounds(roundid),
    CONSTRAINT fk_hole FOREIGN KEY (holeid) REFERENCES holes(holeid),
    CONSTRAINT fk_user FOREIGN KEY (uid) REFERENCES users(id),
    CONSTRAINT fk_course_score FOREIGN KEY (courseid) REFERENCES course(courseid)
);

select * from course;
select * from score;
select * from rounds;
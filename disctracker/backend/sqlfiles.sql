
DROP TABLE IF EXISTS users;


CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    passwd VARCHAR(255) NOT NULL
);
-- Insert data into the table
INSERT INTO users (username, email, passwd) VALUES ('user1', 'user1@example.com', 'root'), ('user2', 'user2@example.com', 'root');

-- Select data from the table
SELECT username FROM users where id = 1;

-- Update data in the table
UPDATE users SET email = 'new_email@example.com' WHERE username = 'user1';

-- Delete data from the table
DELETE FROM users WHERE username = 'user2';
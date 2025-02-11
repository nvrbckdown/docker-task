-- Create the movies table
CREATE TABLE IF NOT EXISTS movies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    rating DECIMAL(2, 1) NOT NULL
);

-- Insert initial data
INSERT INTO movies (name, rating) VALUES
('Avatar', 5.0),
('Inception', 4.8),
('Titanic', 4.7),
('Qish sanatasi', 3.0),
('O`tgan kunlar', 4.5),
('Бригад', 5.0),
('Terminator', 1.1);

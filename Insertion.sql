INSERT INTO Person (Name, Age, Gender) VALUES
('Christopher Nolan', 52, 'Male'),
('Quentin Tarantino', 59, 'Male'),
('Leonardo DiCaprio', 48, 'Male'),
('Kate Winslet', 47, 'Female'),
('Anne Hathaway', 40, 'Female'),
('Christian Bale', 49, 'Male'),
('James Cameron', 68, 'Male'),
('Robert Downey Jr.', 58, 'Male'),
('Scarlett Johansson', 39, 'Female'),
('Tom Hardy', 46, 'Male');

INSERT INTO Actor (Actor_ID, AwardsCount) VALUES
(3, 3), 
(4, 1), 
(5, 2), 
(6, 4), 
(8, 3),
(9, 2), 
(10, 1); 


INSERT INTO Director (Director_ID, DirectorFamousFor) VALUES
(1, 'Inception'),
(2, 'Pulp Fiction'),
(7, 'Titanic');

INSERT INTO LeadingActor (LeadingActor_ID, MostIconicRole) VALUES
(3, 'Cobb in Inception'), 
(6, 'Batman in The Dark Knight'),
(10, 'Eames in Inception'); 


INSERT INTO SupportingActor (SupportingActor_ID, SceneCount) VALUES
(4, 25), 
(5, 20), 
(8, 18), 
(9, 22); 


INSERT INTO Movie (MovieTitle, Rating, Duration, ReleaseDate, Director_ID) VALUES
('Inception', 8.8, 148, '2010-07-16', 1),
('Interstellar', 8.6, 169, '2014-11-07', 1),
('The Dark Knight', 9.0, 152, '2008-07-18', 1),
('Titanic', 7.8, 195, '1997-12-19', 7),
('Pulp Fiction', 8.9, 154, '1994-10-14', 2),
('Avatar', 7.8, 162, '2009-12-18', 7),
('Django Unchained', 8.4, 165, '2012-12-25', 2),
('The Avengers', 8.0, 143, '2012-05-04', 1),
('Black Widow', 6.8, 134, '2021-07-09', 1),
('Mad Max: Fury Road', 8.1, 120, '2015-05-15', 1);


INSERT INTO Genre (GenreName) VALUES
('Sci-Fi'),
('Action'),
('Drama'),
('Thriller'),
('Adventure'),
('Fantasy'),
('Romance'),
('Crime'),
('Comedy'),
('War');


INSERT INTO MovieGenres (Movie_ID, Genre_ID) VALUES
(1, 1), 
(1, 2), 
(2, 1), 
(2, 3),
(3, 2), 
(3, 4), 
(4, 3), 
(4, 7),
(5, 8), 
(6, 1); 


INSERT INTO MovieActors (Movie_ID, Actor_ID) VALUES
(1, 3), 
(1, 10),
(2, 5), 
(2, 10), 
(3, 6),
(4, 4), 
(5, 9), 
(6, 8), 
(7, 3),
(8, 9); 


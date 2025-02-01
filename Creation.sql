CREATE TABLE Person (
    Person_ID INT IDENTITY(1,1) PRIMARY KEY, 
    Name VARCHAR(255) NOT NULL,             
    Age INT CHECK (Age > 0),                
    Gender VARCHAR(10) NOT NULL             
);


CREATE TABLE Actor (
    Actor_ID INT PRIMARY KEY,               
    AwardsCount INT DEFAULT 0,              
    FOREIGN KEY (Actor_ID) REFERENCES Person(Person_ID)
        ON DELETE NO ACTION ON UPDATE CASCADE 
);


CREATE TABLE Director (
    Director_ID INT PRIMARY KEY,            
    DirectorFamousFor VARCHAR(255),        
    FOREIGN KEY (Director_ID) REFERENCES Person(Person_ID)
        ON DELETE NO ACTION ON UPDATE CASCADE 
);


CREATE TABLE LeadingActor (
    LeadingActor_ID INT PRIMARY KEY,        
    MostIconicRole VARCHAR(255),            
    FOREIGN KEY (LeadingActor_ID) REFERENCES Actor(Actor_ID)
        ON DELETE CASCADE ON UPDATE CASCADE 
);


CREATE TABLE SupportingActor (
    SupportingActor_ID INT PRIMARY KEY,     
    SceneCount INT DEFAULT 0,               
    FOREIGN KEY (SupportingActor_ID) REFERENCES Actor(Actor_ID)
        ON DELETE CASCADE ON UPDATE CASCADE 
);


CREATE TABLE Movie (
    Movie_ID INT IDENTITY(1,1) PRIMARY KEY, 
    MovieTitle VARCHAR(255) NOT NULL,      
    Rating DECIMAL(3, 1) CHECK (Rating BETWEEN 0 AND 10),
    Duration INT CHECK (Duration > 0),      
    ReleaseDate DATE NOT NULL,              
    Director_ID INT NOT NULL,               
    FOREIGN KEY (Director_ID) REFERENCES Director(Director_ID)
        ON DELETE NO ACTION ON UPDATE CASCADE 
);


CREATE TABLE Genre (
    Genre_ID INT IDENTITY(1,1) PRIMARY KEY, 
    GenreName VARCHAR(100) NOT NULL UNIQUE  
);


CREATE TABLE MovieGenres (
    MovieGenres_ID INT IDENTITY(1,1) PRIMARY KEY, 
    Movie_ID INT NOT NULL,                        
    Genre_ID INT NOT NULL,                        
    FOREIGN KEY (Movie_ID) REFERENCES Movie(Movie_ID)
        ON DELETE CASCADE ON UPDATE CASCADE,     
    FOREIGN KEY (Genre_ID) REFERENCES Genre(Genre_ID)
        ON DELETE NO ACTION ON UPDATE CASCADE     
);


CREATE TABLE MovieActors (
    MovieActors_ID INT IDENTITY(1,1) PRIMARY KEY, 
    Movie_ID INT NOT NULL,                        
    Actor_ID INT NOT NULL,                        
    FOREIGN KEY (Movie_ID) REFERENCES Movie(Movie_ID)
        ON DELETE CASCADE ON UPDATE CASCADE,     
    FOREIGN KEY (Actor_ID) REFERENCES Actor(Actor_ID)
        ON DELETE NO ACTION ON UPDATE CASCADE     
);

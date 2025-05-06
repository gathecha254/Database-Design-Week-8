-- Library Management System SQL Script
-- Tables: Members, Books, Authors, BookAuthors (M-M), Loans

-- Drop existing tables if they exist
DROP TABLE IF EXISTS Reservations;
DROP TABLE IF EXISTS Loans;
DROP TABLE IF EXISTS BookAuthors;
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Authors;
DROP TABLE IF EXISTS Members;

-- Create Members table
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    JoinDate DATE DEFAULT CURRENT_DATE,
    IsActive BOOLEAN DEFAULT TRUE
);

-- Create Authors table
CREATE TABLE Authors (
    AuthorID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Nationality VARCHAR(100)
);

-- Create Categories table
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(100) UNIQUE NOT NULL
);

-- Create Books table
CREATE TABLE Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    ISBN VARCHAR(13) UNIQUE NOT NULL,
    PublishedYear YEAR,
    CategoryID INT,
    QuantityAvailable INT DEFAULT 1 CHECK (QuantityAvailable >= 0),
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL
);

-- Junction table for many-to-many relationship between Books and Authors
CREATE TABLE BookAuthors (
    BookID INT,
    AuthorID INT,
    PRIMARY KEY (BookID, AuthorID),
    FOREIGN KEY (BookID) REFERENCES Books(BookID) ON DELETE CASCADE,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON DELETE CASCADE
);

-- Create Loans table
CREATE TABLE Loans (
    LoanID INT AUTO_INCREMENT PRIMARY KEY,
    MemberID INT NOT NULL,
    BookID INT NOT NULL,
    LoanDate DATE DEFAULT CURRENT_DATE,
    ReturnDate DATE,
    DueDate DATE,
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE,
    FOREIGN KEY (BookID) REFERENCES Books(BookID) ON DELETE CASCADE
);

-- Create Reservations table
CREATE TABLE Reservations (
    ReservationID INT AUTO_INCREMENT PRIMARY KEY,
    MemberID INT NOT NULL,
    BookID INT NOT NULL,
    ReservationDate DATE DEFAULT CURRENT_DATE,
    Status ENUM('Active', 'Completed', 'Cancelled') DEFAULT 'Active',
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE,
    FOREIGN KEY (BookID) REFERENCES Books(BookID) ON DELETE CASCADE
);

-- Insert sample members with African names and @gmail.com emails
INSERT INTO Members (Name, Email) VALUES
('Amina Jallow', 'aminajallow@gmail.com'),
('Kwame Boateng', 'kwameboateng@gmail.com'),
('Ngozi Eze', 'ngozi.eze@gmail.com'),
('Abdulai Conteh', 'abdulai.conteh@gmail.com'),
('Zinhle Dlamini', 'zinhledlamini@gmail.com'),
('Tendai Mutasa', 'tendaimutasa@gmail.com'),
('Chidi Okoro', 'chidi.okoro@gmail.com'),
('Sipho Moyo', 'sipho.moyo@gmail.com'),
('Adesuwa Obaseki', 'adesuwao@gmail.com'),
('Emeka Nwosu', 'emekanwosu@gmail.com');

-- Insert sample authors
INSERT INTO Authors (FirstName, LastName, Nationality) VALUES
('Chinua', 'Achebe', 'Nigerian'),
('Ngũgĩ wa', 'Thiong’o', 'Kenyan'),
('Chimamanda Ngozi', 'Adichie', 'Nigerian'),
('Tsitsi', 'Dangarembga', 'Zimbabwean'),
('Nnedi', 'Okorafor', 'Nigerian-American'),
('Ben', 'Okri', 'Nigerian'),
('Alain', 'Mabanckou', 'Congolese-French'),
('Yvonne', 'Owour', 'Kenyan'),
('Abubakar', 'Gimba', 'Nigerian'),
('Catherine', 'Ngila', 'Kenyan');

-- Insert sample categories
INSERT INTO Categories (CategoryName) VALUES
('Fiction'),
('Historical Fiction'),
('Contemporary Fiction'),
('Short Stories'),
('Coming-of-Age'),
('War Fiction'),
('Literary Fiction'),
('Science Fiction'),
('Poetry'),
('Non-fiction');

-- Insert sample books
INSERT INTO Books (Title, ISBN, PublishedYear, CategoryID, QuantityAvailable) VALUES
('Things We Lost in the Fire', '9781609454366', 2017, 4, 5),
('Americanah', '9780307455925', 2011, 3, 7),
('Half of a Yellow Sun', '9781400044160', 2006, 2, 4),
('Homegoing', '9781101971069', 2016, 2, 6),
('Purple Hibiscus', '9780060774528', 2003, 5, 5),
('Sozaboy', '9780813913474', 1985, 6, 3),
('The Hairdresser of Harare', '9781770220833', 2010, 3, 6),
('Disgrace', '9780140268661', 1999, 7, 2),
('Who Fears Death', '9780756406601', 2010, 8, 4),
('The Thing Around Your Neck', '9780307265777', 2008, 4, 4);

-- Link books to authors
INSERT INTO BookAuthors (BookID, AuthorID) VALUES
(1, 3), -- Chimamanda Ngozi Adichie
(2, 3), -- Americanah
(3, 1), -- Chinua Achebe - Half of a Yellow Sun
(4, 9), -- Abubakar Gimba - Homegoing (example)
(5, 3), -- Purple Hibiscus
(6, 10), -- Catherine Ngila - Sozaboy (example)
(7, 4), -- Tsitsi Dangarembga - The Hairdresser of Harare
(8, 6), -- Ben Okri - Disgrace (example)
(9, 5), -- Nnedi Okorafor - Who Fears Death
(10, 3); -- Chimamanda Ngozi Adichie

-- Insert sample loans
INSERT INTO Loans (MemberID, BookID, DueDate) VALUES
(1, 1, '2025-04-20'),
(2, 2, '2025-04-22'),
(3, 3, '2025-04-25'),
(4, 4, '2025-04-21'),
(5, 5, '2025-04-26'),
(6, 6, '2025-04-23'),
(7, 7, '2025-04-24'),
(8, 8, '2025-04-27'),
(9, 9, '2025-04-28'),
(10, 10, '2025-04-29');

-- Insert sample reservations
INSERT INTO Reservations (MemberID, BookID) VALUES
(1, 5),
(2, 7),
(3, 9),
(4, 2),
(5, 6),
(6, 8),
(7, 10),
(8, 1),
(9, 4),
(10, 3);

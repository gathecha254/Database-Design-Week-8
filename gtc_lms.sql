-- Library Management System SQL Script
-- Tables: Members, Books, Authors, BookAuthors (M-M), Loans

-- Drop existing tables if needed (for clean setup)
DROP TABLE IF EXISTS Loans;
DROP TABLE IF EXISTS BookAuthors;
DROP TABLE IF EXISTS Authors;
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Members;

-- Create Members table (Users who can borrow books)
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    JoinDate DATE DEFAULT CURRENT_DATE,
    IsActive BOOLEAN DEFAULT TRUE
);

-- Create Books table
CREATE TABLE Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    ISBN VARCHAR(13) UNIQUE NOT NULL,
    PublishedYear YEAR,
    Genre VARCHAR(100),
    QuantityAvailable INT DEFAULT 1 CHECK (QuantityAvailable >= 0)
);

-- Create Authors table
CREATE TABLE Authors (
    AuthorID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Nationality VARCHAR(100)
);

-- Many-to-Many relationship between Books and Authors
CREATE TABLE BookAuthors (
    BookID INT,
    AuthorID INT,
    PRIMARY KEY (BookID, AuthorID),
    FOREIGN KEY (BookID) REFERENCES Books(BookID) ON DELETE CASCADE,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON DELETE CASCADE
);

-- Create Loans table (Tracks borrowing history)
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

-- Insert sample members
INSERT INTO Members (Name, Email) VALUES
('Alice Wahome', 'alicewahomebtAgmail.com'),
('Moses Kuria', 'moseskuria@gmail.com'),
('Oscar Sudi', 'sudihajasoma@gmail.com');

-- Insert sample authors
INSERT INTO Authors (FirstName, LastName, Nationality) VALUES
('George', 'Orwell', 'British'),
('J.K.', 'Rowling', 'British'),
('Harper', 'Laine', 'American');

-- Insert sample books
INSERT INTO Books (Title, ISBN, PublishedYear, Genre, QuantityAvailable) VALUES
('1984', '9783161484100', 1949, 'Dystopian Fiction', 5),
('Harry Potter and the Philosopher\'s Stone', '9780439708180', 1997, 'Fantasy', 10),
('The Midnight Adventure', '9781234567890', 2020, 'Mystery', 3);

-- Link books to authors
INSERT INTO BookAuthors (BookID, AuthorID) VALUES
(1, 1), -- 1984 by George Orwell
(2, 2), -- Harry Potter by J.K. Rowling
(3, 3); -- The Midnight Adventure by Harper Laine

-- Insert sample loans
INSERT INTO Loans (MemberID, BookID, DueDate) VALUES
(1, 1, '2025-04-20'),
(2, 2, '2025-04-22'),
(3, 3, '2025-04-25');

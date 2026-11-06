/*
Customer Database Practice
Platform: Microsoft SQL Server (T-SQL)
Purpose: Practice database creation, table design, INSERT, SELECT, UPDATE and ALTER TABLE.

All names and phone values below are illustrative sample data.
The phone values are intentionally placeholders, not contact details.
*/

IF DB_ID(N'SQLclassDataDB') IS NULL
BEGIN
    CREATE DATABASE SQLclassDataDB;
END;
GO

USE SQLclassDataDB;
GO

-- Recreate the practice table safely without dropping the database.
IF OBJECT_ID(N'dbo.Customer_data_set', N'U') IS NOT NULL
BEGIN
    DROP TABLE dbo.Customer_data_set;
END;
GO

CREATE TABLE dbo.Customer_data_set
(
    customer_id   INT           NOT NULL PRIMARY KEY,
    customername  VARCHAR(50)   NOT NULL,
    lastname      VARCHAR(50)   NOT NULL,
    age           INT           NULL,
    phone_number  VARCHAR(25)   NULL,
    country       VARCHAR(100)  NULL,
    full_address  VARCHAR(200)  NULL,
    email_address VARCHAR(200)  NULL
);
GO

INSERT INTO dbo.Customer_data_set
    (customer_id, customername, lastname, country, age, phone_number)
VALUES
    (1,  'Amina',    'Yusuf',    'Nigeria',      20, '+234-000-000-0001'),
    (2,  'David',    'Olufo',    'Nigeria',      25, '+234-000-000-0002'),
    (3,  'Grace',    'Okafor',   'Nigeria',      29, '+234-000-000-0003'),
    (4,  'Fatima',   'Bello',    'Nigeria',      30, '+234-000-000-0004'),
    (5,  'Esther',   'Eze',      'Nigeria',      35, '+234-000-000-0005'),
    (6,  'John',     'Adewale',  'Nigeria',      27, '+234-000-000-0006'),
    (7,  'Michael',  'Okoro',    'South Africa', 45, '+234-000-000-0007'),
    (8,  'Zainab',   'Mohammed', 'Nigeria',      40, '+234-000-000-0008'),
    (9,  'Kemi',     'Ogunleye', 'Nigeria',      32, '+234-000-000-0009'),
    (10, 'Chiamaka', 'Uche',     'Nigeria',      38, '+234-000-000-0010'),
    (11, 'Ibrahim',  'Sani',     'Nigeria',      33, '+234-000-000-0011'),
    (12, 'Chinedu',  'Ali',      'Nigeria',      37, '+234-000-000-0012');
GO

-- Example SELECT queries.
SELECT *
FROM dbo.Customer_data_set;

SELECT *
FROM dbo.Customer_data_set
WHERE customer_id = 10;

-- Example UPDATE query.
UPDATE dbo.Customer_data_set
SET age = 39
WHERE customer_id = 10;

-- Generate illustrative email addresses from the sample names.
UPDATE dbo.Customer_data_set
SET email_address =
    LOWER(CONCAT(customername, '.', lastname, '@example.test'));
GO

-- Verify the updated records.
SELECT
    customer_id,
    customername,
    lastname,
    age,
    phone_number,
    country,
    email_address
FROM dbo.Customer_data_set
ORDER BY customer_id;
GO

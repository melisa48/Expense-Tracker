-- schema.sql

-- Drop the table if it exists to avoid conflicts
DROP TABLE IF EXISTS expense;

CREATE TABLE expense (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    amount FLOAT NOT NULL,
    category VARCHAR(50) NOT NULL,
    description VARCHAR(200)
);


-- Optionally, you can add some initial data for testing
INSERT INTO expense (amount, category, description) VALUES
(50.00, 'Food', 'Grocery shopping'),
(30.00, 'Transportation', 'Gas'),
(100.00, 'Entertainment', 'Concert tickets'),
(20.00, 'Health', 'Pharmacy');

-- You can add indexes to improve query performance
CREATE INDEX idx_expense_date ON expense(date);
CREATE INDEX idx_expense_category ON expense(category);

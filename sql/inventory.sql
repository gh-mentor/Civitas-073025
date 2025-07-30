-- Step 1: Database Setup

IF DB_ID('Inventory') IS NOT NULL
    DROP DATABASE Inventory;
GO

CREATE DATABASE Inventory;
GO

USE Inventory;
GO

-- Step 2: Table Creation (with 'description' column for each table)

-- Suppliers table
CREATE TABLE suppliers (
    supplier_id INT IDENTITY(1,1) PRIMARY KEY,
    supplier_name NVARCHAR(100) NOT NULL,
    description NVARCHAR(255),
    contact_name NVARCHAR(100),
    phone NVARCHAR(20),
    email NVARCHAR(100),
    created_at DATETIME2 DEFAULT SYSDATETIME(),
    updated_at DATETIME2 DEFAULT SYSDATETIME()
);

-- Categories table
CREATE TABLE categories (
    category_id INT IDENTITY(1,1) PRIMARY KEY,
    category_name NVARCHAR(100) NOT NULL,
    description NVARCHAR(255),
    supplier_id INT NOT NULL,
    created_at DATETIME2 DEFAULT SYSDATETIME(),
    updated_at DATETIME2 DEFAULT SYSDATETIME(),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

-- Products table
CREATE TABLE products (
    product_id INT IDENTITY(1,1) PRIMARY KEY,
    product_name NVARCHAR(100) NOT NULL,
    description NVARCHAR(255),
    category_id INT NOT NULL,
    quantity INT DEFAULT 0,
    price DECIMAL(10,2) NOT NULL,
    created_at DATETIME2 DEFAULT SYSDATETIME(),
    updated_at DATETIME2 DEFAULT SYSDATETIME(),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- Step 3: Data Population

-- Insert sample suppliers
INSERT INTO suppliers (supplier_name, description, contact_name, phone, email)
VALUES 
('Acme Corp', 'Leading supplier of industrial goods', 'John Doe', '555-1234', 'john@acme.com'),
('Global Traders', 'International trading company', 'Jane Smith', '555-5678', 'jane@global.com'),
('Fresh Produce Ltd', 'Supplier of fresh fruits and vegetables', 'Carlos Ruiz', '555-8765', 'carlos@freshproduce.com');

-- Insert sample categories
INSERT INTO categories (category_name, description, supplier_id)
VALUES
('Electronics', 'Electronic devices and accessories', 1),
('Office Supplies', 'Stationery and office equipment', 2),
('Groceries', 'Everyday grocery items', 3);

-- Insert sample products
INSERT INTO products (product_name, description, category_id, quantity, price)
VALUES
('Laptop', '15-inch business laptop', 1, 10, 1200.00),
('Printer Paper', 'A4 size, 500 sheets', 2, 50, 5.50),
('Bananas', 'Fresh organic bananas', 3, 100, 0.30),
('Smartphone', 'Latest model smartphone', 1, 20, 800.00),
('Stapler', 'Standard office stapler', 2, 30, 7.25),
('Apples', 'Red delicious apples', 3, 80, 0.40);

-- Step 4: Additional Features

-- 1. Create a view named product_list to display product, category, and supplier details
CREATE VIEW product_list AS
SELECT 
    p.product_id,
    p.product_name,
    p.description AS product_description,
    p.quantity,
    p.price,
    c.category_id,
    c.category_name,
    c.description AS category_description,
    s.supplier_id,
    s.supplier_name,
    s.description AS supplier_description
FROM products p
INNER JOIN categories c ON p.category_id = c.category_id
INNER JOIN suppliers s ON c.supplier_id = s.supplier_id;

-- 2. Implement a stored procedure to retrieve the product_list view
CREATE PROCEDURE get_product_list
AS
BEGIN
    SELECT * FROM product_list;
END;

-- 3. Add a trigger to update the products table when a categories record is deleted
CREATE TRIGGER trg_category_delete
ON categories
INSTEAD OF DELETE
AS
BEGIN
    -- Set category_id of affected products to NULL before deleting the category
    UPDATE products
    SET category_id = NULL
    WHERE category_id IN (SELECT category_id FROM deleted);

    DELETE FROM categories
    WHERE category_id IN (SELECT category_id FROM deleted);
END;

-- 4. Define functions to calculate the total number of products in a category
CREATE FUNCTION fn_total_products_in_category (@cat_id INT)
RETURNS INT
AS
BEGIN
    DECLARE @total INT;
    SELECT @total = COUNT(*) FROM products WHERE category_id = @cat_id;
    RETURN @total;
END;

-- ...and those supplied by a supplier
CREATE FUNCTION fn_total_products_by_supplier (@sup_id INT)
RETURNS INT
AS
BEGIN
    DECLARE @total INT;
    SELECT @total = COUNT(*) 
    FROM products p
    INNER JOIN categories c ON p.category_id = c.category_id
    INNER JOIN suppliers s ON c.supplier_id = s.supplier_id
    WHERE s.supplier_id = @sup_id;
    RETURN @total;
END;



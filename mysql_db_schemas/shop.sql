CREATE TABLE
    Categories (
        CategoryID INT PRIMARY KEY AUTO_INCREMENT,
        CategoryName VARCHAR(100) NOT NULL,
        Description TEXT
    );
    
CREATE TABLE
    Products (
        ProductID INT PRIMARY KEY AUTO_INCREMENT,
        ProductName VARCHAR(100) NOT NULL,
        CategoryID INT,
        Price DECIMAL(10, 2) NOT NULL,
        Stock INT NOT NULL,
        Description TEXT,
        FOREIGN KEY (CategoryID) REFERENCES Categories (CategoryID)
    );

CREATE TABLE
    Customers (
        CustomerID INT PRIMARY KEY AUTO_INCREMENT,
        FirstName VARCHAR(100) NOT NULL,
        LastName VARCHAR(100) NOT NULL,
        Email VARCHAR(100) UNIQUE NOT NULL,
        Password VARCHAR(100) NOT NULL,
        Address TEXT,
        Phone VARCHAR(15)
    );

CREATE TABLE
    Orders (
        OrderID INT PRIMARY KEY AUTO_INCREMENT,
        CustomerID INT,
        OrderDate DATETIME DEFAULT CURRENT_TIMESTAMP,
        Total DECIMAL(10, 2),
        Status VARCHAR(50),
        FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID)
    );

CREATE TABLE
    OrderDetails (
        OrderDetailID INT PRIMARY KEY AUTO_INCREMENT,
        OrderID INT,
        ProductID INT,
        Quantity INT NOT NULL,
        Price DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (OrderID) REFERENCES Orders (OrderID),
        FOREIGN KEY (ProductID) REFERENCES Products (ProductID)
    );

INSERT INTO
    Categories (CategoryName, Description)
VALUES
    (
        'Electronics',
        'Devices and gadgets including phones, laptops, and more'
    ),
    (
        'Books',
        'Wide range of books from various genres and authors'
    ),
    (
        'Clothing',
        'Apparel for men, women, and children'
    ),
    (
        'Home & Kitchen',
        'Products for home improvement and kitchen use'
    ),
    (
        'Sports & Outdoors',
        'Equipment and gear for outdoor activities and sports'
    );

INSERT INTO
    Products (
        ProductName,
        CategoryID,
        Price,
        Stock,
        Description
    )
VALUES
    (
        'Smartphone',
        1,
        699.99,
        50,
        'Latest model smartphone with advanced features'
    ),
    (
        'Laptop',
        1,
        1199.99,
        30,
        'High-performance laptop suitable for gaming and work'
    ),
    (
        'Novel',
        2,
        19.99,
        100,
        'Best-selling novel by a popular author'
    ),
    (
        'T-shirt',
        3,
        15.99,
        200,
        'Comfortable cotton t-shirt in various sizes'
    ),
    (
        'Blender',
        4,
        49.99,
        60,
        'High-speed blender perfect for making smoothies'
    ),
    (
        'Tent',
        5,
        89.99,
        40,
        '4-person tent ideal for camping'
    ),
    (
        'Tablet',
        1,
        499.99,
        75,
        'Portable tablet with high-resolution display'
    ),
    (
        'Cookbook',
        2,
        24.99,
        120,
        'Recipe book with delicious and easy-to-make dishes'
    ),
    (
        'Jeans',
        3,
        39.99,
        150,
        'Denim jeans with a stylish fit'
    ),
    (
        'Soccer Ball',
        5,
        25.99,
        80,
        'Durable soccer ball for training and matches'
    );

INSERT INTO
    Customers (
        FirstName,
        LastName,
        Email,
        Password,
        Address,
        Phone
    )
VALUES
    (
        'John',
        'Doe',
        'john.doe@example.com',
        'password123',
        '123 Main St, Anytown, USA',
        '555-1234'
    ),
    (
        'Jane',
        'Smith',
        'jane.smith@example.com',
        'password456',
        '456 Oak St, Anytown, USA',
        '555-5678'
    ),
    (
        'Alice',
        'Johnson',
        'alice.johnson@example.com',
        'password789',
        '789 Pine St, Anytown, USA',
        '555-8765'
    ),
    (
        'Bob',
        'Brown',
        'bob.brown@example.com',
        'password101',
        '101 Maple St, Anytown, USA',
        '555-4321'
    ),
    (
        'Charlie',
        'Davis',
        'charlie.davis@example.com',
        'password102',
        '102 Elm St, Anytown, USA',
        '555-8764'
    );

INSERT INTO
    Orders (CustomerID, OrderDate, Total, Status)
VALUES
    (1, '2023-06-15 14:30:00', 749.98, 'Shipped'),
    (2, '2023-06-16 09:45:00', 19.99, 'Processing'),
    (3, '2023-06-17 12:00:00', 65.98, 'Delivered'),
    (4, '2023-06-18 16:20:00', 119.98, 'Cancelled'),
    (5, '2023-06-19 11:30:00', 89.99, 'Shipped');

INSERT INTO
    OrderDetails (OrderID, ProductID, Quantity, Price)
VALUES
    (1, 1, 1, 699.99),
    (1, 3, 1, 19.99),
    (2, 3, 1, 19.99),
    (3, 5, 1, 49.99),
    (3, 9, 1, 15.99),
    (4, 10, 2, 25.99),
    (5, 6, 1, 89.99),
    (5, 2, 1, 1199.99),
    (5, 4, 1, 24.99),
    (5, 7, 1, 499.99);
-- @block inventory
CREATE TABLE inventory (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(100),
    stock_quantity INT,
    restock_threshold INT
);

-- @block sales
CREATE TABLE sales (
    order_id INT PRIMARY KEY,
    product_id VARCHAR(10),
    quantity_sold INT,
    sale_date DATE,
    FOREIGN KEY (product_id) REFERENCES inventory(product_id)
);

-- @block reviews
CREATE TABLE reviews (
    review_id INT PRIMARY KEY,
    product_id VARCHAR(10),
    product_name VARCHAR(255),
    review_text TEXT,
    rating INT,
    review_date DATE,
    FOREIGN KEY (product_id) REFERENCES inventory(product_id)
);

-- @block print
SELECT * FROM inventory;
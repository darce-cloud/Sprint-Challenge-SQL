'''docstring'''
import sqlite3


conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()


expensive_items = """
SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
"""
print(expensive_items)

avg_hire_age = """
SELECT AVG( HireDate - BirthDate)
FROM Employee
"""
print(avg_hire_age)

ten_most_expensive = """
SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
FROM Product, Supplier
WHERE Product.SupplierId=Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10
"""
print(ten_most_expensive)

largest_category = """
SELECT Category.CategoryName,
COUNT(DISTINCT Product.Id)
FROM Category, Product
WHERE Category.Id = Product.CategoryId
GROUP BY 1 ORDER BY 2 DESC
LIMIT 1
"""
print(largest_category)

curs.close()

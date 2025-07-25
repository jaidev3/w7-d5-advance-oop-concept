class Product:
    def __init__(self, name, base_price, discount_percent, stock_quantity, category):
        self._name = name
        self._base_price = base_price
        self._discount_percent = discount_percent
        self._stock_quantity = stock_quantity
        self._category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if 3 <= len(value) <= 50 and all(c.isalnum() or c in ['-', ' '] for c in value):
            self._name = value
        else:
            raise ValueError("Name must be 3-50 characters, no special characters except hyphens and spaces")
        
    @property
    def base_price(self):
        return self._base_price
    
    @base_price.setter
    def base_price(self, value):
        if value > 0 and value <= 50000:
            self._base_price = value
        else:
            raise ValueError("Base price must be positive, maximum $50,000")
    
    @property
    def discount_percent(self):
        return self._discount_percent
    
    @discount_percent.setter
    def discount_percent(self, value):
        if 0 <= value <= 75:
            self._discount_percent = round(value, 2)
        else:
            raise ValueError("Discount percent must be 0-75%")
        
    @property
    def stock_quantity(self):
        return self._stock_quantity
    
    @stock_quantity.setter
    def stock_quantity(self, value):
        if value >= 0 and value <= 10000:
            self._stock_quantity = value
        else:
            raise ValueError("Stock quantity must be non-negative integer, maximum 10,000 units")
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if value in ['Electronics', 'Clothing', 'Books', 'Home', 'Sports']:
            self._category = value
        else:
            raise ValueError("Category must be from predefined list: ['Electronics', 'Clothing', 'Books', 'Home', 'Sports']")
        
    @property
    def final_price(self):
        return self._base_price * (1 - self._discount_percent / 100)
    
    @property
    def savings_amount(self):
        return self._base_price * self._discount_percent / 100
    
    @property
    def availability_status(self):
        if self._stock_quantity > 0:
            return "In Stock"
        elif self._stock_quantity > 10:
            return "Low Stock"
        else:
            return "Out of Stock"
        
    @property
    def product_summary(self):
        return f"Product: {self._name}\nBase Price: ${self._base_price:.2f}\nDiscount: {self._discount_percent:.2f}%\nFinal Price: ${self.final_price:.2f}\nSavings: ${self.savings_amount:.2f}\nStock: {self._stock_quantity} units\nCategory: {self._category}\nAvailability: {self.availability_status}"
    
    def __str__(self):
        return self.product_summary


# Test the Product class
product = Product("Laptop", 1000, 10, 5, "Electronics")
print(product)

product.name = "Smartphone"
product.base_price = 800
product.discount_percent = 15
product.stock_quantity = 15
product.category = "Electronics"
print(product)

product.discount_percent = 40
print(product)
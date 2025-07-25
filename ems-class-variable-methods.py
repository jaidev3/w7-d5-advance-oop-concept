from datetime import datetime, timedelta

class Employee:
    company_name = "Global Tech Solutions"
    total_employees = 0
    departments = {}
    tax_rates = {}
    next_employee_id = 1

    def __init__(self, name, dept, salary, country, email):
        self.employee_id = datetime.now().strftime("%Y%m%d%H%M%S") + str(Employee.next_employee_id)
        self.name = name
        self.department = dept
        self.base_salary = salary
        self.country = country
        self.hire_date = datetime.now()
        self.performance_ratings = []

    @staticmethod
    def validate_email(email):
        if "@" in email and "." in email.split("@")[1]:
            return True
        else:
            return False
        
    @staticmethod
    def calculate_tax(salary, country):
        if country in Employee.tax_rates:
            return salary * Employee.tax_rates[country]
        else:
            return 0
        
    @staticmethod
    def is_valid_department(dept):
        return dept in Employee.departments
    
    @classmethod
    def from_csv_data(cls, csv_line):
        name, dept, salary, country, email = csv_line.split(",")
        if cls.validate_email(email):
            return cls(name, dept, salary, country, email)
        else:
            raise ValueError("Invalid email format")
        
    @classmethod
    def get_department_stats(cls):
        return cls.departments
    
    @classmethod
    def set_tax_rate(cls, country, rate):
        cls.tax_rates[country] = rate
        
    @classmethod
    def hire_bulk_employees(cls, employee_list):
        for employee in employee_list:
            if cls.validate_email(employee.email):
                cls.total_employees += 1
                cls.departments[employee.department] = cls.departments.get(employee.department, 0) + 1
                cls.next_employee_id += 1
            else:
                raise ValueError("Invalid email format")

    def add_performance_rating(self, rating):
        if 1 <= rating <= 5:    
            self.performance_ratings.append(rating)
        else:
            raise ValueError("Performance rating must be between 1 and 5")
        
    def get_average_performance(self):
        if not self.performance_ratings:
            return 0
        else:
            return sum(self.performance_ratings) / len(self.performance_ratings)
        
    def calculate_net_salary(self):
        tax = self.calculate_tax(self.base_salary, self.country)
        return self.base_salary - tax
    
    def get_years_of_service(self):
        return (datetime.now() - self.hire_date).days // 365
    
    def is_eligible_for_bonus(self):
        return self.get_average_performance() > 3.5 and self.get_years_of_service() > 1
    
    def __str__(self):
        return f"Employee ID: {self.employee_id}\nName: {self.name}\nDepartment: {self.department}\nBase Salary: {self.base_salary}\nCountry: {self.country}\nHire Date: {self.hire_date}\nPerformance Ratings: {self.performance_ratings}\nAverage Performance: {self.get_average_performance()}\nNet Salary: {self.calculate_net_salary()}\nYears of Service: {self.get_years_of_service()}\nEligible for Bonus: {self.is_eligible_for_bonus()}"
    

# Test the Employee class
employee1 = Employee("John Doe", "IT", 50000, "US", "john.doe@example.com")
employee1.add_performance_rating(4)
employee1.add_performance_rating(5)
employee1.add_performance_rating(3)
print(employee1)
print(employee1.get_department_stats())
employee2 = Employee("Jane Smith", "HR", 45000, "UK", "jane.smith@example.com")
employee2.add_performance_rating(2)
employee2.add_performance_rating(3)
employee2.add_performance_rating(4)
print(employee2)
print(employee2.get_department_stats())






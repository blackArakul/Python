from employee.employee import Employee


class SalaryEmployee(Employee):
    """Административные работники, которые имеют фиксированную зарплату"""

    def __init__(self, code, name, weekly_salary):
        super().__init__(code, name,)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary



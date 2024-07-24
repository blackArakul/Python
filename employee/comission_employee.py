from employee.salary_employee import SalaryEmployee


class CommissionEmployee(SalaryEmployee):
    """Торговые представители, фиксированная зарплата + комиссия от продаж"""
    def __init__(self, code, name, hours_worked, commission):
        super().__init__(code, name, hours_worked)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission



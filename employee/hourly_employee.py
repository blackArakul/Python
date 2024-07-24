from employee.employee import Employee


class HourlyEmployee(Employee):
    """Рабочие, которые получают почасовую оплату"""
    def __init__(self, code, name, hours_worked, hour_rate):
        super().__init__(code, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate



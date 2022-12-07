"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salaryType, salary, hours = None, commissionType = None, commission = 0, commissionContracts = None):
        self.name = name
        self.salaryType = salaryType.lower()
        self.salary = salary
        self.hours = hours
        self.commissionType = None
        if commissionType:
            self.commissionType = commissionType.lower()
        self.commission = commission
        self.commissionContracts = commissionContracts
    def get_pay(self):
        if self.salaryType == "monthly":
            return self.salary + self.get_commission()
        else:
            return self.salary * self.hours + self.get_commission()
    def get_commission(self):
        if not self.commissionType: 
            return 0
        if self.commissionType == "bonus":
            return self.commission
        else:
            return self.commission * self.commissionContracts
    def __str__(self):
        string = f"{self.name} works on a "
         if self.salaryType == "monthly":
             string += f"{self.salaryType} salary of {self.salary}"
         else:
             string += f"{self.salaryType} of {self.hours} hours at {self.salary}/hour"

         if self.commissionType:
             string += f" and receives a "
             if self.commissionType == "bonus":
                 string += f"{self.commissionType} commission of {self.commission}"
             else:
                 string += f"commission for {self.commissionContracts} contract(s) at {self.commission}/contract"
         string += f". Their total pay is {self.get_pay()}."
         return string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')



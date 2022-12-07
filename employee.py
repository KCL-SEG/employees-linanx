"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, description ="", salary=0, commission=0):
        self.name = name
        self.description = description
        self.salary = salary
        self.commission = commission
    #salary is based on fixed monthly pay
    def contractBasedSalary(self, monthlyIncome):
        self.salary = monthlyIncome
        return
    #salary based on the how long they worked for * how much they get paid per hour
    def hourlyBasedSalary(self, hourlyIncome, hoursWorked):
        self.salary = hourlyIncome * hoursWorked
        return
    #commission based on fixed bonus received on top of salary
    def bonusBasedCommission(self, fixedBonusValue):
        self.commission = fixedBonusValue
        return
    #commission based on number of contracts landed * comission per contract
    def contractBasedCommission(self, commissionPerContract, numOfContractsLanded):
        self.commission= commissionPerContract * numOfContractsLanded
        return
    #description = information on how the payement was calaculated
    def outputPayInfo(self, description):
        self.description = description
        return
    def get_pay(self):
        totalpayement = self.salary + self.commission
        return totalpayement
    #outputs informaiton on how the payement was calculated
    def __str__(self):
        return self.description


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

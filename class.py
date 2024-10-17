#elso
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Kutya neve: {self.name}, életkora: {self.age} év")

#masodik
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} Ft befizetve. egyenleg: {self.balance} Ft")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} Ft felvéve. egyenleg: {self.balance} Ft")
        else:
            print("Nincs elég lóvé")

    def get_balance(self):
        return self.balance

#harmadikk
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        print(f"Jegy addolva: {grade}")

    def get_average(self):
        if len(self.grades) > 0:
            return sum(self.grades) / len(self.grades)
        else:
            return 0
'''
===========================================

== Written by... Fritzson Louis
== Date Written. Feb 26, 2023
== Purpose...... Chapter9-Classes101

===========================================
'''

class Date:
    def __init__(self, month, day, year):
        self._month = month
        self._day = day
        self._year = year

    def __str__(self):
        return f"{self._month}/{self._day}/{self._year}"

    def setMonth(self, month):
        self._month = month

    def setDay(self, day):
        self._day = day

    def setYear(self, year):
        self._year = year

    def getMonth(self):
        return self._month

    def getDay(self):
        return self._day

    def getYear(self):
        return self._year

    @staticmethod
    def isLeapYear(year):
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True

    def isValid(self):
        if self._month < 1 or self._month > 12:
            return False
        if self._day < 1 or self._day > 31:
            return False
        if self._month == 2:
            if self.isLeapYear(self._year):
                return self._day <= 29
            else:
                return self._day <= 28
        if self._month in [4, 6, 9, 11]:
            return self._day <= 30
        return True


def main():
    valid_date = False
    while not valid_date:
        month = int(input("Enter the month of your birthdate (1-12): "))
        day = int(input("Enter the day of your birthdate: "))
        year = int(input("Enter the year of your birthdate: "))
        date = Date(month, day, year)
        if date.isValid():
            print(f"Your birthdate is: {date}")
            valid_date = True
        else:
            print("Invalid date, please try again.")

# Example usage
date1 = Date(2, 29, 2020)
print(date1)  # prints "2/29/2020"
date1.setDay(28)
print(date1)  # prints "2/28/2020"
date2 = Date(13, 32, 2021)
print(date2.isValid())  # prints False
main()  # prompts the user for their birthdate and prints it

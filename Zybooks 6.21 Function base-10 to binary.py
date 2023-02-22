'''
===========================================

== Written by... Fritzson Louis
== Date Written. Feb 19, 2023
== Purpose...... LAB 6.21 Convert to Binary - Function

===========================================
'''


def main():
    done = False
    while not done:
        number = int(input("Enter a positive integer (or a negative integer to stop): "))
        if number < 0:
            done = True
        else:
            displayPrime(number)
            displayBinary(number)

def displayPrime(value):
    if value < 2:
        print("The value", value, "is not a prime number.")
        return

    isPrime = True
    i = 2
    while isPrime and i <= int(value ** 0.5):
        if value % i == 0:
            isPrime = False
        i += 1

    if isPrime:
        print("The value", value, "is a prime number.")
    else:
        print("The value", value, "is not a prime number.")

def displayBinary(value):
    if value == 0:
        print("The number 0 in binary is: 0")
        return

    binary = ""
    done = False
    while not done:
        binary = str(value % 2) + binary
        value //= 2
        if value == 0:
            done = True

    print("The number", value, "in binary is:", binary)

main()

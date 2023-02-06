'''

===========================================

== Written by... Fritzson Louis
== Date Written. Feb 05, 2023
== Purpose...... LAB 3.12: List Basics

===========================================

'''


def main():
    # Taking 3 flowers as input for myList
    myFlower1 = input("Enter first flower for myList: ")
    myFlower2 = input("Enter second flower for myList: ")
    myFlower3 = input("Enter third flower for myList: ")

    # Defining myList with the flowers
    myList = [myFlower1, myFlower2, myFlower3]

    # Taking 3 flowers as input for yourList
    yourFlower1 = input("Enter first flower for yourList: ")
    yourFlower2 = input("Enter second flower for yourList: ")
    yourFlower3 = input("Enter third flower for yourList: ")

    # Defining yourList with the flowers
    yourList = [yourFlower1, yourFlower2, yourFlower3]

    # Concatenating myList and yourList to form ourList
    ourList = myList + yourList

    # Taking another flower as input and appending to ourList
    theirFlower = input("Enter another flower: ")
    ourList.append(theirFlower)

    # Replacing second flower of ourList with "Purple Flower"
    ourList[1] = "Purple Flower"

    # Removing first flower from ourList
    ourList.remove(ourList[0])

    # Removing second element from ourList
    ourList.pop(1)

    # Displaying the 3 lists
    print("\nMy List:", myList)
    print("\nYour List:", yourList)
    print("\nOur List:", ourList)

main()

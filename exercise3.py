"""
10-6. Addition: One common problem when prompting for numerical input occurs
 when people provide text instead of numbers. When you try to convert the 
 input to an int, you’ll get a ValueError. 
 Write a program that prompts for two numbers. Add them together and print the result.
 Catch the ValueError if either input value is not a number, and print a friendly error 
message. 
Test your program by entering two numbers and then by entering some text instead of a number.
"""

def addition():
    print("Give me two numbers and I'll add them!")
    print("If you want to stop, just enter 'q'.")
    while True:
        first_num = input("Enter the first number: ")
        if first_num == 'q':
            break
        second_num = input("Enter a second number: ")
        if second_num == 'q':
            break
        try:
            sum = int(first_num) + int(second_num)
            print(f"\n\tThis is your result: {sum}\n")
        except ValueError:
            print("Please enter just numbers!")

addition()

"""
10-7. Addition Calculator: Wrap your code from 
Exercise 10-5 in a while loop so the user can 
continue entering numbers, even if they make a
 mistake and enter text instead of a number.
"""



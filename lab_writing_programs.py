"""CSC 161 Lab: Writing Programs

Lihang Liu
Lab Section CSC 161-2 TR 2:00-3:15pm
Spring 2022
"""


def main():
    print("This program helps you calculate the result of an expression.")
    loop = input("How many times should this program run: ")
    # This is the second credit
    for a in range(int(loop)):
        expression = input("Enter a mathematical expression: ")
        print(expression + " = " + str(eval(expression)))
        # This is the first credit pretty print


if __name__ == "__main__":
    main()
        
         
    

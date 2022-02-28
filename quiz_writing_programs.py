"""CSC 161 Quiz: Writing Programs

Lihang Liu
Lab Section TR 2:00-3:15pm
Spring 2022
"""


def main():
    kg = float(input("What is the mass of this object (in kg)? "))
    sp = float(input("What is the velocity of this object (in m/sec)? "))
    ke = float((kg * (sp ** 2)) / 2)
    print("The kinetic energy is: " + str(ke) + " Joules")


if __name__ == '__main__':
    main()

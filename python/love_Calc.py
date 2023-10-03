import random


def check(a):
    if a > 10:
        print("Greater than 10 ")
    else:
        print("Less than 10 :")


if __name__ == "__main__":
    name = input("Enter your Name\n")
    name_2 = input("Enter Your Partner Name\n")
    
    rando = random.randint(0, 100)
    print(name + " love " + name_2 + " " + str(rando) + " % ")
import random
while True:
    print("Welcome to Guessing Game")
    print("1.Guess from 1 to 10")
    print("2.Guess from 1 to 50")
    print("3.Guess from 1 to 100")
    print("4.Exit!!!")
    choice=int(input("Please Choose Any Options:"))
    if choice==1:
        print("Welcome to First Guessing Level 1:")
        print("Each Guess Cost 10$")
        while True:
            try: 
                chance=int(input("Enter Number of Round to Play:"))
                break
            except ValueError:
                print("Please Enter Digit Number!")
        for i in range(1,chance+1):
            print("Round",i)
            while True:
                try:
                    number1=int(input("Enter Your Guess Number:"))
                    break
                except ValueError:
                    print("Please Enter Digit Number!")
        number=random.randint(1,10) 
        if number1>number:
            print("The Number is Too high")
        if number==number1:
            print("Your Guess is correct")
        else:
            print("Your Guess is Incorrect!!!","\nCorrect Number is:",number) 
    elif choice==2:
        print("Welcome to Level of Guessing Game")
        print("Each Guess Cost 15$")
        while True:
                try:
                    chance=int(input("Enter Number of Round to Play:"))
                    break
                except ValueError:
                    print("Please Enter Number of Round to Play! ")
        for i in range(1,chance+1):
            print("Round",i)
            while True:
                    try:                      
                        number2=int(input("Enter Your Guess Number:"))
                        break
                    except ValueError:
                        print("Please Enter Digit Number!")
                        number=random.randint(1,50)
                    if number2>number:
                        print("The Number is too High")
                    if number==number2:
                        print("Your Guess is correct")
        else:
            print("Your Guess is Incorrect!!!","\nCorrect Number is:",number) 
    elif choice==3:
                        print("Welcome to Level of Guessing Game")
                        print("Each Guess Cost 20$")
                        while True: 
                            try:                           
                                chance=int(input("Enter Number of Round to Play:"))
                                break
                            except ValueError: 
                                print("Please Enter Number of Round to Play!!!")
                        for i in range(1,chance+1):
                            print("Round",i) 
                            while True:
                                try:
                                    number3=int(input("Enter Your Guess Number:"))
                                    break
                                except ValueError:
                                    print("Please Enter Digit Number!!!")                                              
                            number=random.randint(1,100)
                            if number==number3:
                                print("Your Guess is correct")
                            else:
                                print("Your Guess is Incorrect!!!","\nCorrect Number is:",number) 
    elif choice==4:
        print("Thank You For Playing")
        break
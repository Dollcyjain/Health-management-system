def program():
    def getdate():
        import datetime
        return datetime.datetime.now()

    def ask1():
        print("What you want to log?\n1. Diet\n2. Exercise")

    def ask2():
        print("What you want to retrieve?\n1. Diet\n2. Exercise")

    print("Welcome to Health Management System\nWhat you want to do?")
    print("1. Log")
    print("2. Retrieve")
    ans = int(input())
    if ans == 1:
        print("What is name of the client?")
        client = input()
        ask1()
        activity = int(input())
        if activity == 1:
            with open("diet.txt", "a") as f:
                log = input("Write whatever you want to log\n")
                f.write("["+str(getdate())+"] "+log+"\n")
            print(f"You have successfully logged to diet, {client}")
        else:
            with open("exer.txt", "a") as f:
                log = input("Write whatever you want to log\n")
                f.write("["+str(getdate())+"] "+log+"\n")
            print(f"You have successfully logged to exercise, {client}")
    else:
        print("What is name of the client?")
        client = input()
        ask2()
        activity = int(input())
        if activity == 1:
            with open("diet.txt") as f:
                print(f.read())
            print(f"You have successfully retrieved to diet, {client}")
        else:
            with open("exer.txt") as f:
                print(f.read())
            print(f"You have successfully retrieved to exercise, {client}")
    print("\nWant to log or retrieve again? Press 'y' for yes and 'n' for no")
    yesno = input()
    if yesno == 'y':
        program()
    else:
        print("Thank You!!")


program()

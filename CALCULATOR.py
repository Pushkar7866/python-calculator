while True:
    print("\n=======================================")
    print("|  <WEJCOME TO MY PYTHON CALCULATOR>  |")
    print("=======================================")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("5. SQUARE")
    print("6. CUBE")
    print("7. FACTORIAL")
    print("8. FACTORS OF A NUMBER")
    print("9. EXIT")
    print("=================================")
    
    choice=int(input("CHOOSE AN OPTION (1-9):"))
    if choice==9:
        print("\n================================")
        print("  <CALCULATOR IS BEING CLOSED>")
        print("<THANKS FOR USING MY CALCULATOR>")
        print("================================")
        break

    if choice==7:
        num=int(input("Enter the number:"))
        fact=1
        for i in range(1,num+1):
            fact=fact*i
        print("FACTORIAL OF",num,"is",fact,)

    elif choice==8:
        num=int(input("Enter the Number:"))
        for i in range(1,num+1):
            if num%i==0:
             print("FACTOR OF",num,"is",i,) 

    elif choice==5:
        num=int(input("Enter the Number:"))
        print("RESULT=",num*num)

    elif choice==6:
        num=int(input("Enter the Number:"))
        print("RESULT=",num*num*num)
    
    else:
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        if choice==1:
            print("RESULT",num1+num2)
        elif choice==2:
            print("RESULT",num1-num2)

        elif choice==3:
            print("RESULT",num1*num2)

        elif choice==4:
            print("RESULT",num1/num2)

        else:
            print("INVALID CHOICE ENTERED")


        




print("Welcome to Calculator!")
print("What do you want to do?")
print("1. Addition  2. Subtraction\n3. Multiply  4. Division")
print("5. Factorial 6. Exponent\n7. Remainder 8. Roots")
choice=[1,2,3,4,5,6,7,8]
while True:
 ch=int(input("Enter your choice OR press zero to exit"))
 if ch in choice:
    match ch:
        case 1:
            print("Enter the numbers")
            a=int(input())
            b=int(input())
            c=lambda a,b:a+b
            print(f"Sum is {c(a,b)}")
        
        case 2:
            print("Enter the numbers")
            a=int(input())
            b=int(input())
            c=lambda a,b:a-b
            print(f"Difference is {c(a,b)}")

        case 3:
            print("Enter the numbers")
            a=int(input())
            b=int(input())
            c=lambda a,b:a*b
            print(f"product is {c(a,b)}")        

        case 4:
            print("Enter the numbers")
            a=int(input())
            b=int(input())
            c=lambda a,b:a/b
            print(f"Division is {c(a,b)}")

        case 5:
            print("Enter the number")
            a=int(input())
            c=1
            for i in range(1,a+1):
                c=c*i
            print(f"Factorial is {c}")

        case 6:
            a=int(input("Enter base->"))
            b=int(input("Enter exponent->"))
            c=lambda a,b:a**b
            print(f"Result of exponent is {c(a,b)}")

        case 7:
            print("Enter the numbers")
            a=int(input())
            b=int(input())
            c=lambda a,b:a%b
            print(f"Remainder is {c(a,b)}")

        case 8:
            print("Enter the numbers")
            a=int(input())
            b=int(input())
            c=lambda a,b:a**(1.0/b)
            print(f"Root is {c(a,b)}")
 elif ch==0:
     print("Exit successful!")
     break   
 else:
    print("Entered wrong choice")

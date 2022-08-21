ans = 0
print(ans)
while True:
 
    opreation_choices=['+','-','*','/']
    
    operation=input("enter your choice (+,-,*,/  or enter q to quit) ")
    
    if operation=="q":
        quit()

    elif operation not in opreation_choices:
        print("enter a valid choice, Try Again !")
        continue

    else:
        try:
            digit=int(input("enter the digit "))
        except:
            print("enter a numeric value only")
            continue
        else:
            if operation=="+":
                ans=ans+digit
                print(ans)

            elif operation=="-":
                ans=ans-digit
                print(ans)
                        
            elif operation=="*":
                ans=ans*digit
                print(ans)
            else:
                try:
                    if operation=="/":
                        ans=ans/digit
                        print(ans)
                except:
                    print("a number can't be divisible by 0 ")
                    continue

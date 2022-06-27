#pattern printting 

True 
"""
*
**
***
****
"""
False
"""
****
***
**
*
"""

num = int(input("Enter the no. of line in star pattern : "))

choose = int(input("Enter the type of pattern in 1 or 0 : "))
mark = bool(choose)
if mark == True :
    print("True")
    for i in range(1, num+1) :
        for j in range(1,i+1) :
            print("*", end="")
        print()
else :
    print("False")
    for i in range(1, num+1) :
        for j in range(1,(num+2-i)) :
            print("*", end="")
        print()


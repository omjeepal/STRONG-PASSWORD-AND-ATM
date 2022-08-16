a=int(input(":"))
b=int(inputssss



pass1=input("Enter the password: ")
if len(pass1)<=8:
    if((("A" in pass1) or ("B" in pass1) or ("C" in pass1) or ("D" in pass1) or ("E" in pass1) or ("F" in pass1) or ("G" in pass1) or ("H" in pass1) or ("I" in pass1) or ("J" in pass1) or ("K" in pass1) or ("M" in pass1) or ("N" in pass1) or ("O" in pass1) or ("P" in pass1) or ("Q" in pass1) or ("R" in pass1) or ("S" in pass1) or ("T" in pass1) or ("U" in pass1) or ("V" in pass1) or ("W" in pass1) or ("X" in pass1) or ("Y" in pass1) or ("Z" in pass1)) and (("a" in pass1) or ("b" in pass1) or ("c" in pass1) or ("e" in pass1) or ("f" in pass1) or ("g" in pass1) or ("h" in pass1) or ("i" in pass1) or ("j" in pass1) or ("k" in pass1) or ("m" in pass1) or ("n" in pass1) or ("o" in pass1) or ("p" in pass1) or ("q" in pass1) or ("r" in pass1) or ("s" in pass1) or ("t" in pass1) or ("u" in pass1) or ("v" in pass1) or ("w" in pass1) or ("x" in pass1) or ("y" in pass1) or ("z" in pass1)) and (("1" in pass1) or ("2" in pass1) or ("3" in pass1) or ("4" in pass1) or ("5" in pass1) or ("6" in pass1) or ("7" in pass1) or ("8" in pass1) or ("9" in pass1) or ("0" in pass1)) and (("@" in pass1) or ("#" in pass1) or ("₹" in pass1) or ("&" in pass1) or ("_" in pass1) or ("-" in pass1) or ("+" in pass1) or ("()" in pass1) or ("*" in pass1) or("/" in pass1) or ("!" in pass1) or ("?" in pass1))):
        print("corret password")
    else:
        print("wrong_password")
else:
    print("worng password :- ")


pass1=input("Enter the password...")
if len(pass1)<=8:
              if("A" or "B" or "C" or "D" or "E" or "F" or "G" or "H" or "I" or "J" or "K" or "M" or "N" or "O" or "P" or "Q" or "R" or "S" or "T" or "U" or "V" or "W" or "X" or "Y" or "Z" in pass1) and ("a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m" or "n" or "o" or "p" or "q" or "r" or "s" or "t" or "u" or "v" or "w" or "x" or "y" or "z" in pass1) and("1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0" in pass1) and ("@" or "#" or "₹" or "_" or "&" or "-" or  "+" or "(" or ")" or "/" or "*" in pass1):
                  print("correct passwaord")
              else:
                    print("wrong password")
else:
        
        
                       print("worng password")

  
  
print("              welcome to ATM machine")
pin=int(input("Enter your 4 digit pin number: "))
AMT= 150000
if pin == 1111:
    print("1.Withdraw\n2.Balance Enquiry\n3.frist cash\n4.Deposit")
    choice=int(input("please choose transactions: "))
    if (choice==1):
        w=int(input("Enter withdraw amount: "))
        print("after withdrawl your amount is :-",AMT-w)
        if (w < AMT and w % 150 == 0):
            print("please take your amount:",w)
        else:
            print("Your available ammount is ",AMT-w)
    elif(choice==2):
        print("your avilable amount:",AMT)
    elif (choice ==3):
        print("1.->20000\n2.->50000\n3.70000\n4.->90000\n5.->100000\n6.->150000\n")
        op=int(input("ENTER FAST CASH OPTION: "))
        if (op==1 and 20000<=AMT):
            print("plaese take your cash: ")
        elif (op==2 and 50000<=AMT):
            print("please take your cash: ")
        elif (op==3 and 70000<=AMT):
            print("please take your cash: ")
        elif (op==4 and 90000<=AMT):
            print("please take your cash:")
        elif (op==5 and 100000<=AMT):
            print("please take your cash: ")
        elif (op==6 and 150000<=AMT):
            print("please take your cash: ")
    elif (choice==4):
        print("please deposit your amount: ")
        dp=int(input("ENTER YOUR  DEPOSIT AMOUNT  "))
        AMT+=dp
        print(AMT)      
    else:
        print("you have selected wrong option!")
else:
    print("You have entered wrong pin!")

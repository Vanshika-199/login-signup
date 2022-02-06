import json

print("WELCOME")
print("LOGIN OR SIGN UP\nPress 1 for SIGN UP and 2 for LOGIN:")
response=int(input("Enter your response:- "))
if response==1:
    print("WELCOME TO SIGN UP")
    username=input("Enter your username:- ")
    password1 = input("enter the  password:- ")
    if ('a' in password1  or 'b' in password1  or 'c' in password1 or 'd' in password1 or 'e' in password1 or 'f' in password1 or 'g' in password1 or 'h' in password1 or 'i' in password1 or 'j' in password1 or 'k' in password1 or 'l' in password1 or 'm' in password1 or 'n' in password1 or 'o' in password1 or 'p' in password1 or 'q' in password1 or 'r' in password1 or 's' in password1 or 't' in password1 or 'u' in password1 or 'v' in password1 or 'w' in password1 or 'password1' in password1 or 'y' in password1 or 'z' in password1 ) and ('A' in password1 or 'B' in password1 or 'C' in password1 or 'D' in password1 or 'E' in password1 or 'F' in password1 or 'G' in password1 or 'H' in password1 or 'I' in password1 or 'J' in password1 or 'K' in password1 or 'L' in password1 or 'M' in password1 or 'N' in password1 or 'O ' in password1 or 'P' in password1 or 'Q' in password1 or 'R' in password1 or 'S' in password1 or 'T' in password1  or 'U' in password1 or 'V' in password1 or 'W' in password1 or 'password1' in password1 or 'Y' in password1 or 'Z'in password1) and ('0'  in password1 or '1' in password1 or '2' in password1 or '3'in password1 or '4' in password1 or '5' in password1 or  '6' in password1 or '7' in password1 or '8' in password1 or '9' in password1) and ('@'in password1 or '#'in password1 or '$'in password1):
        print("Confirm your password")
    else:
        print("Atleast password should contain one special character and one number")
    password2=input("Enter your password to confirm:- ")
    if password1==password2:
        print("YOU ARE SIGNED UP SUCCESSFULLY",username)
    else:
        print("Both the password is different")
file="userdetails.json"
if response==2:
    print("LOGIN TO YOUR ACCOUNT")
    username=input("Enter your username:- ")
    password1 = input("enter the  password:")
    if ('a' in password1  or 'b' in password1  or 'c' in password1 or 'd' in password1 or 'e' in password1 or 'f' in password1 or 'g' in password1 or 'h' in password1 or 'i' in password1 or 'j' in password1 or 'k' in password1 or 'l' in password1 or 'm' in password1 or 'n' in password1 or 'o' in password1 or 'p' in password1 or 'q' in password1 or 'r' in password1 or 's' in password1 or 't' in password1 or 'u' in password1 or 'v' in password1 or 'w' in password1 or 'password1' in password1 or 'y' in password1 or 'z' in password1 ) and ('A' in password1 or 'B' in password1 or 'C' in password1 or 'D' in password1 or 'E' in password1 or 'F' in password1 or 'G' in password1 or 'H' in password1 or 'I' in password1 or 'J' in password1 or 'K' in password1 or 'L' in password1 or 'M' in password1 or 'N' in password1 or 'O ' in password1 or 'P' in password1 or 'Q' in password1 or 'R' in password1 or 'S' in password1 or 'T' in password1  or 'U' in password1 or 'V' in password1 or 'W' in password1 or 'password1' in password1 or 'Y' in password1 or 'Z'in password1) and ('0'  in password1 or '1' in password1 or '2' in password1 or '3'in password1 or '4' in password1 or '5' in password1 or  '6' in password1 or '7' in password1 or '8' in password1 or '9' in password1) and ('@'in password1 or '#'in password1 or '$'in password1):
        print("Re-enter your password")
    else:
        print(" invalid password")
    password2=input("re-enter your password:- ")
    if password1==password2:
        if username in file:
            print("Invalid username and password")
        else:
            print("YOU ARE LOGGED IN SUCCESSFULLY",username)
details={"username":username,"password1":password1,"password2":password2}
with open("userdetails.json","w") as file_object:
    json.dump(details,file_object,indent=4)
    if username in file:
        print("Username already exist")
    else:
        print("THANK YOU")
def get_inputs():
    name = input("Enter your username:- ")
    d =  {}
    d['date'] = input('Enter a date of birth in (06.08.1999) format:')
    d['hobbies'] = input("Enter your Hobbies:- ")
    d['gender'] = input("Enter your gender:- ")
    return(name,d)
out = {}
while True:
    exit = input('Do you want to add your details (y/n)? ')
    if exit.lower() == 'n':
        break
    else:
        name, d = get_inputs()
        out[name] = d
with open('names.json','w') as f:
    json.dump(out, f, indent=2)

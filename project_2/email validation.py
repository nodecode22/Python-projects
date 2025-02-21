# program to check the validation of an email
#taking input of the email
email=input("Enter an email ID:")
x=len(email)
if x>=6:
    if email[0].isalpha()==True:
        if ("@" in email and email.count("@")==1):
            if email[-4:x]==".com" or email[-3:x]==".in":
                for i in email:
                    if i.isspace()==True:
                        print("Invalid email 1!!")
                    elif i.islower()==True or i.isdigit()==True:
                        continue
                    elif i=="_" or i=="@" or i==".":
                        continue
                    else:
                        print("## UNEXPECTED ERROR ##")
                print(email,"is in the correct format of the email")
            else:
                print("ERROR 4")

        else:
            print("ERROR 3")
    else:
        print("ERROR 2")
else:
    print("ERROR 1")


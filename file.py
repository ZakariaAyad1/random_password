from random import choice

length_pswd=int(input("welcome to our service, enter length of the password : "))

def pswd(length_pswd):
    password= " "
    all_ltrs = input ("Excuse me, your password must includes : ")
    #length_pswd=int(input("enter length of the password : "))
    #all_ltrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    for i in range(length_pswd) :
        password = password + choice(all_ltrs)
    return password
    
print("welcome to our service, your password is :", pswd(length_pswd))
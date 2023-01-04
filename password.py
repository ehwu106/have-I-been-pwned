import random
import requests
import hashlib

def random_password():
    length = int(input("Enter your desired length of password: "))
    pwd =""
    for _ in range(length):
        pwd+=chr(random.randint(33,126))        
    print("Your generated password: "+str(pwd))
    return

def check_password_breach():
    pwd = input("Enter your password: ")
    hash_pwd = ((hashlib.sha1(pwd.encode())).hexdigest()).upper()
    response = requests.get(f"https://api.pwnedpasswords.com/range/{hash_pwd[:5]}")        
    if response.status_code !=200:
        print("unable to make the request")
        return
    for password in response.text.split("\n"):                                             
        hashed_val, num_breaches = password.split(":")
        if hashed_val==hash_pwd[5:]:
            print("Your password is not secure. Number of breaches: "+str(num_breaches))
            return
    print("Your password has not been breached")
    return

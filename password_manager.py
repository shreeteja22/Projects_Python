from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)'''
def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password ? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)


def view():

    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print("Username : ",user ,"\nPassword : ", fer.decrypt(passw.encode()).decode() + "\n")

def add():
    name = input("Enter username : ")
    pwd = input("Enter password : ")

    with open('passwords.txt','a') as f:
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("would you like to add password or view existing passwords (view,add) & press Q to quit the program ! ").strip().lower()
    if mode == "q":
        quit()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else :
        print("Invalid input!")    
        continue

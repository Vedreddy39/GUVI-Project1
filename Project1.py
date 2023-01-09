def login(name, password):
    success = False
    file = open("login_details.txt", "r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if (a==name and b==password):
            success = True
            break
    file.close()
    if(success):
        print("Login Successful!")
    else:
        print("Wrong details", ", Try Again")
        begin()
        access(option)

def register(name, password):
    file = open("login_details.txt","a")
    file.write("\n" +name+","+password)
    file.close()
    print("Registered Successfully")

def forget_password():
    success = False
    file = open("login_details.txt", "r")
    name = input("Enter your Email id to retrieve the password: ")
    for i in file:
        x,y = i.split(",")
        y = y.strip()
        if (x==name):
            success = True
            break
    file.close()
    if success:
        print("Your Password is: ", y)
        begin()
        access(option)
    else:
        print("Wrong Email id")
        forget_password()

def begin():
    global option
    print("Welcome")
    option = input("Login or Register or Forgot Password (login or register or forgot password): ")
    if option!= "login" and option!= "register" and option!= "forgot password":
        begin()

begin()

def access(option):
    if option== 'login':
        name = input("Enter Email id: ")
        password = input("Enter Password: ")
        login(name, password)
    elif option == "register":
        print("Enter Email id and Password to Register")
        name = input("Enter Email id: ")
        password = input("Enter Password: ")
        if password_check(password):
            register(name, password)
        else:
            access(option)
    else:
        forget_password()


def password_check(password):
    SpecialSym = ['$', '@', '#', '%']
    val = True
    if len(password) < 5:
        print('length should be at least 6')
        val = False
    if len(password) >16 :
        print('length should be not be greater than 15')
        val = False
    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        val = False
    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        val = False
    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        val = False
    if not any(char in SpecialSym for char in password):
        print('Password should have at least one of the symbols $@#%')
        val = False
    if val:
        return val

access(option)



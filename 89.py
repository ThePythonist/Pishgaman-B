def sign_up():
    username = input("Username : ").casefold() # .lower()
    password = input("Password : ")
    f = open("DB-USERS.txt","a").write(username+"\n")
    f2 = open("DB-PASSWORDS.txt","a").write(password+"\n")
    print("Sabtnam ba movafaqiat anjam shod")

def sign_in():
    users = []
    passwords = []
    db_users = open("DB-USERS.txt").readlines()
    db_passwords = open("DB-PASSWORDS.txt").readlines()

    for user in db_users :
        # users.append(user[0:-1])
        users.append(user.rstrip())

    for password in db_passwords :
        # users.append(password[0:-1])
        passwords.append(password.rstrip())

    accounts = dict(zip(users,passwords))
    # print(accounts)

    entry_user = input("Username : ").casefold()

    if entry_user in accounts :
        password = input("Password : ")
        if password == accounts[entry_user] :
            print("Vorod ba movafaqiat anjam shod")
        else :
            print("Password eshtebah ast")
            sign_in()
    else :
        print("Username eshtebah ast")
        sign_in()

choice = input("1 : Sabtnam , 2 : Vorod : ")


if choice == "1" :
    sign_up()
elif choice == "2" :
    sign_in()
else :
    print("Adad entekhab shode eshtebah ast")

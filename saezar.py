# Alphabet and Special characters
alphabet = "abcdefghijklmnopqrstuvwxyz"
ell = "~`!@#$%^&*)(_+-=][:;<>?,.\|/\"'"

# De/En cryption function
def password_gen(p,b) :
    global alphabet
    p = p.lower().strip() # Summerizing
    for i in p :
        if i.isnumeric() or i in ell or i == " ": p = p.replace(i,"")
        # Replacing
        p = p.replace(i,alphabet[(alphabet.find(i)+4) % 26]) if b == True else p.replace(i,alphabet[(alphabet.find(i)-4) % 26])
    return p

# True -> Encryotion , False -> Decryption
def main():
    while True :
        menu = input("1.Encryption\t2.Decryption\t3.Quit\n")
        if menu.isnumeric() :
            if menu == "3" : break
            if menu == "1" :
                password = input("\nEnter your password for Encryption : ")
                print(f"\n~ Your New password is\n- {password_gen(password,True)}\n")
            elif menu == "2" :
                password = input("\nEnter your password for Decryption : ")
                print(f"~ Your Old password is\n- {password_gen(password,False)}")
            else :
                print("\n>> Error : Check your input !\n")
        else :
            print("\n>> Error : Enter valid option number !\n")


if __name__ == "__main__" :
    main()
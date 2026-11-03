alphabet = "abcdefghijklmnopqrstuvwxyz"

def saezar(p,b) :
    return "".join(alphabet[(alphabet.find(i) + 3) % 26] if i in alphabet else i for i in p) if b == True else "".join(alphabet[(alphabet.find(i) - 3) % 26] if i in alphabet else i for i in p)

def main() :
    while True :
        menu = input("1.Encode\t2.Decode\t3.Quit\n")
        if menu.isnumeric() :
            if menu == "1" :
                password = input("\nEnter text for encoding : ")
                print("\nYour Encoded text is\n-",saezar(password.replace(" ","").lower(),True),"\n")
            elif menu == "2" :
                password = input("\nEnter text for decoding : ")
                print("\nYour Decoded text is\n-",saezar(password.replace(" ","").lower(),False),"\n")
            elif menu == "3" : break
            else :
                print("\n>> Error : Enter number between 1-3 !\n")
        else :
            print("\n>> Enter Valid Input !\n")

if __name__ == "__main__" :
    main()
    print("\n>> Thanks for choosing us ;)\n")
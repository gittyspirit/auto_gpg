#GPG is so complicated,so I want to make it easier
import os
while True:
    q1 = input("Have you generated a key before?(Y/n/q)") #q for quit
    if q1 == "n" or q1 == "N":
        comm = "gpg --full-generate-key"
        os.system(comm)
    elif q1 == "Y" or q1 == "y":
        email = input("Enter your email address or the public that you gonna use:")
        file = input("Which file do you want to treat?")
        query = input("What do you want to do next?[signature(s)/encrypt(en)/import(im)/decrypt(d)/revoke(r)/upload(u)/show pub key(sp)/fingerprint(f)/search key on the server(sk)/refresh the key(rk)")
        if query == "en":
            comm1 = "gpg --encrypt --sign --armor -r " + email + " " + file
            os.system(comm1)
        elif query == 's':
            comm2 = "gpg --sign-key " + email + " " + file
            os.system(comm2)
        elif query == "im":
            comm3 = "gpg --import " + file
            os.system(comm3)
        elif query == 'd':
            comm4 = "gpg --decrypt " + file + " > plain.txt"
            os.system(comm4)
        elif query == 'r':
            comm4 = "gpg --output ~/revocation.crt --gen-revoke " + email
            os.system(comm4)
        elif query == 'u':
            url = input("Enter the key server:")
            fin = input("Enter your fingerprint here:")
            comm5 = "gpg --send-keys --keyserver " + url + " " + fin
            os.system(comm5)
        elif query == "sp":
            comm6 = "gpg --output ~/dave-geek.key --armor --export " + email
            os.system(comm6)
        elif query == "sk":
            url1 = input("Enter the key server:")
            comm7 = "gpg --keyserver " +  " --search-keys " + email
            os.system(comm7)
        elif query == "rk":
            url2 = input("Enter the site server:")
            comm8 = "gpg --keyserver " + url2 + " --refresh-keys " + email
            os.system(comm8)
        else:
            print("Error!")
    else:
        break
        
           

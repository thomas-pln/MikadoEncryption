def main():
    for i in range(3):
        choice = (input("-> Encrypt : 0 | Decrypt : 1 => "))
        if(choice=='1' or choice=='0'):
            choice = (int)(choice)
            break
    if(choice == 0):
        print("***Encryption***\n")
        key = input("---Key : ")
        msg = input("---Message : ")
        msg = encrypt(msg, key)
        print("\n",msg)
    elif(choice == 1):
        print("***Decryption***\n")
        key = input("---Key : ")
        msg = input("---Message : ")
        msg = decrypt(msg, key)
        print("\n",msg)


def encrypt(clearMessage, encryptkey):
    lm = list(clearMessage)
    lk = list(encryptkey)
    lmk = [None]*len(lm)

    i = 0
    j = 0
    while (i< len(lm)):
        if (j == len(lk)):
            j=0

        msg = ord(lm[i])
        key = ord(lk[j])

        hash = msg - key

        if(hash < 0):
            hash = chr(hash + 91)
        elif (hash<65):
            hash = chr(hash+65)
        else:
            hash = chr(hash)

        lmk[i]=hash
        i +=1
        j +=1

    messageEncrypt = "".join(lmk)


    return messageEncrypt



def decrypt(hashMessage, encryptkey):
    lmk = list(hashMessage)
    lk = list(encryptkey)
    lm = [None]*len(lmk)

    i = 0
    j = 0
    while (i< len(lmk)):
        if (j == len(lk)):
            j=0

        msg = ord(lmk[i])
        key = ord(lk[j])

        hash = msg + key

        if((hash-65)<90 and (hash-65)>=65 ):
            hash = chr(hash-65)
        elif ((hash-65)>90):
            hash = chr(hash-91)

        if(type(hash)==int):
            hash = " "
        lm[i]=hash
        i +=1
        j +=1

    leMessage = "".join(lm)

    return leMessage


if __name__ == '__main__':
    main()

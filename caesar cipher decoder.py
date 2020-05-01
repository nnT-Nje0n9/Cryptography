#Caesar Cipher Decoder

cipher = input("Input The Cipher : ")

cipher_list = list(cipher)

'''
ord(a) = 97 ord(z) = 122
ord(A) = 65 ord(Z) = 90
ord('0') = 48 ord('9') = 57
'''


for i in range(1,26):
    print("move [",i,"] : ",end = '')
    for j in cipher_list:
        if((ord(j) >= 65 and ord(j) <=90) or (ord(j) >= 97 and ord(j)<=122)): #English
            if((ord(j)+i > 90 and ord(j)+i < 97) or ord(j)+i > 122): #over
                print(chr(ord(j)+i-26),end='')
            else :
                print(chr(ord(j)+i),end='')
        else :    
            print(j,end = '')
    print()

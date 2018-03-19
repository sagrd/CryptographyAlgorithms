import sys

def encrypt(msg, key):
    #Convert  list(msg) to list of numbers
    num_msg = []
    key_list = []

    for i in msg:
        num_msg.append(alpha_num(i)) 
    for i in key:
        key_list.append(alpha_num(i))


    enc_list = []
    len_key = len(key_list)
    for i in range(0, len(num_msg)):
        if (i<len_key):
            num = (num_msg[i] + key_list[i]) % 26

        else:
            num = (num_msg[i] + key_list[i % len_key]) % 26

        enc_list.append(alpha_num(num))

    print(enc_list)

def decrypt(msg, key):
    #Convert  list(msg) to list of numbers
    num_msg = []
    key_list = []

    for i in msg:
        num_msg.append(alpha_num(i)) 
    for i in key:
        key_list.append(alpha_num(i))


    enc_list = []
    len_key = len(key_list)
    for i in range(0, len(num_msg)):
        if (i<len_key):
            num = (num_msg[i] - key_list[i]) % 26

        else:
            num = (num_msg[i] - key_list[i % len_key]) % 26

        enc_list.append(alpha_num(num))

    print(enc_list)

def alpha_num(arg):
    '''
    convert alphabet to their corresponding numeric values
    '''

    alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    num = list(range(0,26))

    if isinstance(arg, str):
        ind = alpha.index(arg)
        return num[ind]

    else:
        ind = num.index(arg)
        return alpha[ind]
        

def main():
    method = sys.argv[1]
    key = sys.argv[2]
    key = list(key.upper())

    # print [ord(char) - 96 for char in raw_input('Write Text: ').lower()]
    msg = input("Enter the message: ")
    msg = list(msg.upper())
    print(msg)
    
    if method == "enc":
        encrypt(msg, key)
    elif method == "dec":
        decrypt(msg, key)

if __name__ == "__main__":
    main()

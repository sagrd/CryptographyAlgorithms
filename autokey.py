ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    message = input('enter message: ')
    key = input('enter your key: ')
    mode = input('encrypt or decrypt: ')


    if mode == 'encrypt':
       cipher = cipherMessage(message, key, 'encrypt')
    elif mode == 'decrypt':
       cipher = cipherMessage(message, key, 'decrypt')

    print(cipher)



def cipherMessage (messages, keys, mode):
    cipher = []
    k_index = 0
    key = keys.upper()
    for i in messages:
        text = ALPHA.find(i.upper())
        ## if text != -1:
        if mode == 'encrypt':
             text += ALPHA.find(key[k_index])
             key += i.upper()  # add current char to keystream

        elif mode == 'decrypt':
             text -= ALPHA.find(key[k_index])
             key += ALPHA[text]  # add current char to keystream
        text %= len(ALPHA)
        k_index += 1
        cipher.append(ALPHA[text])
    return ''.join(cipher)

if __name__ == "__main__":
    main()
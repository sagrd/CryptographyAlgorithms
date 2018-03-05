import sys

def main():
    dict = {}   
    alpha=['a','b','c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    method = sys.argv[1]

    key=str(input("Enter the 26 lettered key:"))
    key = list(key) # key  qwertyuiopasdfghjklzxcvbnm

    for i in range(len(alpha)):
        dict[alpha[i]] = key[i]

    c_text=str(input("Enter the plain text:"))
    c_text = list(c_text)
    
    if method == "enc":
	    for i in range(len(c_text)):
	        c_text[i] = dict[c_text[i]]
    else:
	    for i in range(len(c_text)):
	    	#retriving keys from values
	    	c_text[i] = list(dict.keys())[list(dict.values()).index(c_text[i])]

    c_text = "".join(c_text)
    print(c_text)

if __name__ == "__main__":
    main()



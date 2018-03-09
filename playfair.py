import sys

def index_2d(thelist,v):
	''' 
	return index of value in 2d list in form of tuples(col,row)
	'''
	for i, x in enumerate(thelist):
		if v in x:
			itup = [i, x.index(v)]
			return itup


def preparing_message(message):
	'''
	takes a string, strips spaces, splits message in pairs

	Must be split into pairs
	Remove all duplicate letters by inserting letter X
	if there is an odd letter at the end of message, insert letter X
	'''
	message = list(message.strip())
	message_pairs = []
	for i in range(0, len(message)):
		if(i%2 == 0 ):
			if (message[i] != message[i+1]):
				temp_tuples = [message[i], message[i+1]]
				message_pairs.append(temp_tuples)

			else:
				message.insert(i+1,"x")
				temp_tuples = [message[i], message[i+1]]
				message_pairs.append(temp_tuples)

	if(len(message)%2 == 1):
		temp_tuples = [message[-1], "x"]
		message_pairs.append(temp_tuples)

	print(message_pairs)
	return message_pairs

def playfair_enc(tuples_message, table):
	for pair in tuples_message:

		# for 2d matirx
		index_first = index_2d(table, pair[0])
		index_sec = index_2d(table, pair[1])

		# for same row
		if(index_first[0] == index_sec[0]):
			index_first[1] = (index_first[1] + 1) % 5
			index_sec[1] = (index_sec[1] +1) % 5

		#for same column
		elif(index_first[1] == index_sec[1]):
			index_first[0] = (index_first[0] + 1) % 5
			index_sec[0] = (index_sec[0] +1) % 5

		# for none 
		else:
			''' swap the letters with the ons on the end of rectangle'''
			temp = index_first[:]
			index_first[1] = index_sec[1]
			index_sec[1] = temp[1]

		#assigning value of index in pair
		pair[0] = table[index_first[0]][index_first[1]]
		pair[1] = table[index_sec[0]][index_sec[1]]
	print(tuples_message)
	return tuples_message


def playfair_dec(tuples_message, table):


	for pair in tuples_message:

		# for 2d matirx
		index_first = index_2d(table, pair[0])
		index_sec = index_2d(table, pair[1])

		# for same row
		if(index_first[0] == index_sec[0]):
			index_first[1] = (index_first[1] - 1) % 5
			index_sec[1] = (index_sec[1] - 1) % 5

		#for same column
		elif(index_first[1] == index_sec[1]):
			index_first[0] = ((index_first[0] - 1)) % 5
			index_sec[0] = (index_sec[0] - 1) % 5

		# for none 
		else:
			''' swap the letters with the ons on the end of rectangle'''
			temp = index_first[:]
			index_first[1] = index_sec[1]
			index_sec[1] = temp[1]

		#assigning value of index in pair
		pair[0] = table[index_first[0]][index_first[1]]
		pair[1] = table[index_sec[0]][index_sec[1]]
	
	print(tuples_message)
	return tuples_message



def main():
    key = sys.argv[1] #monarchy
    key_list = list(key.strip())

    removed_letter = str(sys.argv[2])
    alpha=['a','b','c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

    # key_list.append(removed_letter)
    fill_matrix = [x for x in alpha if x not in key_list and x != removed_letter]

    # the matrix essential
    fill = key_list
    fill.extend(fill_matrix)

    table = [[] for i in range(5)]

    # preparing list of table
    for col in table:
    	temp_col = fill[:5]
    	del fill[:5]
    	col.extend(temp_col)

    print(table)

    message = input("Enter the message to be encrypted:") #parallel
    tuples_message = preparing_message(message)

    playfair_dec(tuples_message, table)

if __name__ == "__main__":
    main()

    # secretmessage
    # nordkunkqzpcnd
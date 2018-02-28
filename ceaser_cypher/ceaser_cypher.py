import sys

def enc_dec(shiftby, input_file, method, output_file):
	f = open(input_file, 'r')
	in_string = f.readlines()

	output = open(output_file, "w")

	for sen in in_string:
		sen= sen.upper()
		print(sen)
		for char in sen:
			# number of char to be displayed in txt
			if method == "enc":
				num = ord(char) + int(shiftby)
			else:
				num = ord(char) - int(shiftby)
			
			char = chr(num)
			output.write(char)

	output.close()

def main():
	# python ceaser_cypher.py shiftby input.txt enc/dec output.txt
	
	shiftby = sys.argv[1]
	input_file = sys.argv[2]
	method = sys.argv[3]
	output_file = sys.argv[4]

	enc_dec(shiftby, input_file, method, output_file)
 

if __name__ == "__main__":
	main()


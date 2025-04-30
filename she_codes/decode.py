#decoding a message. every letter is switched to the 13th letter forward
def rot_13():
    """
    a way to create the initial dictionary
    """
    encoding = {}
    abc = 'abcdefghijklmnopqrstuvwxyzabcdefghijklm'
    abc_capital = abc.upper()

    for i in range(0, 26):
        encoding.update({abc[i]: abc[i + 13]})
        encoding.update({abc_capital[i]: abc_capital[i + 13]})

    return encoding

def decode(s):
    key = rot_13()
    sentence = []

    for i in range(len(s)):
        if key.get(s[i]) is None :
            sentence.append(s[i])

        else:
            sentence.append(key[s[i]])

    new_sentence = ''.join(sentence)

    return new_sentence




print(decode('V NZ YRNEAVAT CLGUBA JVGU FUR PBQRF NPNQRZL!'))
print(decode('I AM LEARNING PYTHON WITH SHE CODES ACADEMY!'))

# Function to convert integer to Roman values
def printRoman(number):
	num = [1, 4, 5, 9, 10, 40, 50, 90,
		100, 400, 500, 900, 1000]
	sym = ["I", "IV", "V", "IX", "X", "XL",
		"L", "XC", "C", "CD", "D", "CM", "M"]
	i = 12

	while number:
		div = number // num[i]
		number %= num[i]

		while div:
			print(sym[i], end = "")
			div -= 1
		i -= 1

printRoman(2678)

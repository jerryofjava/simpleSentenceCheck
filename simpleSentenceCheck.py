#Capitalizes the first letter at the beginning of the string, and capitalizes any letter after a period('.'), exclamation mark('!'), or question mark('?')  
def capitalize(sentence):
    newSentence = ""
    letterBefore = ""
	
    newSentence += sentence[0:1].upper()
    letterBefore = newSentence[0]
    for letter in sentence[1:]:
        if letterBefore == "." or letterBefore == "!" or letterBefore == "?":
            newSentence += letter.upper()
            letterBefore = letter
        else:
            newSentence += letter
            letterBefore = letter
			
    return newSentence

#Places a space after each period('.'), comma(','), exclamation mark('!'), question mark('?'), or semi-colon(';')
def put_spaces(sentence):
    newSentence=""
    for letter in sentence:
        if sentence.index(letter) != 0 and sentence.index(letter) != len(sentence)-1 and (letter == "." or letter == "," or letter == "!" or letter == "?" or letter == ";"):
            if (sentence[sentence.index(letter)+1] != " " and sentence[sentence.index(letter)+1] != "." and sentence[sentence.index(letter)+1] != "!" \
		       and sentence[sentence.index(letter)+1] != "?" and sentence[sentence.index(letter)+1] != "," and sentence[sentence.index(letter)+1] != ";"):
                newSentence += letter+" "
            else:
                newSentence += letter
        else:
                newSentence += letter				
			
    return newSentence

#Main function of the program
def main():
    sentence = input("Input a string for correction: ")
    capSentence = capitalize(sentence)
    spcSentence = put_spaces(capSentence)
    print("Corrected String: "+spcSentence)
    exit = input("Press ENTER to exit.")

#Start the program
main()
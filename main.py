from art import logo
alphaforward = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
alphareverse = 'zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba'
def encrypt(alphabets, encdec, inputtext, shiftrequired):
  assert len(alphabets) > 26 and encdec != '' and inputtext != '' 
  resulttext = ''
  # if encdec == 'encode':
  for i in range(0, len(inputtext)):
    resulttext += alphabets[alphabets.index(inputtext[i]) + shiftrequired]
  return(resulttext)


alphabet = list(alphaforward)
alphabetreversed = list(alphareverse)
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
if direction == 'encode':
  result = encrypt(alphabet, direction, text, shift)
  print(f"The encrypted word is {result}")  
else:
  result = encrypt(alphabetreversed, direction, text, shift)
  print(f"The decrypted word is {result}")

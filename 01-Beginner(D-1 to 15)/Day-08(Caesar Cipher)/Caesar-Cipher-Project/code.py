import art
print(art.logo)



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):  #1 : Define the function with parameters for the original text, shift amount, and whether to encode or decode.
    output_text = ""                                         #3 : Create an empty string to store the output text.
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:                             #2 : Loop through each letter in the original text.(originaltext is the text inputted by user)

        if letter not in alphabet:                             #4 : we created this intentionaly since that else part of shifted position actually stayed as if part but
            output_text += letter                              # BUt due to if user written like hello! then symbol be reflected as it is , so only we created this becauses in alphabets any way theer is alphabets only so
        else:
            shifted_position = alphabet.index(letter) + shift_amount #5 index() refer to the picture i have attached in folder .index() &  .count() function used to find the index number in the list : IT means inside the alphabet (letter for example "C " present at what index that index number be added with shift _number user wants to shift that alphabet beautiful logic of maths here)
            output_text += alphabet[shifted_position]                #6 : that final shifted position will be as number to make as readable text we use the alphabet[] see square braces
    print(f"Here is the {encode_or_decode}d result: {output_text}") 


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("BYE HAVE A GOOD DAY :) ")
import random
import string


chars = " "+ string.punctuation+string.digits+string.ascii_letters
chars = list(chars)
key = chars.copy()


random.shuffle(key)

#Encription of message
plain_txt=input("Enter any message to encript:")
encripte_txt=""

for letter in plain_txt:
    index = chars.index(letter)  #this find all the letter in string that is inside the list and gives the postion of that string in list
    encripte_txt+=key[index] #this add the postion of the string in list key and add to encipted txt


print(f"you original message:{plain_txt}")
print(f"your encripted message:{encripte_txt}")
chosice=input("do you wnat this message to be send encripted(y/n)").capitalize

if chosice== "y":
    print("IT has been send")
else:
    print("Thanks for trying my program")

#dicription of message
encripted_txt=input("Enter your encripted message:")
plain_txt=""

for letter in encripted_txt:
    index = key.index(letter)  
    plain_txt+=chars[index] 

print(f"your decripted message:{plain_txt}")


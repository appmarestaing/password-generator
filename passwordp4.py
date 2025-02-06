import random
import string
import requests 

# function that generates a single random character
def random_character():
    choices = string.ascii_letters + string.digits + string.punctuation
    return random.choice(choices)

passwordLength = 12 #make it so that you ask the user for a length or generate a random number

# function that generates a random password 
def generate_strong_password():
    password = ""
    for i in range(passwordLength):
        password = password + random_character()
    print(password)

generate_strong_password()

# function to give us a random word 
def fetch_word():
    response = requests.get("https://random-word-api.herokuapp.com/word?length=6")
    word = response.json()[0] 
    return word

print(fetch_word())

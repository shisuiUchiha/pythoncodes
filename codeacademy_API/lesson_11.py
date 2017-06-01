import requests

# Make a GET request here and assign the result to kittens:
kittens=requests.get('http://placekitten.com/')


print kittens.headers	
print kittens.text[559:1000]
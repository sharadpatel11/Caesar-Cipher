import os
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cypher(data, degree, dir):
  result = []
  for i in range(0, len(data)):
    if alphabet.count(data[i]) > 0 and dir == "encode":
      index = (alphabet.index(data[i]) + degree) % 26
      result.append(alphabet[index])
    elif alphabet.count(data[i]) > 0 and dir == "decode":
        index = alphabet.index(data[i]) - degree
        result.append(alphabet[index])
    else:
        result.append(data[i])
  
  return result

run = "yes"
while run == "yes":
  os.system('cls' if os.name == 'nt' else 'clear')
  print(art.logo)
  
  validDir = ["encode", "decode"]
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
  while validDir.count(direction) <= 0:
    direction = input("Try again. Type 'encode' to encrypt, type 'decode' to decrypt: ")
  
  text = input("Type your message: ").lower()
  shift = int(input("Type the shift number: "))

  print(f"\nYour {direction}d word: {(''.join(cypher(text, shift, direction)))}")

  run = input("\nDo you want to continue: yes or no?\n")
  run.lower()

os.system('cls' if os.name == 'nt' else 'clear') 
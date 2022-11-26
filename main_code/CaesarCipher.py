def encrypt(string, shift):

  cipher = ''
  for char in string:
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  
  return cipher


def decrypt(cipher,key):
    encrp_msg = cipher
    decrp_key = key

    decrypted_text = ""

    for i in range(len(encrp_msg)):
        if ord(encrp_msg[i]) == 32:
            decrypted_text += chr(ord(encrp_msg[i]))

        elif ((ord(encrp_msg[i]) - decrp_key) < 97) and ((ord(encrp_msg[i]) - decrp_key) > 90):
            # subtract key from letter ASCII and add 26 to current number
            temp = (ord(encrp_msg[i]) - decrp_key) + 26
            decrypted_text += chr(temp)

        elif (ord(encrp_msg[i]) - decrp_key) < 65:
            temp = (ord(encrp_msg[i]) - decrp_key) + 26
            decrypted_text += chr(temp)

        else:
            decrypted_text += chr(ord(encrp_msg[i]) - decrp_key)

    return decrypted_text
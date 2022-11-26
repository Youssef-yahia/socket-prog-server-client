import string

def caesarEncrypt(text, shift):
    alphabets = [string.ascii_lowercase, string.ascii_uppercase , string.punctuation]
    def shift_alphabet(alphabet):
        return alphabet[shift:]+ alphabet[:shift]
    
    shifted_alphabets = tuple(map(shift_alphabet,alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet,final_shifted_alphabet)
    return text.translate(table)

def caesarDecrypt(text, shift):
    alphabets = [string.ascii_lowercase, string.ascii_uppercase , string.punctuation]
    def shift_alphabet(alphabet):
        new_shift = 26-shift
        return alphabet[new_shift:]+ alphabet[:new_shift]
    
    shifted_alphabets = tuple(map(shift_alphabet,alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet,final_shifted_alphabet)
    return text.translate(table)
    
    
plain_text = "This is a new (test) Hello World!"
cipher_text = caesarEncrypt(plain_text, 7)
plain_text_new = caesarDecrypt(cipher_text, 7)
print(cipher_text)
print(plain_text_new)

class translate:
    a2mo_dict = {'a': '01', 'b': '1000', 'c': '1010', 'd': '100', 'e': '0',
                 'f': '0010', 'g': '110', 'h': '0000', 'i': '00', 'j': '0111',
                 'k': '101', 'l': '0100', 'm': '11', 'n': '10', 'o': '111',
                 'p': '0110', 'q': '1101', 'r': '010', 's': '000', 't': '1',
                 'u': '001', 'v': '0001', 'w': '011', 'x': '1001', 'y': '1011', 'z': '1100',
                 '0': '11111', '1': '01111', '2': '00111', '3': '00011', '4': '00001',
                 '5': '00000', '6': '10000', '7': '11000', '8': '11100', '9': '11110'
                 }

    def mo_str(self,crypto_text):
        morse_key = crypto_text.strip().split(" ")
        plain_text = [mo2a_dict[key] for key in morse_key]
        plain_text = "".join(plain_text)
        return plain_text

    def str_mo(self,str_text):
        crypto_text = ""
        plain_text = str_text.strip().replace(" ", "")
        for word in plain_text:
            crypto_text += a2mo_dict[word] + " "
        return crypto_text
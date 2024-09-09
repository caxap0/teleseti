class Coder:
    def __init__(self, text, dict):
        self.text = text
        self.dict = dict

    def utf8_to_windows1251(self):
        result = bytearray()
        for char in self.text:
            if char in self.dict:
                result.append(self.dict[char])
        return bytes(result)

    def windows1251_to_bin(self, coded_text):
        binary_string = ''
        for byte in coded_text:
            binary_string += f'{byte:08b} '
        return binary_string

    def windows1251_to_utf8(self, coded_text):
        result = ''
        cp1251_to_utf8 = {value: key for key, value in self.dict.items()}
        for byte in coded_text:
            if byte in cp1251_to_utf8:
                result += cp1251_to_utf8[byte]
        return result


utf8_to_cp1251 = {
    'А': 0xC0, 'Б': 0xC1, 'В': 0xC2, 'Г': 0xC3, 'Д': 0xC4, 'Е': 0xC5, 'Ж': 0xC6, 'З': 0xC7,
    'И': 0xC8, 'Й': 0xC9, 'К': 0xCA, 'Л': 0xCB, 'М': 0xCC, 'Н': 0xCD, 'О': 0xCE, 'П': 0xCF,
    'Р': 0xD0, 'С': 0xD1, 'Т': 0xD2, 'У': 0xD3, 'Ф': 0xD4, 'Х': 0xD5, 'Ц': 0xD6, 'Ч': 0xD7,
    'Ш': 0xD8, 'Щ': 0xD9, 'Ъ': 0xDA, 'Ы': 0xDB, 'Ь': 0xDC, 'Э': 0xDD, 'Ю': 0xDE, 'Я': 0xDF,
    'а': 0xE0, 'б': 0xE1, 'в': 0xE2, 'г': 0xE3, 'д': 0xE4, 'е': 0xE5, 'ж': 0xE6, 'з': 0xE7,
    'и': 0xE8, 'й': 0xE9, 'к': 0xEA, 'л': 0xEB, 'м': 0xEC, 'н': 0xED, 'о': 0xEE, 'п': 0xEF,
    'р': 0xF0, 'с': 0xF1, 'т': 0xF2, 'у': 0xF3, 'ф': 0xF4, 'х': 0xF5, 'ц': 0xF6, 'ч': 0xF7,
    'ш': 0xF8, 'щ': 0xF9, 'ъ': 0xFA, 'ы': 0xFB, 'ь': 0xFC, 'э': 0xFD, 'ю': 0xFE, 'я': 0xFF,
    'Ё': 0xA8, 'ё': 0xB8,
    'A': 0x41, 'B': 0x42, 'C': 0x43, 'D': 0x44, 'E': 0x45, 'F': 0x46, 'G': 0x47, 'H': 0x48,
    'I': 0x49, 'J': 0x4A, 'K': 0x4B, 'L': 0x4C, 'M': 0x4D, 'N': 0x4E, 'O': 0x4F, 'P': 0x50,
    'Q': 0x51, 'R': 0x52, 'S': 0x53, 'T': 0x54, 'U': 0x55, 'V': 0x56, 'W': 0x57, 'X': 0x58,
    'Y': 0x59, 'Z': 0x5A, 'a': 0x61, 'b': 0x62, 'c': 0x63, 'd': 0x64, 'e': 0x65, 'f': 0x66,
    'g': 0x67, 'h': 0x68, 'i': 0x69, 'j': 0x6A, 'k': 0x6B, 'l': 0x6C, 'm': 0x6D, 'n': 0x6E,
    'o': 0x6F, 'p': 0x70, 'q': 0x71, 'r': 0x72, 's': 0x73, 't': 0x74, 'u': 0x75, 'v': 0x76,
    'w': 0x77, 'x': 0x78, 'y': 0x79, 'z': 0x7A, '0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33,
    '4': 0x34, '5': 0x35, '6': 0x36, '7': 0x37, '8': 0x38, '9': 0x39,
    ' ': 0x20, '.': 0x2E, ',': 0x2C, '!': 0x21, '?': 0x3F,
}

message = "Привет, мир!"
encoded_text = Coder(message, utf8_to_cp1251)
encoded = encoded_text.utf8_to_windows1251()
bin_encoded = encoded_text.windows1251_to_bin(encoded)
decoded = encoded_text.windows1251_to_utf8(encoded)


# кнопка сохранения в бинарный файл
def save_binary_file(file, bin_text):
    with open(file, 'wb') as file:
        file.write(bin_text)


# кнопка сохранения в текстовый файл
def save_text_file(file, text):
    text = ' '.join(f'{byte:02x}' for byte in text)
    with open(file, 'w') as file:
        file.write(text)


save_binary_file('binary.txt', encoded)
save_text_file('text.txt', encoded)
print(encoded, bin_encoded, decoded, sep='\n')

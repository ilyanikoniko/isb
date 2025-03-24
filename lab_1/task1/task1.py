def vigenere_encrypt(key, alphabet, text):
    """
    Функция для шифрования текста с шифром Виженера.
    :param key: ключ шифрования
    :param alphabet: алфавит для шифрования
    :param text: исходный текст для шифрования
    :return: зашифрованный текст
    """
    try:
        for char in key:
            if char not in alphabet:
                raise ValueError(f"Ключ содержит недопустимый символ: '{char}'")

        key = key.lower()
        text = text.lower()
        key_length = len(key)
        encrypt_text = ''
        alphabet_size = len(alphabet)

        for i in range(len(text)):
            char = text[i]
            if char.lower() in alphabet:
                char_index = alphabet.find(char)
                key_char = key[i % key_length]
                key_char_index = alphabet.find(key_char)
                new_index = (char_index + key_char_index) % alphabet_size
                encrypt_text += alphabet[new_index]
            else:
                encrypt_text += char
        return encrypt_text
    except ValueError as e:
        print(f"Ошибка: {e}")
        return ""
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        return ""


def save_to_file(filename, data):
    """
    Сохранение данных в файл
    :param filename: путь к файлу
    :param data: данные
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(data)
    except Exception as e:
        print(f"Ошибка при записи в файл {filename}: {e}")




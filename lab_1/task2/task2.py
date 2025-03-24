def replace_chars_safely(text, replacements):
    """
    Заменяет символы в тексте по словарю replacements
    :param text: Исходный текст
    :param replacements: Словарь замен
    :return: Текст после замен
    """
    try:
        return ''.join(replacements.get(char, char) for char in text)
    except Exception as e:
        print(f"Ошибка при замене символов: {e}")
        return text


def write_to_file(filename, data):
    """
    Записывает содержимое в файл.
    :param filename: путь к файлу
    :param data: содержимое файла для записи
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(data)
    except Exception as e:
        print(f"Ошибка при записи в файл {filename}: {e}")


def calculate_char_frequency(text):
    """
    Вычисляет частоту встреч символов в тексте
    :param text: исходный текст
    :return: словарь, где ключ/значение - символ/частота его встречаемости
    """
    try:
        dictionary_freq = {}
        text_len = len(text)

        for char in text:
            dictionary_freq[char] = dictionary_freq.get(char, 0) + 1

        return {char: (count / text_len) * 100 for char, count in dictionary_freq.items()}
    except Exception as e:
        print(f"Ошибка при вычислении процента символов: {e}")
        return {}


def create_crypt_key(supportive_dict, replace_dict):
    """
    Создает словарь encryption_key на основе вспомогательного и основного словарей
    :param supportive_dict: вспомогательный словарь замен SUPPORTIVE_DICT
    :param replace_dict: основной словарь замен REPLACE_DICT
    :return: ключ-словарь  encryption_key
    """
    try:
        reverse_supportive_dict = {val: key for key, val in supportive_dict.items()}

        encryption_key = {}
        for key, val in replace_dict.items():
            if key in reverse_supportive_dict:
                original_key = reverse_supportive_dict[key]
                encryption_key[original_key] = val
        for key, val in replace_dict.items():
            if key not in reverse_supportive_dict:
                encryption_key[key] = val
        return encryption_key
    except Exception as e:
        print(f"Ошибка при создании ключа шифрования: {e}")
        return encryption_key

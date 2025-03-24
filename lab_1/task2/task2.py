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
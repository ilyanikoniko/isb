import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from filehandler import FileHandler

class Symmetrical:
    """
    Класс для алгоритма шифрования CAST5
    """
    @staticmethod
    def generate_key(key_len_bits: int) -> bytes:
        """
        Генерирует ключ с заданной длиной
        :param key_len_bits: длина ключа
        :return: ключ
        """
        if not (40 <= key_len_bits <= 128):
            raise ValueError("Длина ключа должна быть 40-128 бит!")
        key_len_bytes = key_len_bits // 8
        key = os.urandom(key_len_bytes)
        return key

    @staticmethod
    def serialize_symmetric_key(key: bytes, file_path: str) -> None:
        """
        Сериализация симметричного ключа в файл
        :param key: симметричный ключ
        :param file_path: путь для сохранения ключа
        :return: None
        """
        FileHandler.write_bytes(file_path, key)

    @staticmethod
    def deserialize_symmetric_key(file_path: str) -> bytes:
        """
        Десериализация симметричного ключа
        :param file_path: файл с ключом
        :return: ключ в виде байтовой последовательности
        """
        return FileHandler.get_bytes(file_path)

    @staticmethod
    def encrypt_text(key: bytes, file_path: str, text_file: str) -> None:
        """
        Шифрование текстового файла симметричным алгоритмом
        :param key: симметричный ключ
        :param file_path: путь для сохранения зашифрованных данных
        :param text_file: путь к исходному текстовому файлу
        :return: None
        """
        try:
            with open(text_file, 'r', encoding='utf-8', newline='') as f:
                text = f.read()

            if not text:
                raise ValueError("Пустой файл для шифрования")

            if not (5 <= len(key) <= 16):
                raise ValueError(f"Некорректный размер ключа: {len(key)} байт")

            text_bytes = text.encode('utf-8')

            padder = padding.ANSIX923(64).padder()
            padded_text = padder.update(text_bytes) + padder.finalize()

            iv = os.urandom(8)
            cipher = Cipher(algorithms.CAST5(key), modes.CBC(iv))
            encryptor = cipher.encryptor()
            c_text = iv + encryptor.update(padded_text) + encryptor.finalize()

            FileHandler.write_bytes(file_path, c_text)
        except Exception as e:
            raise Exception(f"Ошибка шифрования: {str(e)}")

    @staticmethod
    def decrypt_text(key: bytes, file_path: str, text_file: str) -> str:
        """
        Дешифрование файла, зашифрованного симметричным алгоритмом
        :param key: симметричный ключ
        :param file_path: путь для сохранения расшифрованного текста
        :param text_file: путь к зашифрованному файлу
        :return: расшифрованный текст
        """
        try:
            encrypted_data = FileHandler.get_bytes(text_file)
            if len(encrypted_data) < 8:
                raise ValueError("Файл слишком короткий для расшифровки")

            iv = encrypted_data[:8]
            encrypted_text = encrypted_data[8:]

            if not (5 <= len(key) <= 16):
                raise ValueError(f"Некорректный размер ключа: {len(key)} байт")

            cipher = Cipher(algorithms.CAST5(key), modes.CBC(iv))
            decryptor = cipher.decryptor()
            decrypted_padded = decryptor.update(encrypted_text) + decryptor.finalize()

            unpadder = padding.ANSIX923(64).unpadder()
            unpadded_text = unpadder.update(decrypted_padded) + unpadder.finalize()

            try:
                result = unpadded_text.decode('UTF-8').replace('\r\n', '\n').replace('\r', '\n')

                with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
                    f.write(result)
                return result
            except UnicodeDecodeError:
                raise ValueError("Ошибка декодирования - возможно, неверный ключ")

        except Exception as e:
            raise Exception(f"Ошибка дешифрования: {str(e)}")
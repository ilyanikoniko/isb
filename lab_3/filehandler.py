import json

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


class FileHandler:
    """
    Вспомогательный класс для работы с файлами
    """
    @staticmethod
    def write_public_key(file_path: str, public_key: RSAPublicKey) -> None:
        """
        Сохранение открытого ключа в pem файл
        :param file_path: путь для сохранения
        :param public_key: открытый ключ
        :return: None
        """
        try:
            with open(file_path, 'wb') as public_out:
                public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                     format=serialization.PublicFormat.SubjectPublicKeyInfo))
        except FileNotFoundError:
            print(f"Файл не найден")
        except Exception as e:
            print(f"При записи данных в файл произошла ошибка: {str(e)}.")

    @staticmethod
    def write_private_key(file_path: str, private_key: RSAPrivateKey) -> None:
        """
        Сохранение закрытого ключа в pem файл
        :param file_path: путь для сохранения
        :param private_key: закрытый ключ
        :return: None
        """
        try:
            with open(file_path, 'wb') as private_out:
                private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                        encryption_algorithm=serialization.NoEncryption()))
        except FileNotFoundError:
            print(f"Файл не найден")
        except Exception as e:
            print(f"При записи данных в файл произошла ошибка: {str(e)}.")

    @staticmethod
    def extraction_public_key(file_path: str) -> RSAPublicKey:
        """
        Извлечение открытого ключа из pem файла
        :param file_path: путь к файлу
        :return: открытый ключ
        """
        try:

            with open(file_path, 'rb') as pem_in:

                public_bytes = pem_in.read()
            return load_pem_public_key(public_bytes)
        except FileNotFoundError:
            print(f"Файл не найден")
        except Exception as e:
            print(f"При чтении файла произошла ошибка: {str(e)}.")

    @staticmethod
    def extraction_private_key(file_path: str) -> RSAPrivateKey:
        """
        Извлечение закрытого ключа из pem файла
        :param file_path: путь к файлу
        :return: закрытый ключ
        """
        try:

            with open(file_path, 'rb') as pem_in:

                private_bytes = pem_in.read()
            return load_pem_private_key(private_bytes, password=None, )
        except FileNotFoundError:
            print(f"Файл не найден")
        except Exception as e:
            print(f"При чтении файла произошла ошибка: {str(e)}.")

    @staticmethod
    def write_bytes(file_path: str, data: bytes) -> None:
        """
        Запись бинарных данных в файл
        :param file_path: путь к файлу
        :param data: бинарные данные
        :return: None
        """
        try:
            with open(file_path, mode='wb') as file:
                file.write(data)
        except FileNotFoundError:
            print(f"Файл не найден")
        except Exception as e:
            print(f"При записи данных в файл произошла ошибка: {str(e)}.")

    @staticmethod
    def get_bytes(file_path: str) -> bytes:
        """
        Чтение бинарных данных из файла
        :param file_path: путь к файлу
        :return: байты
        """
        try:
            with open(file_path, 'rb') as file:
                data = file.read()
            return data
        except FileNotFoundError:
            print(f"Файл не найден")
        except Exception as e:
            print(f"При чтении файла произошла ошибка: {str(e)}.")

    @staticmethod
    def write_txt(file_path: str, text: str) -> None:
        """
        Запись текстовых данных в файл
        :param file_path: файл куда записывать текст
        :param text: текст для записи
        :return: None
        """
        try:
            with open(file_path, 'w') as file:
                file.write(text)
        except FileNotFoundError:
            print(f"Файл не найден")
        except Exception as e:
            print(f"При записи данных в файл произошла ошибка: {str(e)}.")

    @staticmethod
    def write_json(file_path: str, data: dict) -> None:
        """
        Сохранение в JSON файл
        :param file_path: путь к файлу
        :param data: словарь
        :return: None
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as fp:
                json.dump(data, fp, ensure_ascii=False, indent=1)
        except FileNotFoundError:
            print(f"Файл не найден")
        except Exception as e:
            print(f"При записи данных в файл произошла ошибка: {str(e)}.")

    @staticmethod
    def get_json(file_name: str) -> dict[str, str]:
        """
        Чтение и парсинг JSON файла
        :param file_name: путь к JSON-файлу
        :return: словарь
        """
        try:
            with open(file_name, 'r', encoding='utf-8') as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            print(f"Файл не найден")
        except Exception as e:
            print(f"При чтении файла произошла ошибка: {str(e)}.")
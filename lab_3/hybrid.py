from asymmetrical import Asymmetrical
from symmetrical import Symmetrical

class Hybrid:
    """
    Класс совмещающий RSA и CAST5 алгоритмы
    """
    @staticmethod
    def generate_and_save_keys(
            public_key_path: str,
            private_key_path: str,
            encrypted_sym_key_path: str,
            key_length: int = 128) -> None:
        """
        Генерация и сохранение ключей для гибридной криптосистемы
        :param public_key_path: путь для хранения открытого ключа
        :param private_key_path: путь для хранения закрытого ключа
        :param encrypted_sym_key_path: путь для хранения симметричного ключа
        :param key_length: длина ключа
        :return: None
        """
        private_key, public_key = Asymmetrical.generate_asymmetrical_keys()

        Asymmetrical.serialize_public_key(public_key_path, public_key)
        Asymmetrical.serialize_private_key(private_key_path, private_key)

        symmetric_key = Symmetrical.generate_key(key_length)

        Asymmetrical.encryption_by_public_key(
            public_path=public_key_path,
            symmetric_key=symmetric_key,
            file_path=encrypted_sym_key_path
        )

    @staticmethod
    def encrypt_data(
            file_path: str,
            private_key_path: str,
            encrypted_sym_key_path: str,
            encrypted_path: str
    ) -> None:
        """
        Шифрует данные с помощью гибридного шифрования
        :param file_path: путь к файлу с данными для шифрования
        :param private_key_path: путь к файлу с закрытым ключом
        :param encrypted_sym_key_path: путь к файлу с зашифрованным симметричным ключом
        :param encrypted_path: путь для сохранения зашифрованного текста
        :return: None
        """
        symmetric_key = Asymmetrical.decryption_by_private_key(
            private_path=private_key_path,
            file_path=encrypted_sym_key_path
        )

        Symmetrical.encrypt_text(
            key=symmetric_key,
            file_path=encrypted_path,
            text_file=file_path
        )

    @staticmethod
    def decrypt_data(
            encrypted_file_path: str,
            private_key_path: str,
            encrypted_sym_key_path: str,
            decrypted_path: str
    ) -> None:
        """
        Дешифрует данные с помощью гибридного шифрования
        :param encrypted_file_path: путь к файлу с зашифрованными данными
        :param private_key_path: путь к pem файлу с закрытым ключом
        :param encrypted_sym_key_path: путь к файлу с зашифрованным симметричным ключом
        :param decrypted_path: путь для сохранения расшифрованных данных
        :return: None
        """
        symmetric_key = Asymmetrical.decryption_by_private_key(
            private_path=private_key_path,
            file_path=encrypted_sym_key_path
        )

        Symmetrical.decrypt_text(
            key=symmetric_key,
            file_path=decrypted_path,
            text_file=encrypted_file_path
        )
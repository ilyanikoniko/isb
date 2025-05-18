from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from typing import Tuple
from filehandler import FileHandler

class Asymmetrical:
    """
    Класс, который работает с RSA алгоритмом
    """
    @staticmethod
    def generate_asymmetrical_keys() -> Tuple[RSAPrivateKey, RSAPublicKey]:
        """
        Генерация открытого и закрытого ключа для RSA алгоритма
        :return: пара сгенерированных ключей
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def serialize_public_key(file_path: str, public_key: RSAPublicKey) -> None:
        """
        Сериализация открытого ключа в файл
        :param file_path: файл в который записывается ключ
        :param public_key: открытый ключ
        :return: None
        """
        FileHandler.write_public_key(file_path, public_key)

    @staticmethod
    def serialize_private_key(file_path: str, private_key: RSAPrivateKey) -> None:
        """
        Сериализация закрытого ключа в файл
        :param file_path: файл в который записывается ключ
        :param private_key: закрытый ключ
        :return: None
        """
        FileHandler.write_private_key(file_path, private_key)

    @staticmethod
    def deserialization_public_key(file_path: str) -> RSAPublicKey:
        """
        Десериализация открытого ключа
        :param file_path: файл откуда считывается ключ
        :return: открытый ключ
        """
        return FileHandler.extraction_public_key(file_path)

    @staticmethod
    def deserialization_private_key(file_path: str) -> RSAPrivateKey:
        """
        Десериализация закрытого ключа
        :param file_path: файл откуда считывается ключ
        :return: закрытый ключ
        """
        return FileHandler.extraction_private_key(file_path)

    @staticmethod
    def encryption_by_public_key(public_path: str, symmetric_key: bytes, file_path: str) -> bytes:
        """
        Шифрование симметричного ключа открытым ключом
        :param public_path: файл с открытым ключом
        :param symmetric_key: симметричный ключ
        :param file_path: файл куда будет записан симметричный ключ
        :return: зашифрованный симметричный ключ
        """
        public_key = Asymmetrical.deserialization_public_key(public_path)
        encryption_sym_key = public_key.encrypt(symmetric_key,
                                    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),
                                                 label=None))
        FileHandler.write_bytes(file_path, encryption_sym_key)
        return  encryption_sym_key

    @staticmethod
    def decryption_by_private_key(private_path: str, file_path: str) -> bytes:
        """
        Lешифрование симметричного ключа с использованием закрытого ключа
        :param private_path: файл с закрытым ключом
        :param file_path: путь к файлу, содержащему зашифрованный симметричный ключ
        :return: расшифрованный симметричный ключ
        """
        private_key = Asymmetrical.deserialization_private_key(private_path)
        symmetric_key = FileHandler.get_bytes(file_path)
        decryption_sym_key = private_key.decrypt(symmetric_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                           algorithm=hashes.SHA256(), label=None))
        return decryption_sym_key
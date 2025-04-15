import argparse
import nist_tests
import os


def parse_arguments():
    """
    Парсинг аргументов
    :return: Объект argparse
    """
    parser = argparse.ArgumentParser(description="Сравнение последовательностей C++ и Java кода")
    parser.add_argument("cpp_file", help="Путь C++ к файлу с сгенерированной последовательностью")
    parser.add_argument("java_file", help="Путь к Java файлу с сгенерированной последовательностью")
    parser.add_argument("results", help="Файл для сохранения результатов тестов")
    return parser.parse_args()
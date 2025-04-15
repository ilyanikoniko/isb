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


def read_file(filename: str):
    """
    Чтение файла
    :param filename: Путь к файлу
    :return: Последовательность в виде строки
    """
    with open(filename, "r") as file:
        sequence = file.read()
    return sequence


def write_results(freq_cpp, freq_java,
                 runs_cpp, runs_java,
                 long_cpp, long_java,
                 results: str):
    """
    Сохранение результатов тестов в файл
    :param freq_cpp: P-значение частотного побитового теста последовательности из cpp файла
    :param freq_java: P-значение частотного побитового теста последовательности из java файла
    :param runs_cpp: P-значение теста на одинаковые подряд идущие биты последовательности из cpp файла
    :param runs_java: P-значение теста на одинаковые подряд идущие биты последовательности из java файла
    :param long_cpp: P-значение теста на самую длинную послежовательность единиц в блоке последовательности из cpp файла
    :param long_java: P-значение теста на самую длинную послежовательность единиц в блоке последовательности из java файла
    :param results: Путь к файлу для записи результатов
    :return:
    """
    with open(results, 'w') as file:
        file.write("Frequency bitwise test:\n")
        file.write(f"cpp: {freq_cpp}\n")
        file.write(f"java: {freq_java}\n\n")

        file.write("A test for identical consecutive bits:\n")
        file.write(f"cpp: {runs_cpp}\n")
        file.write(f"java: {runs_java}\n\n")

        file.write("Test for the longest sequence of units in a block:\n")
        file.write(f"cpp: {long_cpp}\n")
        file.write(f"java: {long_java}\n")
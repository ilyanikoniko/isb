import argparse
import os
import sys
from pathlib import Path
from hybrid import Hybrid
from filehandler import FileHandler
from constants import SETTINGS_FILE, DEFAULT_SETTINGS


def create_default_settings_if_needed() -> None:
    """
    Создает файл настроек с дефолтными значениями, если он отсутствует
    :return: None
    """
    if not Path(SETTINGS_FILE).exists():
        FileHandler.write_json(SETTINGS_FILE, DEFAULT_SETTINGS)
        print(f" Создан файл настроек '{SETTINGS_FILE}' с дефолтными значениями.")


def load_settings() -> dict[str, str]:
    """
    Загружает настройки из JSON файла
    :return: настройки из JSON файла
    """
    try:
        settings = FileHandler.get_json(SETTINGS_FILE)
        return settings
    except Exception as e:
        print(f" Ошибка загрузки настроек: {e}. Используются значения по умолчанию")
        return DEFAULT_SETTINGS


def parse_arguments() -> argparse.Namespace:
    """
    Парсинг аргументов командной строки
    :return: объект с атрибутами
    """
    parser = argparse.ArgumentParser(
        description="Гибридная криптосистема (RSA + CAST5)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-m", "--mode",
        choices=["generate", "encrypt", "decrypt"],
        required=True,
        help="Выберите режим работы:\ngenerate - создание ключей\nencrypt - зашифровать текст\ndecrypt - расшифровать текст"
    )
    parser.add_argument(
        "-l", "--key-length",
        type=int,
        choices=[i for i in range(40, 129) if i % 8 == 0],
        metavar="[40-128]",
        default=128,
        help="Длина симметричного ключа в битах (только для режима generate)"
    )
    return parser.parse_args()


def main():
    """
    Основной управляющий модуль
    :return: None
    """
    create_default_settings_if_needed()

    settings = load_settings()
    hybrid = Hybrid()
    args = parse_arguments()
    try:
        match args.mode:
            case "generate":
                print("Генерация ключей...")
                hybrid.generate_and_save_keys(
                    public_key_path=settings["public_key"],
                    private_key_path=settings["private_key"],
                    encrypted_sym_key_path=settings["symmetric_key"],
                    key_length=args.key_length
                )
                print("Ключи успешно сгенерированы и сохранены")

            case "encrypt":
                print("Шифрование данных...")

                if not all([
                    os.path.exists(settings["private_key"]),
                    os.path.exists(settings["public_key"]),
                    os.path.exists(settings["symmetric_key"])
                ]):
                    raise FileNotFoundError(
                        "Ключи не найдены. Сначала выполните генерацию ключей (режим generate)"
                    )

                if not os.path.exists(settings["initial_text"]):
                    raise FileNotFoundError(
                        f"Исходный файл {settings['initial_text']} не найден"
                    )

                hybrid.encrypt_data(
                    file_path=settings["initial_text"],
                    private_key_path=settings["private_key"],
                    encrypted_sym_key_path=settings["symmetric_key"],
                    encrypted_path=settings["encrypted_text"]
                )
                print(f"Данные зашифрованы в {settings['encrypted_text']}")

            case "decrypt":
                print("Дешифрование данных...")

                if not os.path.exists(settings["encrypted_text"]):
                    raise FileNotFoundError(
                        f"Зашифрованный файл {settings['encrypted_text']} не найден"
                    )

                if not all([
                    os.path.exists(settings["private_key"]),
                    os.path.exists(settings["symmetric_key"])
                ]):
                    raise FileNotFoundError(
                        "Необходимые ключи не найдены. Проверьте наличие приватного ключа и зашифрованного симметричного ключа"
                    )

                hybrid.decrypt_data(
                    encrypted_file_path=settings["encrypted_text"],
                    private_key_path=settings["private_key"],
                    encrypted_sym_key_path=settings["symmetric_key"],
                    decrypted_path=settings["decrypted_text"]
                )
                print(f"Данные дешифрованы в {settings['decrypted_text']}")

            case _:
                print("Неизвестная команда")
    except Exception as e:
        print(f"Ошибка: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
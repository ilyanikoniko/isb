import math
from scipy.special import gammaincc


def frequency_monobit_test(binary_sequence):
    """
    Частотный побитовый тест NIST
    :param binary_sequence: Последовательность(строка) из "0" и "1"
    :return: P-значение последовательности
    """
    n = len(binary_sequence)

    sum_sn= 0

    for bit in binary_sequence:
        sum_sn += 1 if bit == '1' else -1

    normal_sum = abs(sum_sn) / math.sqrt(n)
    p_value = math.erfc(normal_sum / math.sqrt(2))

    return p_value


def runs_test(binary_sequence):
    """
    Тест на одинаковые подряд идущие биты
    :param binary_sequence: Последовательность(строка) из "0" и "1"
    :return: P-значение последовательности
    """
    n = len(binary_sequence)
    if n < 2:
        raise ValueError("Последовательность должна содержать минимум 2 бита")

    ones_count = binary_sequence.count('1')
    zeta = ones_count / n

    if abs(zeta - 0.5) >= (2 / math.sqrt(n)):
        return 0.0  # Последовательность не прошла предварительную проверку

    series = 0
    for i in range(n - 1):
        if binary_sequence[i] != binary_sequence[i + 1]:
            series += 1

    numerator = abs(series - 2 * n * zeta * (1 - zeta))
    denominator = 2 * math.sqrt(2 * n) * zeta * (1 - zeta)
    p_value = math.erfc(numerator / denominator)

    return p_value
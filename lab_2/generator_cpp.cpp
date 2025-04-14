#include <iostream>
#include <fstream>
#include <random>
#include <bitset>
#include <ctime>

using namespace std;

int main() {
    unsigned seed = static_cast<unsigned>(time(nullptr));
    mt19937 gen(seed);
    uniform_int_distribution<> distrib(0, 1);

    // Генерация последовательности из 128 бита
    bitset<128> bits;
    for (int i = 0; i < 128; ++i) {
        bits[i] = distrib(gen);
    }

    // Вывод последовательности в консоль
    cout << "C++ GPSCH (128 bit):\n" << bits << endl;

    // Сохранение последовательности в файл
    ofstream outfile("bin_sequence_cpp.txt");
    if (outfile.is_open()) {
        outfile << bits;
        outfile.close();
        cout << "Sequence saved to bin_sequence_cpp.txt." << endl;
    } else {
        cerr << "Error: Couldn't open the file for writing!" << endl;
        return 1;
    }
    return 0;
}
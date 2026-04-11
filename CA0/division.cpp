using namespace std;
#include <iostream>

int main() {
    long long a, b;
    cin >> a >> b;
    if (b == 0) {
        cout << "division by zero!!\n";
    }
    else {
        cout << a / b << "\n";
    }
    return 0;
}
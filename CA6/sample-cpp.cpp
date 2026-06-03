#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool regular_expression_matching(string T, string P) {
    // Return whether the text string match the pattern
    return true;
}


int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    int tc;
    cin >> tc;
    for (int t = 0; t < tc; t++) {
        string T, P;
        cin >> T >> P;
        bool result = regular_expression_matching(T, P);
        cout << (result ? "YES\n" : "NO\n");
    }
}

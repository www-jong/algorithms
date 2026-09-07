#include <iostream>

using namespace std;

int main(void) {
    int n;
    cin >> n;
    cout << to_string(n) +(n%2?" is odd":" is even");
    return 0;
}
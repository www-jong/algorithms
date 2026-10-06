#include <iostream>
#include <algorithm>
using namespace std;

int answer=0;
int main() {
    int A,B,C;
    cin >> A >> B >> C;
    answer=max(abs(A-B)-1,abs(B-C)-1);
    cout << answer;
    return 0;
}
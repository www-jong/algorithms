#include <iostream>
#include <algorithm>
using namespace std;

int answer=0;
int A,B,x,y;
int main() {
    cin >> A>>B>>x>>y;
    answer=abs(B-A);
    answer=min({answer,abs(A-x)+abs(y-B),abs(A-y)+abs(x-B)});

    cout << answer;
    return 0;
}
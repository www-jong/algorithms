#include <iostream>
using namespace std;

int X,Y;

int func(int n){
    int tmp=0;
    while(n>0){
        tmp+=n%10;
        n/=10;
    }
    return tmp;
}

int main() {
    
    cin >> X >> Y;

    int answer = -1;

    for(int i=X;i<=Y;i++){
        int now = func(i);
        answer=max(answer,now);
    }

    cout << answer;
    return 0;
}
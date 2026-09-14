#include <iostream>
#include <algorithm>
using namespace std;

int A,B,C;
int answer;
int main() {
    cin >>A>>B>>C;
    answer=min(A,B);
    int N=C/A+1;
    int M=C/B+1;
    for(int i=0;i<=N;i++){
        for(int j=0;j<=M;j++){
            int now=A*i+B*j;
            if(now>C){break;}
            answer=max(now,answer);
        }
    }
    cout <<answer;
    return 0;
}
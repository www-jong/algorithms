#include <iostream>
#include <algorithm>
using namespace std;


int N;
int answer=1e9;
int main() {
    cin >>N;
    int X[N];
    int Y[N];
    for(int i=0;i<N;i++){
        int x,y;
        cin >> x>>y;
        X[i]=x;
        Y[i]=y;
    }
    for(int i=0;i<=100;i+=2){
        for(int j=0;j<=100;j+=2){
            int c1,c2,c3,c4;
            c1=0;
            c2=0;
            c3=0;
            c4=0;
            for(int k=0;k<N;k++){
                int x=X[k];
                int y=Y[k];
                if(x<i&&y<j)c1++;
                else if(x<i&&y>j)c2++;
                else if(x>i&&y<j)c3++;
                else c4++;
            }
            answer=min(answer,max({c1,c2,c3,c4}));
        }
    }
    cout << answer;
    return 0;
}
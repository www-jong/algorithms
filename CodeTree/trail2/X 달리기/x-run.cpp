#include <iostream>
#include <algorithm>
using namespace std;

int X;
int answer=1000000;
int check(int v){
    return (1+v)*v/2;
}
int main() {
    cin >> X;
    int time=0;
    int now=0;
    int velo=0;
    while(now!=X){
        if(X>=check(velo+1)+now){
            velo++;
            time++;
            now+=velo;
        }else if(X>=check(velo)+now){
            time++;
            now+=velo;
        }else{
            velo--;
            time++;
            now+=velo;
        }
    }
    cout << time;
    return 0;
}
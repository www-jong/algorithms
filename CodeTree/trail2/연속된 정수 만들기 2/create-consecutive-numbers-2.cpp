#include <iostream>
#include <algorithm>
using namespace std;

int p1,p2,p3;
int a,b,c;
int main() {
    cin >> p1>>p2>>p3;
    int li[3] = {p1, p2, p3};
    sort(li,li+3);
    a=li[0];
    b=li[1];
    c=li[2];
    int check=0;
    if(c-b==1&&b-a==1){
        check=0;
    }
    else if(b-a==2||c-b==2){
        check=1;
    }else{
        check=2;
    }
    cout << check;
    return 0;
}
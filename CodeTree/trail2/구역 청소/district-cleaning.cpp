#include <iostream>
using namespace std;

int a,b,c,d;
int main() {
    cin >>a>>b;
    cin >>c>>d;

    if(b<c||d<a)cout<< (b+d-a-c);
    else{
        cout<<max(b,d)-min(a,c);
    }
    return 0;
}
#include <iostream>
#include <algorithm>
using namespace std;

int N;
int li[101];
int main() {
    cin >> N;
    for(int i=0;i<N;i++){
        int a,b;
        cin >> a >> b;
        for(;a<=b;a++){
            li[a]+=1;
        }
    }
    for(int i=1;i<=100;i++){
        if(li[i]==N){
            cout << "Yes";
            return 0;
        }
    }
    cout << "No";
    return 0;
}
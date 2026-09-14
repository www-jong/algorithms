#include <iostream>
#include <algorithm>
using namespace std;

int N;
int answer[3];
int idx[3];
int main() {
    cin >> N;
    idx[0]=0;
    idx[1]=1;
    idx[2]=2;
    for(int i=0;i<N;i++){
        int a,b,c;
        cin >>a>>b>>c;
        swap(idx[a-1],idx[b-1]);
        answer[idx[c-1]]++;
    }
    cout<<max({answer[0],answer[1],answer[2]});
    return 0;
}
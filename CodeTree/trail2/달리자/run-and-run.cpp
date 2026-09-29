#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N;
int answer=0;
int now=0;
int main() {
    cin >> N;
    int li[N];

    for(int i=0;i<N;i++){
        int t;
        cin >> t;
        li[i]=t;
    }
    for(int i=0;i<N;i++){
        int t;
        cin >> t;
        now+=(li[i]-t);
        if(now>0){
            answer+=now;
        }
    }
    cout << answer;
    return 0;
}
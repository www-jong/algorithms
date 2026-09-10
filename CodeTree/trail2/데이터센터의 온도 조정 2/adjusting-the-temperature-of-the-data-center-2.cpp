#include <iostream>
#include <vector>
using namespace std;

int N,C,G,H;
vector<pair<int,int>> li;
int answer =0;

int func(int x){
    int tmp=0;
    for(int i=0;i<N;i++){
        int Ta=li[i].first;
        int Tb=li[i].second;
        if(x<Ta)tmp+=C;
        else if(x<=Tb)tmp+=G;
        else tmp+=H;
    }
    return tmp;
}

int main() {
    
    cin >> N>>C>>G>>H;

    for(int i=0;i<N;i++){
        int Ta,Tb;
        cin >> Ta>>Tb;
        li.push_back({Ta,Tb});
    }
    for(int i=-1;i<=1001;i++){
        answer=max(answer,func(i));
    }
    cout << answer;
    return 0;
}
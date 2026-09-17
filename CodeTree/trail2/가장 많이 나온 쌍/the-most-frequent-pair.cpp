#include <iostream>
#include <map>

using namespace std;

int N,M;
int answer=0;
map<pair<int,int>,int> d;
int main() {
    cin >> N>>M;
    for(int i=0;i<M;i++){
        int a,b;
        cin >> a>>b;
        pair<int,int> tmp;
        tmp.first=min(a,b);
        tmp.second=max(a,b);
        d[tmp]+=1;
    }
    for(auto [k,v]:d){
        answer=max(answer,v);
    }
    cout << answer;
    return 0;
}
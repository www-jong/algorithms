#include <iostream>
#include <unordered_map>
using namespace std;

string X,Y;
int Xi,Yi;
int func(int i){
    int flag=1;
    unordered_map<char, int> d;
    string tmp=to_string(i);
    for(char j:tmp){
        d[j]+=1;
    }
    if(d.size()>=3||d.size()==1){
        return 0;
    }
    auto it = d.begin();
    int v1 = it->second;
    int v2 = next(it)->second;

    if(v1 != 1 && v2 != 1){
        return 0;
    }
    return 1;
}

int main() {
    int answer=0;
    cin >> X >> Y;
    Xi=stoi(X);
    Yi=stoi(Y);
    for(int i=Xi;i<=Yi;i++){
        answer+=func(i);
    }
    cout << answer;
    return 0;
}
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
string S;
vector<int> v;
vector<int> w;
int answer=0;
int main() {
    cin >> N;
    cin >> S;
    for(int i=0;i<N;i++){
        int t=S[i]-'0';
        if(t==1)v.push_back(i);
        else w.push_back(i);
    }
    for(int i=0;i<w.size();i++){
        for(int j=0;j<w.size();j++){
            if(i==j)continue;
            vector<int> tmp=v;
            int val=10000;
            tmp.push_back(w[i]);
            tmp.push_back(w[j]);
            for(int x=0;x<tmp.size();x++){
                for(int y=0;y<tmp.size();y++){
                    if(x==y)continue;
                    val=min(val,abs(tmp[x]-tmp[y]));
                }
            }
            answer=max(answer,val);
        }
    }
    cout << answer;
    return 0;
}
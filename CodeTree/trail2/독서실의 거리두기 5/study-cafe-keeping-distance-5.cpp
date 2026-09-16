#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> v;
vector<int> w; 
int N;
string S;
int answer=0;

int main() {
    cin >> N;
    cin >> S;
    for(int i=0;i<N;i++){
        if(S[i]=='1'){
            v.push_back(i);
        }else{
            w.push_back(i);
        }
    }

    
    for(int i:w){
        vector<int> v2=v;
        v2.push_back(i);
        sort(v2.begin(),v2.end());
        int now = 1e9;
        for(int x:v2){
            for(int y:v2){
                if(x==y)continue;
                now=min(now,abs(x-y));
            }
        }
        answer=max(answer,now);
    }

    cout << answer;
    return 0;
}
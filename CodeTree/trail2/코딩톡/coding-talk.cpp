#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <set>
#include <vector>
using namespace std;

int N,M,p;
vector<char> li1;
vector<char> li2;

set<char> s;
int main() {
    cin >> N >> M >> p;
    for(int i=0;i<N;i++){
        s.insert('A'+i);
    }
    for(int i=1;i<=M;i++){
        char c;
        int t;
        cin >> c >> t;
        li1.push_back(c);
        li2.push_back(t);
    }
    if(li2[p-1]==0){
        return 0;
    }
    for(int i=p-1;i<M;i++){
        s.erase(li1[i]);
    }
    for(int i=p-2;i>=0;i--){
        if(li2[p-1]==li2[i]){
            s.erase(li1[i]);
        }else{
            break;
        }
    }
    for(char i:s){
        cout << i << " ";
    }
    return 0;
}
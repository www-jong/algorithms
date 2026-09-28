#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;
unordered_map<int,int> d;
int answer=0;
int N;
int main() {
    cin >> N;
    for(int i=0;i<N;i++){
        int a,b;
        cin >>a>>b;
        if(d.find(a)!=d.end()){
            if(d[a]!=b){
                answer++;
            }        
        }
        d[a]=b;
    }
    cout << answer;
    return 0;
}
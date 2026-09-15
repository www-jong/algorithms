#include <iostream>
#include <unordered_set>

using namespace std;

int N;
string S;
int main() {
    cin >> N;
    cin >> S;
    
    for(int i=1;i<=N;i++){
        unordered_set<string> tmp;
        for(int j=0;j<N-i+1;j++){
            tmp.insert(S.substr(j,i));
        }
        if(tmp.size()==N-i+1){
            cout << i;
            return 0;
        }
    }
    cout << N;
    return 0;
}
#include <iostream>
#include <vector>

using namespace std;

int T,a,b;
vector<int> s;
vector<int> n;
int answer=0;
int main() {
    
    cin >> T>>a>>b;
    for(int i=0;i<T;i++){
        char c;
        int x;
        cin >> c>>x;
        if(c=='S'){
            s.push_back(x);
        } 
        else{
            n.push_back(x);
        }   
    }
    for(int i=a;i<=b;i++){
        int d1=1e9;
        int d2=1e9;
        for(int j:s){
            d1=min(d1,abs(i-j));
        }
        for(int j:n){
            d2=min(d2,abs(i-j));
        }
        if(d1<=d2){
            answer++;
        }
    }
    cout << answer;
    return 0;
}
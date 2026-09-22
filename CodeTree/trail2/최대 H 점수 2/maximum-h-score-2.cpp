#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N,L;
int main() {
    cin >> N >> L;
    int answer=0;
    vector<int> li;
    for(int i=0;i<N;i++){
        int t;
        cin >> t;
        li.push_back(t);
    }
    sort(li.begin(),li.end());
    for(int i=1;i<=N;i++){
        int cnt=0;
        int val=0;
        for(int j:li){
            if (j>=i){
                cnt++;
            }
            else if (j+1>=i){
                val++;
            }
        }
        cnt += min(L,val);
        if (cnt>=i){
            answer = i;
        }
    }
    cout << answer;
    return 0;
}
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int N,K;
vector<int> li;
int answer=0;
int main() {
    cin >> N >> K;
    for(int i=0;i<N;i++){
        int x;
        cin >> x;
        li.push_back(x);
    }
    sort(li.begin(), li.end());
    int st=0;
    for(int end=0;end<N;end++){
        if(li[end]-li[st]>K){
            st++;
        }
        answer=max(answer,end-st+1);
    }
    cout << answer;
    return 0;
}
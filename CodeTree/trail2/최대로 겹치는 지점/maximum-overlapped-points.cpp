#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    vector<pair<int,int>> li;
    for(int i=0;i<n;i++){
        int a,b;
        cin >>a>>b;
        li.push_back({a,1});
        li.push_back({b,-1});
    }

    sort(li.begin(),li.end(),[](const auto&a,const auto&b){
        if(a.first!=b.first) return a.first<b.first;
        return a.second>b.second;
    });

    int answer=0;
    int cnt=0;
    for(auto a:li){
        cnt+=a.second;
        answer=max(cnt,answer);
    }
    cout << answer;
    return 0;
}
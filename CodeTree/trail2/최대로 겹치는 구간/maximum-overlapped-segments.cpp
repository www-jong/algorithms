#include <iostream>
#include <vector>
using namespace std;

int n;


int main() {
    // Please write your code here.
    cin >> n;
    int answer =0;
    vector<pair<int,int>> li;
    li.resize(n);
    for(int i=0;i<n;i++){
        int a,b;
        cin >>a>>b;
        li[i]={a,b};
    }
    for(int i=-100;i<100;i++){
        int cnt=0;
        float t=i+0.5;
        for(int j=0;j<n;j++){
            if(li[j].first<t&&t<li[j].second){
                cnt++;
            }
        }
        answer=cnt>answer?cnt:answer;
    }
    cout << answer;
    return 0;
}
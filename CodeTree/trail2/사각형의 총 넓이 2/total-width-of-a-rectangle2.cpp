#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int li[201][201];
int N;
int answer=0;
vector<pair<int,int>> dp[201];
int main() {
    cin >> N;
    for(int i=0;i<N;i++){
        int x1,y1,x2,y2;
        cin >>x1>>y1>>x2>>y2;
        x1+=100;
        x2+=100;
        y1+=100;
        y2+=100;
        for(int i=x1;i<x2;i++){
            dp[i].push_back({y1,y2});
        }
    }
    for(int i=0;i<201;i++){
        if(dp[i].empty())continue;

        int now=0;
        sort(dp[i].begin(),dp[i].end());

        int left=dp[i][0].first;
        int right=dp[i][0].second;
        for(int j=0;j<dp[i].size();j++){
            int next_left=dp[i][j].first;
            int next_right=dp[i][j].second;
            if(next_left>right){//new 구간
                now+=right-left;
                left=next_left;
                right=next_right;
            }else{//구간연장
                right=max(right,next_right);
            }
        }
        now+=right-left;
        answer+=now;
    }

    cout << answer;
    return 0;
}
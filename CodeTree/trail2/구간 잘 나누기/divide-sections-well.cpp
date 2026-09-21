#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N,M;
vector<int> li;
vector<int> sli;

int main() {
    cin >> N >> M;
    vector<vector<int>> dp(N + 1, vector<int>(M+1,100000));
    li.resize(N+1);
    sli.resize(N+1);
    for(int i=0;i<N;i++){
        int tmp;
        cin >> tmp;
        li[i+1]=tmp;
        sli[i+1]=sli[i]+tmp;
    }
    dp[0][0]=0;
    // dp[j][i] = j까지 i개 토막으로 나눠져있을 때 가장큰 토막의 최소값
    for(int i=1;i<=M;i++){
        for(int j=1;j<=N;j++){
            for(int k=i-1;k<j;k++){
                int val=sli[j]-sli[k];
                dp[j][i]=min(dp[j][i],max(dp[k][i-1],val));
            }
        }
    }
    cout << dp[N][M];
    return 0;
}
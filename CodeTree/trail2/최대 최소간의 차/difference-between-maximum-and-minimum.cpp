#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int N,K;
vector<int> li;
int dp_up[10001];
int dp_down[10001];
int cnt[10001];
int answer=INT_MAX;
int min_idx=10001;
int max_idx=0;
int main() {
    cin >> N >> K;
    for(int i=0;i<N;i++){
        int tmp;
        cin >> tmp;
        li.push_back(tmp);
        cnt[tmp]++;
        min_idx=min(min_idx,tmp);
        max_idx=max(max_idx,tmp);
    }
    sort(li.begin(),li.end());

    int cnt_up=0,cnt_down=cnt[10000];
    for(int i=1;i<=10000;i++){
        int di=10000-i;
        dp_up[i]=dp_up[i-1]+cnt_up;
        dp_down[di]=dp_down[di+1]+cnt_down;
        cnt_up+=cnt[i];
        cnt_down+=cnt[di];
    }
    while(min_idx+K<=max_idx){
        answer=min(answer,dp_up[min_idx]+dp_down[min_idx+K]);
        min_idx++;
    }
    /*
    cout << dp_up[3];
    cout << dp_up[4];
    cout << dp_up[6] << "\n";
    cout << dp_down[9885];
    cout << dp_down[6];
    cout << dp_down[5];
    */
    if(answer==INT_MAX)answer=0;
    cout << answer;
    return 0;
}
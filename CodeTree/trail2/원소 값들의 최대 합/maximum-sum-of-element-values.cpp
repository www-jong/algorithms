#include <iostream>
using namespace std;


int N,M;
int answer=0;
int main() {
    
    cin >> N>>M;
    int li[N+1];
    for(int i=1;i<=N;i++){
        cin >> li[i];
    }
    for(int st=1;st<=N;st++){
        int cnt=1;
        int now=st;
        int flag=0;
        int tmp=li[now];
        while(cnt<M){
            int next=li[now];
            if(next==st&&!flag){
                tmp=tmp*(M/cnt);
                cnt=(M/cnt)*cnt;
                flag=1;
            }
            if(cnt==M)break;
            now=next;
            tmp+=li[next];
            cnt++;
        }
        answer=max(answer,tmp);
    }
    cout << answer;
    return 0;
}
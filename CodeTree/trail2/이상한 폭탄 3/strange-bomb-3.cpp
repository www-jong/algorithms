#include <iostream>
#include <unordered_set>
#include <map>
#include <vector>
using namespace std;

int N,K;
unordered_set<int> S;
map<int,vector<int>> d;
int main() {
    cin >> N>>K;
    int li[N];
    int max_v=0;
    int answer=0;
    for(int i=0;i<N;i++){
        int tmp;
        cin >> tmp;
        li[i]=tmp;
        S.insert(tmp);
        d[tmp].push_back(i);
    }

    for(int i:S){
        int tmp_v=0;
        int tmp_answer=0;
        int before=-200;
        int flg=0;
        for(int j:d[i]){
            if(j-before<=K){
                tmp_v+=1;
                if(!flg){
                    tmp_v+=1;
                    flg=1;
                }
            }else{
                flg=0;
            }
            before=j;
        }
        if(tmp_v>max_v&&tmp_v!=0){
            max_v=tmp_v;
            answer=i;
        }else if(tmp_v==max_v&&tmp_v!=0){
            if(answer<i){
                answer=i;
            }
        }
    }
    cout << answer;
    return 0;
}
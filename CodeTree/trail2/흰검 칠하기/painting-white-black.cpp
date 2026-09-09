#include <iostream>
#include <vector>
using namespace std;


int N;
const int MAX=200002;
int now=100000;

int li_w[MAX];
int li_b[MAX];
int li[MAX];
vector<int> answer(3);
int main() {
    cin >> N;
    
    for(int j=0;j<N;j++){
        int a;
        char b;
        cin >> a>>b;
        if(b=='L'){
            for(int i=0;i<a;i++){
                if(li[now]!=3){
                    li_w[now]++;
                    if(li_w[now]>=2&&li_b[now]>=2){
                        li[now]=3;
                    }else{
                        li[now]=1;
                    }
                }
                if(i<a-1)now--;
            }
        }else{
            for(int i=0;i<a;i++){
                if(li[now]!=3){
                    li_b[now]++;
                    if(li_w[now]>=2&&li_b[now]>=2){
                        li[now]=3;
                    }else{
                        li[now]=2;
                    }
                }
                if(i<a-1)now++;
            }
        }
    }

    for(int i=0;i<MAX;i++){
        if(li[i]==1){
            answer[0]++;
        }else if(li[i]==2){
            answer[1]++;
        }else if(li[i]==3){
            answer[2]++;
        }
    }
    cout << to_string(answer[0])+" " << to_string(answer[1])+" " << to_string(answer[2]);
    return 0;
}
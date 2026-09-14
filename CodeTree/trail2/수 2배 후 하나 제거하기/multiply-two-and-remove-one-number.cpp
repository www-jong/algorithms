#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
int answer=1e9;
int main() {
    cin >> N;
    vector<int> li(N);
    for(int i=0;i<N;i++){
        cin >> li[i];
    }
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            int tmp=0;
            for(int k=0;k<N-1;k++){
                int a,b;
                if(k==j){continue;}
                else if(k==i){a=li[k]*2;}
                else{a=li[k];}
                if(k+1==j){
                    if(k+1==N-1){
                        continue;
                    }
                    if(k+2==i){
                        b=li[k+2]*2;
                    }else{
                        b=li[k+2];
                    }
                }else if(k+1==i){
                    b=li[k+1]*2;
                }else{
                    b=li[k+1];
                }
                tmp+=abs(a-b);
            }
            answer=min(answer,tmp);
        }
    }
    cout << answer;
    return 0;
}
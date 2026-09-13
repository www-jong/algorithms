#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
int answer=0;
int main() {

    cin >> N;
    vector<int> li(N);
    int min_v=100;
    int max_v=1;
    
    for(int i=0;i<N;i++){
        cin >> li[i];
        min_v=min(min_v,li[i]);
        max_v=max(max_v,li[i]);
    }
    for(int i=min_v;i<=max_v;i++){
        int tmp=0;
        for(int j=0;j<N;j++){
            for(int k=j+1;k<N;k++){
                if(li[j]+li[k]==2*i){
                    tmp++;
                }
            }
        }
        answer=max(answer,tmp);
    }

    cout << answer;

    return 0;
}
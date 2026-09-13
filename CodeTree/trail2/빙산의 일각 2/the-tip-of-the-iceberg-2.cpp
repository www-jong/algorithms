#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
int answer=0;
int main() {
    cin >> N;
    vector<int> li(N);
    
    int max_h=0;
    for(int i=0;i<N;i++){
        cin >> li[i];
        max_h=max(max_h,li[i]);
    }

    for(int i=0;i<max_h;i++){
        int tmp=0;
        int check=0;
        for(int j=0;j<N;j++){
            if(li[j]>i){
                if(check==0){
                    tmp++;
                    check=1;
                }
            }else{
                check=0;
            }
        }
        answer=max(answer,tmp);
    }
    cout << answer;
    return 0;
}
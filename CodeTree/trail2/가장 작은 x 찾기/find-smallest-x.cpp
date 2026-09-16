#include <iostream>
#include <vector>
using namespace std;

int N;

int answer=1e9;
int main() {
    cin >> N;
    int a,b;
    cin >> a>>b;
    vector<int> li(b-a+1);
    vector<int> original(b-a+1);
    for(int i=a;i<=b;i++){
        if(i%2==0){
            li[i-a]=i*2;
            original[i-a]=i/2;
        }
    }

    for(int i=0;i<N-1;i++){
        int a,b;
        cin >> a>>b;
        for(int j=0;j<li.size();j++){
            if(li[j]!=0){
                if(a<=li[j]&&li[j]<=b){
                    li[j]*=2;
                }else{
                    li[j]=0;
                }
            }
        }
        
    }
    for(int i=0;i<li.size();i++){
        if(li[i]!=0){
            answer=min(answer,original[i]);
        }
    }
    cout << answer;
    return 0;
}
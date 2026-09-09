#include <iostream>
#include <vector>
using namespace std;


const int MAX=200002;


int now=100000;
int arr[200002];

int N;
vector<int> answer(2);
int main() {
    cin >> N;
    for(int i=0;i<N;i++){
        int a;
        char b;
        cin >> a>>b;
        if(b=='L'){
            for(int j=0;j<a;j++){
                arr[now]=1;
                if(j!=a-1)now--;
            }
        }else{
            for(int j=0;j<a;j++){
                arr[now]=2;
                if(j!=a-1)now++;
            }
        }
    }
    for(int i=0;i<200002;i++){
        if(arr[i]==1){
            answer[0]++;
        }else if(arr[i]==2){
            answer[1]++;
        }
    }
    cout << answer[0] <<' '<<answer[1];
    return 0;
}
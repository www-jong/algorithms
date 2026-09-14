#include <iostream>
#include <vector>
using namespace std;

int X,Y;
int answer=0;
int main() {
    cin >> X>>Y;
    for(int i=X;i<=Y;i++){
        string v=to_string(i);
        int v_len=v.size();
        int flag=0;
        for(int j=0;j<(v_len+1)/2;j++){
            if(v[j]!=v[v_len-1-j]){
                flag=1;
                break;
            }
        }
        if(not flag)answer++;
    }
    cout << answer;
    return 0;
}
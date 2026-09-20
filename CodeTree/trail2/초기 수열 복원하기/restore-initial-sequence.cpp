#include <iostream>
#include <vector>
using namespace std;

int N;
int main() {
    cin >> N;
    vector<int> li;
    for(int i=0;i<N-1;i++){
        int x;
        cin >> x;
        li.push_back(x);
    }
    for(int i=1;i<=N;i++){
        vector<int> tmp(N);
        vector<int> check(N+1,0);
        int flag=1;
        tmp[0]=i;
        check[i]=1;
        for(int j=0;j<N-1;j++){
            tmp[j+1]=li[j]-tmp[j];
            if(tmp[j+1]<1||tmp[j+1]>N||check[tmp[j+1]]){
                flag=0;
                break;
            }
            check[tmp[j+1]]=1;
        }
        if(flag){
            for(int j=0;j<N;j++){
                cout << tmp[j] << (j==N-1?"":" ");
            }
            cout << "\n";
            return 0;
        }
    }

    return 0;
}
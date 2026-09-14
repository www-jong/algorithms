#include <iostream>
#include <vector>
#include <set>
using namespace std;


int N;
vector<pair<int,int>> li;
int main() {
    cin >> N;
    set<int> Sx;
    set<int> Sy;
    for(int i=0;i<N;i++){
        int x,y;
        cin >> x>>y;
        li.push_back({x,y});
        Sx.insert(x);
        Sy.insert(y);
    }
    for(int i=0;i<=10;i++){
        for(int j=0;j<=10;j++){
            for(int k=0;k<=10;k++){
                int f1=N;
                int f2=N;
                int f3=N;
                int f4=N;
                for(int v=0;v<N;v++){
                    int x=li[v].first;
                    int y=li[v].second;
                    if(x==i||x==j||x==k){
                        f1-=1;
                    }
                    if(x==i||x==j||y==k){
                        f2-=1;
                    }
                    if(x==i||y==j||y==k){
                        f3-=1;
                    }
                    if(y==i||y==j||y==k){
                        f4-=1;
                    }
                }
                if(f1==0||f2==0||f3==0||f4==0){
                    cout << 1;
                    return 0;
                }
                
            }
        }
    }
    cout << 0;
    return 0;
}
#include <iostream>
#include <unordered_set>
#include <algorithm>
using namespace std;

int A=0;
int B=0;
int C=0;
int D=0;
unordered_set<int> S;
int check(int a,int b,int c,int d){
    int tmp_li[4]={a,b,c,d};
    for(int i=1;i<=15;i++){
        int tmp=0;
        for(int j=0;j<4;j++){
            if(i&(1<<j)){
                tmp+=tmp_li[j];
            }
        }
        if(S.find(tmp)==S.end())return 0;
    }
    return 1;
}
int main() {
    int li[15];
    for(int i=0;i<15;i++){
        cin >> li[i];
        S.insert(li[i]);
    }
    sort(li,li+15);
    for(int a=0;a<15;a++){
        for(int b=a+1;b<15;b++){
            for(int c=b+1;c<15;c++){
                for(int d=c+1;d<15;d++){
                    if(a==b||a==c||a==d||b==c||b==d||c==d)continue;
                    int flag=check(li[a],li[b],li[c],li[d]);
                    if(flag){
                        cout << li[a]<< " " << li[b]<< " " << li[c]<< " " << li[d];
                        return 0;
                    }
                }
            }
        }
    }
    return 0;
}
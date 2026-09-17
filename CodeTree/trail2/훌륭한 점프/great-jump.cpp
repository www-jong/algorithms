#include <iostream>
using namespace std;

int N,K;
int d[101];
int INF = 1e9;
int main() {
    cin >> N >> K;
    int li[N];
    for(int i=0;i<N;i++){
        cin >> li[i];
        d[i]=INF;
    }
    d[0]=li[0];
    for(int i=0;i<N;i++){
        for(int j=i+1;j<=i+K;j++){
            d[j]=min(d[j],max(d[i],li[j]));
        }
    }
    cout << d[N-1];
    return 0;
}
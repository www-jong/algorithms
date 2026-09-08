#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n;
int k;

int main() {
    cin >> n >> k;
    vector<int> li(n);
    int answer = 0;
    for(int i=0;i<k;i++){
        int a,b;
        cin >> a >> b;
        for(int j=a-1;j<b;j++){
            li[j]++;
        }
    }
    for(int i=0;i<n;i++){
        answer=max({answer,li[i]});
    }
    cout << answer;
    return 0;
}
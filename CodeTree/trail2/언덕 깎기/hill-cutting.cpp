#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
vector<int> li;
int answer=1000000;
int main() {
    cin >> N;
    for(int i=0;i<N;i++){
        int x;
        cin >> x;
        li.push_back(x);
    }
    sort(li.begin(),li.end());
    int min_v=li[0];
    int max_v=li[li.size()-1];
    int gap=max_v-min_v;
    if(gap<=17){
        cout << 0;
        return 0;
    }
    for(int i=0;i<=gap-17;i++){
        int j=gap-17-i;
        int minimum=min_v+i;
        int maximum=max_v-j;
        int cost=0;
        for(int i:li){
            if(minimum<=i&&i<=maximum){continue;}
            else if(i<minimum){cost+=(minimum-i)*(minimum-i);}
            else{cost+=(i-maximum)*(i-maximum);}
        }

        answer=min(answer,cost);

    }
    cout << answer;
    return 0;
}
#include <iostream>
#include <set>
using namespace std;

set<pair<int,int>> s;
int li[3][3];

void func(set<int> v){
        if(v.size()==2){
            pair<int,int> tmp_pair;
            tmp_pair.first=*v.begin();
            tmp_pair.second=*next(v.begin());
            s.insert(tmp_pair);
        }
}

int main() {
    set<int> tmp1;
    set<int> tmp2;
    for(int i=0;i<3;i++){
        string x;
        cin >> x;
        li[i][0]=x[0]-'0';
        li[i][1]=x[1]-'0';
        li[i][2]=x[2]-'0';
        tmp1.insert(li[i][i]);
        tmp2.insert(li[i][2-i]);
    }
    func(tmp1);
    func(tmp2);
    for(int x=0;x<3;x++){
        set<int> tmp1;
        set<int> tmp2;
        for(int y=0;y<3;y++){
            tmp1.insert(li[x][y]);
            tmp2.insert(li[y][x]);
        }
        
        func(tmp1);
        func(tmp2);

    }
    cout << s.size();
    return 0;
}
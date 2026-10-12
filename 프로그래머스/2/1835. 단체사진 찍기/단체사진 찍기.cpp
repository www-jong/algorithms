#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int n, vector<string> data) {
    int answer = 0;
    unordered_map<char, int> people = {
        {'A', 0},
        {'C', 1},
        {'F', 2},
        {'J', 3},
        {'M', 4},
        {'N', 5},
        {'R', 6},
        {'T', 7}
    };
    
    vector<int> people_idx={0,1,2,3,4,5,6,7};
    vector<vector<char>> li(data.size(), vector<char>(3, 0));

    for(int i=0;i<data.size();i++){
        li[i]={data[i][0],data[i][2],data[i][3],data[i][4]};
    }
    
    do {
        int flag=0;
        for(int i=0;i<li.size();i++){
            int A=people_idx[people[li[i][0]]];
            int B=people_idx[people[li[i][1]]];
            int val=li[i][3]-'0';
            int gap=abs(A-B)-1;
            if(li[i][2]=='<'){
                if(gap>=val){
                    flag=1;
                    break;
                }
            }else if(li[i][2]=='>'){
                if(gap<=val){
                    flag=1;
                    break;
                }
            }else{
                if(gap!=val){
                    flag=1;
                    break;
                }
            }
        }
        if(!flag){
            answer++;
        }
    } while (next_permutation(people_idx.begin(), people_idx.end()));
    return answer;
}
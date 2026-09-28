#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(int k, vector<int> score) {
    vector<int> li;
    vector<int> answer;
    for(int i:score){
        li.push_back(i);
        sort(li.rbegin(),li.rend());
        if(li.size()<=k){
            answer.push_back(li.back());
        }else{
            li.pop_back(); 
            answer.push_back(li.back());
        }
    }
    return answer;
}
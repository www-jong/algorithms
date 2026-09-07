#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(vector<string> str_list, string ex) {
    string answer;
    for(string i:str_list){
        if(i.find(ex)==string::npos){
            answer+=i;
        }
    }
    return answer;
}
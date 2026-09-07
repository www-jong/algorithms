#include <string>
#include <vector>
#include <sstream>

using namespace std;

vector<string> solution(string my_string) {
    vector<string> answer;
    stringstream s(my_string);
    string i;
    while(s>>i){
        answer.push_back(i);
    }
    return answer;
}
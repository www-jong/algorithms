#include <string>
#include <vector>
#include <cctype>
#include <algorithm>

using namespace std;

vector<string> solution(vector<string> strArr) {
    vector<string> answer;
    for(int i=0;i<strArr.size();i++){
        transform(strArr[i].begin(),strArr[i].end(),strArr[i].begin(),i%2?::toupper: ::tolower);
    }
    return strArr;
}
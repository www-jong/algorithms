#include <string>
#include <vector>
#include <cctype>

using namespace std;

string solution(string my_string, string alp) {
    string answer = "";
    for(char i:my_string){
        if(i!=alp[0]){
            answer+=i;
        }else{
            answer+=toupper(i);
        }
    }
    return answer;
}
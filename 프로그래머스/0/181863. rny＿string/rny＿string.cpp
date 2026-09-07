#include <string>
#include <vector>

using namespace std;

string solution(string rny_string) {
    string answer = "";
    for(char i:rny_string){
        answer+=i=='m'?"rn":string(1,i);
    }
    return answer;
}
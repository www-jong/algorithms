#include <string>
#include <vector>

using namespace std;

int solution(string my_string, string is_suffix) {
    if(my_string.size()>=is_suffix.size()){
    return my_string.substr(my_string.size()-is_suffix.size())==is_suffix?1:0;
        }else{
        return 0;
    }
}
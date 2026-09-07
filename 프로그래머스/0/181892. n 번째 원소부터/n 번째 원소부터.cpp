#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list, int n) {
    
    vector<int> answer;
    n-=1;
    for(;n<num_list.size();n++){
        answer.push_back(num_list[n]);
    }
    return answer;
}
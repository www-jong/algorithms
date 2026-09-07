#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
    int N = num_list.size();
    for(int i=0;i<N;i++){
        if(num_list[i]<0){
            return i;
        }
    }
    return -1;
}
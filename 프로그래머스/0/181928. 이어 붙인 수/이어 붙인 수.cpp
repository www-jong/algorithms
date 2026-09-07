#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
    int answer = 0;
    string a,b;
    for(int i:num_list){
        if(i%2){
            a+=to_string(i);
        }else{
            b+=to_string(i);
        }
    }
    printf("%s, %s",a.c_str(),b.c_str());
    return stoi(a)+stoi(b);
}
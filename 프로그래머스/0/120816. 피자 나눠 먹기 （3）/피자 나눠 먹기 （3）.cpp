#include <string>
#include <vector>

using namespace std;

int solution(int slice, int n) {
    for(int i = 0 ; i<=50;i++){
        if(slice*i>=n){
            return i;
        }
    }
}
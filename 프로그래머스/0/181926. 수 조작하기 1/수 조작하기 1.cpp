#include <string>
#include <vector>

using namespace std;

int solution(int n, string control) {
    for(char i:control){
        if(i=='w'){
            n+=1;
        }else if(i=='s'){
            n-=1;
        }else if(i=='d'){
            n+=10;
        }else{
            n-=10;
        }
    }
    return n;
}
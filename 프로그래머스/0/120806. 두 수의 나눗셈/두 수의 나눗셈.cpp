#include <string>
#include <iostream>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    double answer = (double)num1/num2;
    cout << answer;
    return answer*1000/1;
}
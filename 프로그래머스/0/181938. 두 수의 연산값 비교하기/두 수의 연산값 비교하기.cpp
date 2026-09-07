#include <string>
#include <vector>

using namespace std;

int solution(int a, int b) {
    int A=stoi(to_string(a)+to_string(b));
    return A>=2*a*b?A:2*a*b;
}
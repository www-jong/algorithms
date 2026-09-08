#include <string>
#include <vector>
#include <cstdlib>
using namespace std;

int solution(int a, int b) {
    return a%2?(b%2?a*a+b*b:2*(a+b)):(b%2?2*(a+b):abs(a-b));
}
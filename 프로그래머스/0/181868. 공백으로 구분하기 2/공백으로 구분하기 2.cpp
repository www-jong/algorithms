#include <string>

#include <vector>



using namespace std;



vector<string> solution(string my_string) {

    vector<string> answer;

    

    for (int i = 0; i < my_string.size(); ++i) {

        if (my_string[i] == ' ')

            continue;

        

        auto it = my_string.find(" ", i);

        

        if (it != string::npos) {

            answer.push_back(my_string.substr(i, it - i));

            i = it;

        }

        else {

            answer.push_back(my_string.substr(i, my_string.size() - i));

            break;

        }

        

    }

    return answer;

}
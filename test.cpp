#include <iostream>
using namespace std;

string getArg(vector<string>& input, string target) {
    auto it = std::find(input.begin(), input.end(), target);

    if (it != input.end()) {
        // String found
        int index = std::distance(input.begin(), it);
        
        if (input.size() > index + 1) {
            string value = input[index + 1];

            if (value.size() < 2 || value[0] != '<' || value[value.size() - 1] != '>')
                throw "bad request";
            else
                return value.substr(1, value.size() - 2)
        }
        else
            throw "Bad request";
    } else {
        return "";
    }
}

int main() {
    string s = "id <13> age <23>";
    
}
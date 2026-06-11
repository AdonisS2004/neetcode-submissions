class Solution {
public:

    string encode(vector<string>& strs) {
        string res = "";
        // format: number of characters after the number with #
        for(string str: strs){
            int len = str.size();
            res = res + to_string(len) + "#" + str;
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;

        string current_num = "";
        int current_len = 0;
        string curent_string = "";

        int idx = 0;
        int max = s.size();
        while (idx < max){
            while(s[idx] != '#'){
                current_num = current_num + s[idx];
                idx++;
            }
            current_len = stoi(current_num);
            idx++;
            while(current_len > 0){
                curent_string = curent_string + s[idx];
                idx++;
                current_len--;
            }
            res.push_back(curent_string);
            curent_string = "";
            current_num = "";
        }
        return res;
    }
};

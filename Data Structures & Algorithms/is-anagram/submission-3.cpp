class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map <char, int> comparison;
        if (s.length() != t.length()){
            return false;
        }

        for (char c: s){
            if (comparison.count(c)){
                comparison[c]++;
            } else {
                comparison[c] = 1;
            }
        }

        for (char c: t){
            if (comparison.find(c) == comparison.end() ||  
            comparison.find(c) -> second == 0){
                return false;
            } else {
                comparison[c]--;
            }
        }

        return true;
    }
};

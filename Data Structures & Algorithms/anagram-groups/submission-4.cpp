class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) { 
       unordered_set<int> visited; // O(m)
       unordered_map<string, unordered_map<char, int>> frequencies; //O(m*26)
       vector<vector<string>> res; // O(m)

        // build frequency table
       for(const string& str: strs){
            if (frequencies.find(str) != frequencies.end()){
                continue;
            }
            unordered_map<char, int> char_count;
            for(char c: str){
                char_count[c]++;
            }
            frequencies[str] = char_count;
       }

        // use frequency table
       for(int i = 0; i < strs.size(); i++){
            string str1 = strs[i];
            if (visited.find(i) != visited.end()){
                continue;
            }
            vector<string> anagrams; // new anagrams vector
            anagrams.push_back(str1); 
            visited.insert(i); // str1 index visited
            for(int j = 0; j < strs.size(); j++){
                string str2 = strs[j];
                bool addStr = true;
                if (visited.find(j) != visited.end() || str1.size() != str2.size()){
                    continue;
                }
                for(const auto& [key, value]: frequencies[str2]){
                    if(frequencies[str1].find(key) == frequencies[str1].end()
                    || frequencies[str1][key] != value){
                        addStr = false;
                    }
                }
                if(addStr){
                    anagrams.push_back(str2);
                    visited.insert(j);
                }
            }
            res.push_back(anagrams);
       }
       return res;
    }
};

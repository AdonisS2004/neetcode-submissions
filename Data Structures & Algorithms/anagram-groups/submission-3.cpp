class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) { 
       unordered_set<int> seen; // O(m)
       unordered_map<string, unordered_map<char, int>> char_counts; //O(m*26)
       vector<vector<string>> res; // O(m)

        // build frequency table
       for(const string& str: strs){
            if (char_counts.find(str) != char_counts.end()){
                continue;
            }
            unordered_map<char, int> char_count;
            for(char c: str){
                char_count[c]++;
            }
            char_counts[str] = char_count;
       }

        // use frequency table
       for(int i = 0; i < strs.size(); i++){
            string str1 = strs[i];
            if (seen.find(i) != seen.end()){
                continue;
            }
            vector<string> anagrams; // new anagrams vector
            anagrams.push_back(str1); 
            seen.insert(i); // str1 index seen
            for(int j = 0; j < strs.size(); j++){
                string str2 = strs[j];
                bool addStr = true;
                if (seen.find(j) != seen.end() || str1.size() != str2.size()){
                    continue;
                }
                for(const auto& [key, value]: char_counts[str2]){
                    if(char_counts[str1].find(key) == char_counts[str1].end()
                    || char_counts[str1][key] != value){
                        addStr = false;
                    }
                }
                if(addStr){
                    anagrams.push_back(str2);
                    seen.insert(j);
                }
            }
            res.push_back(anagrams);
       }

       return res;
    }
};

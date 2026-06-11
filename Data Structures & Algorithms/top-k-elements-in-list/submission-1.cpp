class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> res;
        unordered_map<int, int> frequencies;
        unordered_map<int, vector<int>> freq2items;
        int count = k;
        for (int num: nums){
            frequencies[num]++;
        }

        for(const auto& [key, value]: frequencies){
            freq2items[value].push_back(key);
        }

        for(int i = nums.size(); i >= 0; i--){
            if(freq2items.find(i) != freq2items.end()){
                vector<int> current = freq2items[i];
                for(int num:current){
                    if(count > 0){
                        res.push_back(num);
                        count--;
                    }
                }
            }
        }

        return res;
    }
};

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        vector<int> res;
        for(int i = 0; i<nums.size(); i++){
            if (seen.find(target - nums[i]) != seen.end()){
                res.push_back(seen[target - nums[i]]);
                res.push_back(i);
                return res;
            }
            seen[nums[i]] = i;
        }
        return res;
    }
};

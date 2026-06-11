class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int longest = 0;
        unordered_set<int> nums_set(nums.begin(), nums.end());
        unordered_set<int> seen;

        for(int num: nums){
            if (seen.find(num) != seen.end()){
                continue;
            }

            int current_longest = 1;
            int current_num = num;
            bool goLeft = true;
            bool goRight = true;
            seen.insert(current_num);

            while (nums_set.find(current_num - 1) != nums_set.end()) {
                current_longest++;
                current_num = current_num - 1;
                seen.insert(current_num);
            }
            current_num = num;
            while (nums_set.find(current_num + 1) != nums_set.end()) {
                current_longest++;
                current_num = current_num + 1;
                seen.insert(current_num);
            }

            if (current_longest > longest) {
                longest = current_longest;
            }
        }
        return longest;
    }
};

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res;
        vector<int> prefix_products;
        vector<int> suffix_products;

        prefix_products.push_back(1);
        suffix_products.push_back(1);

        int len = nums.size();
        
        for(int i = 0; i < len-1; i++){
            prefix_products.push_back(prefix_products[i]*nums[i]);
        }

        for(int i = 0; i < len; i++){
            suffix_products.push_back(suffix_products[i]*nums[len-1-i]);
        }
        for(int i = 0; i < len; i++){
            res.push_back(prefix_products[i]*suffix_products[len-1-i]);
        }
        return res;
    }
};

class Solution {
public:
    vector<int> minSubsequence(vector<int>& nums) {
        vector<int> res, freq(101, 0);
        int sumres = 0, sumleft = accumulate(begin(nums), end(nums), 0);
        
        for(auto n: nums)
            freq[n]++;
        
        for (int n = 100; n>= 1; n--){
            while(freq[n]-->0 && sumres<=sumleft){
                sumres += n;
                sumleft -= n;
                res.push_back(n);
            }
        }
        return res;
    }
};
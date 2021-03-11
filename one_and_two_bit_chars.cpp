// https://leetcode.com/problems/1-bit-and-2-bit-characters/discuss/1021841/Fastest-and-Easy-C%2B%2B-solution-(100-space-and-time)

class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        int i = 0;
        int n = bits.size();
        while (i < n - 1){
            if(bits[i] == 0){
                i = i+1;
            }
            else{
                i+=2;
            }
        }
        if(i == n){
            return false;
        }
        else if(i == n-1){
            return true;
        }
        return true;
    }
};
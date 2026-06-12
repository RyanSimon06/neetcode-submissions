#include <unordered_set>
#include <vector>

class Solution {
    public:
        bool hasDuplicate(vector<int>& nums) {
            std::unordered_set<int> seen;
            seen.reserve(nums.size());

            for (int n : nums) {
                if (!seen.insert(n).second)
                    return true;
            }

            return false;
        }
};

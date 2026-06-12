#include <set>
#include <vector>

using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> seen;

        for (int i = 0; i < nums.size(); i++) {
            cout << nums[i] << endl;
            if (!seen.insert(nums[i]).second) {
                return true;
            }
        }
        return false;
    }
};
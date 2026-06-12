use std::collections::HashMap;

impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut seen = HashMap::new();

        for n in nums {
            if seen.contains_key(&n) {
                return true;
            }
            else {
                seen.insert(n, true);
            }
        }   
        false
    }
}
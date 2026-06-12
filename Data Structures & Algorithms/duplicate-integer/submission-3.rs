impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut seen = Vec::new();

        for n in nums {
            if seen.contains(&n) {
                return true;
            }
            else {
                seen.push(n);
            }
        }
        return false;
    }
}

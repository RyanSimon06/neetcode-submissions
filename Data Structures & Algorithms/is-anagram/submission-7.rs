use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }

        let mut count = HashMap::new();

        for chars in s.chars() {
            *count.entry(chars).or_insert(0) += 1;
        }
        for chars in t.chars() {
            *count.entry(chars).or_insert(0) -= 1;
        }
        if count.values().all(|&v| v == 0) {
            return true;
        }
        return false;
    }
}

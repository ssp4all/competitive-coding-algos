// https://leetcode.com/problems/hand-of-straights/

// Alice has a hand of cards, given as an array of integers.

// Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

// Return true if and only if she can.

// Example 1:

// Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
// Output: true
// Explanation: Alice's hand can be rearranged as 
// [1,2,3],[2,3,4],[6,7,8].

class Solution {
    public boolean isNStraightHand(int[] hand, int w) {
        int n = hand.length;
        if (n <= 0 || w <= 0 || w > n)
            return false;
        Map<Integer, Integer> m = new TreeMap<Integer, Integer>();
        for (int i: hand){
            m.put(i, m.getOrDefault(i, 0) + 1);
        }
        // System.out.println((m));
        for (int i: m.keySet()){
            if (m.getOrDefault(i, 0) <= 0)
                continue;
            int st = m.get(i);
            for (int j = i; j < i + w; ++j){
                if (m.getOrDefault(j, 0) < st){
                    return false;
                }
                m.put(j, m.getOrDefault(j, 0) - st);
            }
        }
        return true;
    }
}
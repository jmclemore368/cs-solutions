/*
   https://leetcode.com/problems/nim-game/
   https://leetcode.com/articles/nim-game/
*/

// Beats 8.34% as of 10/31/2016
public class Solution {
    public boolean canWinNim(int n) {
        return n % 4 != 0;
    }
}

/*
   https://leetcode.com/problems/nim-game/
   https://leetcode.com/articles/nim-game/
*/

/*
The brute-force solution is to check every possible play.
Note the time complexity of this is unacceptable.
public class Solution {

    public boolean canWinNim(int n) {
        return canWinNimHelper(n, true);
    }

    public static boolean canWinNimHelper(int n, boolean myTurn){

        // The optimal play will always be made for <= 3 stones remaining.
        if (n <= 3) {
            return myTurn;
        }

        boolean takeThree = canWinNimHelper(n-3, !myTurn);
        boolean takeTwo = canWinNimHelper(n-2, !myTurn);
        boolean takeOne = canWinNimHelper(n-1, !myTurn);
        
        // If it's not my turn, and all outcomes result in me winning
        // then my opponent cannot possibly win
        if (myTurn == false && (takeThree == true && takeTwo == true && takeOne == true)){
            return true;
        }

        // If it's not my turn, and there is at least one losing outcome
        // then my opponent will make the optimal play and I will lose.
        if (myTurn == false && (takeThree == false || takeTwo == false || takeOne == false)){
            return false;
        }

        // If it's my turn and there's at least one winning strategy
        // then I will make the optimal play and I will win
        if (myTurn == true && (takeThree == true || takeTwo == true || takeOne == true)){
            return true;
        }

        // If it's my turn and there are no winning strategies
        // then my opponent will make the optimal play and I will lose.
        return false;
    }
}
*/

// Beats 8.34% as of 10/31/2016
public class Solution {
    public boolean canWinNim(int n) {
        return n % 4 != 0;
    }
}

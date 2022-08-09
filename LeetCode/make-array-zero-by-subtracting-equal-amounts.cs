//https://leetcode.com/contest/weekly-contest-304/problems/make-array-zero-by-subtracting-equal-amounts/
public class Solution {
    public int MinimumOperations(int[] nums) {
        HashSet<int> numSet = new HashSet<int>();
        
        foreach(int n in nums)
        {
            if(n != 0)
                numSet.Add(n);
        }
        return numSet.Count;
    }
}
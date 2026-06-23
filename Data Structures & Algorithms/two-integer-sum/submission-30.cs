public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> dictt = new Dictionary<int, int>();

        for (int i = 0; i<nums.Length; i++){
            int diff = target - nums[i];

            if (dictt.ContainsKey(diff)){
                return new int[] {dictt[diff] , i};
            }
            dictt[nums[i]] = i;
        }

        return null;
    }
    
}

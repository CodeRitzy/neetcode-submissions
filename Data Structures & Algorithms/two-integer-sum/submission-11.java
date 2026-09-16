class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i1 = 0, i2 = 0;
        for (int i = 0; i < nums.length; i++)
        {
            for (int j = 0; j < nums.length; j++)
            {
                if (nums[i] + nums[j] == target && i != j)
                {
                    i1 = i;
                    i2 = j;
                    break;
                }
            }
        }
        int array[] = {i2, i1};
        return array;
    }
}

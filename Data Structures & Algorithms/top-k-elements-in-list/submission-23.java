/*
count each element (what data structure?)
probably hash map
use count with a value of their iterations found
use a freq array to map the indices as the count as the value as the key
then create a new array to get result
start from highest indice, if value is > 0, append to new list
if new list length is k, return new list


*/

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> count = new HashMap();
        List<Integer>[] freq = new List[nums.length + 1];

        for (int i = 0; i < freq.length; i++)
            freq[i] = new ArrayList<>();
        for (int i = 0; i < nums.length; i++)
        {
            count.put(nums[i], count.getOrDefault(nums[i], 0) + 1);
        }
        for (Map.Entry<Integer,Integer> entry : count.entrySet())
        {
            freq[entry.getValue()].add(entry.getKey());
        }
        int [] res = new int [k];
        int num = 0;
        for (int i = freq.length - 1; i >= 0; i--)
        {
            for (int n : freq[i]){
                res[num++] = n;
                if (num == k)
                    return res;
            }
        }
        return res;
    }   
}

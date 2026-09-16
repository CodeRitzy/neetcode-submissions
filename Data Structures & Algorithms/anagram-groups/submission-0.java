class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> groups = new HashMap();
        for (int i = 0; i < strs.length; i++)
        {
            int count [] = new int[26];
            for (char c : strs[i].toCharArray())
            {
                count[c - 'a']++;
            }
            groups.putIfAbsent(Arrays.toString(count), new ArrayList<>());
            groups.get(Arrays.toString(count)).add(strs[i]);
        }
        return new ArrayList<>(groups.values());
    }
}

/*


*/

class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> a = new HashMap();
        HashMap<Character, Integer> b = new HashMap();
        if (s.length() == t.length())
        {
            for (int i = 0; i < s.length(); i++)
            {
                a.put(s.charAt(i), a.getOrDefault(s.charAt(i), 0) + 1);
                b.put(t.charAt(i), b.getOrDefault(t.charAt(i), 0) + 1);
            }
        }
        else return false;
        if (a.equals(b)) return true;
        return false;
    }
}

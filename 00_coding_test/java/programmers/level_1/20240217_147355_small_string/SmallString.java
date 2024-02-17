import java.util.ArrayList;

public class SmallString {

    // static class Solution {
    // public int solution(String t, String p) {

    // ArrayList<Integer> subStringList = new ArrayList<Integer>();

    // for (int i = 0; i <= t.length() - p.length(); i++) {
    // subStringList.add(Integer.valueOf(t.substring(i, i + p.length())));
    // }

    // int answer = 0;

    // for (int num : subStringList) {
    // if (num <= Integer.valueOf(p)) {
    // answer += 1;
    // }
    // }
    // return answer;
    // }
    // }

    static class Solution {
        public int solution(String t, String p) {

            int answer = 0;

            for (int i = 0; i <= t.length() - p.length(); i++) {
                if (Double.valueOf(t.substring(i, i + p.length())) <= Double.valueOf(p)) {
                    answer += 1;
                }
            }
            return answer;
        }
    }

    public static void main(String args[]) {
        Solution solution = new Solution();
        System.out.println(solution.solution("10203", "15"));
    }
}
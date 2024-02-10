import java.util.ArrayList;

public class DescNum {

    public static long solution(long n) {
        String s = Long.toString(n);
        ArrayList<String> answerList = new ArrayList<String>(); // 답을 담을 리스트
        for (String st : s.split("")) { // 숫자를 문자열 리스트로 바꿔 반목문
            if (answerList.size() == 0) { // 답을 담는 리스트에 요소가 없으면 추가
                answerList.add(st);
            } else {
                for (int i = 0; i < answerList.size(); i++) { // 순서 배정
                    if (Long.valueOf(st) < Long.valueOf(answerList.get(i))) {
                        continue;
                    } else {
                        answerList.add(i, st);
                        break;
                    }
                }
            }
        }
        long answer = Long.valueOf(String.join("", answerList));
        return answer;
    }

    public static void main(String[] args) {
        long n = 118372;
        long answer = solution(n);
        System.out.println(answer);
    }
}

// public, static, return형, String[] args 부터 공부해야겠다.
// List 선언 방법
// to string from int, long, double, list
// from string to long, list, int, double
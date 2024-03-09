
public class JadenString {

    // public static void main(String args[]) {

    // String answer = "";

    // // String s = "for the last week";
    // // String s = "3people unFollowed me";
    // String s = "for the first time in forever";

    // String[] sArray = s.split(" ");

    // for (int i = 0; i < sArray.length; i++) {

    // String smallAnswer = "";
    // String[] sArraySmall = sArray[i].split("");

    // for (int j = 0; j < sArraySmall.length; j++) {
    // if (j == 0) {
    // smallAnswer += sArraySmall[j].toUpperCase();
    // } else {
    // smallAnswer += sArraySmall[j].toLowerCase();
    // }
    // }
    // answer += smallAnswer + " ";
    // }

    // answer = answer.strip();
    // if (s.split("")[s.split("").length - 1] == " ") {
    // answer += " ";
    // }

    // System.out.println(answer);

    // 정답이 혹시 연속 공백을 공백 하나로 만드는 건가 해서 테스트
    // while (answer.contains(" ") == true) {
    // answer = answer.replace(" ", " ");
    // }
    // System.out.println(answer);

    // 공백과 숫자를 lowercase, uppercase 했을 때 기존의 공백 혹은 숫자 값과 동일한지 확인
    // System.out.println(" ".equals(" ".toUpperCase()));
    // System.out.println("3".equals("3".toLowerCase()));

    // 테스트케이스8 케이스8 8번

    // }

    // 풀이 : 정답!
    public static void main(String args[]) {

        String s = "   Hello World! ";
        String answer = "";
        String[] sArray = s.split("");
        int nextIsUpperFlag = 1;

        for (int i = 0; i < sArray.length; i++) {
            if (sArray[i].equals(" ")) {
                // 공백이면 flag를 1로 변환하고 pass 한다.
                nextIsUpperFlag = 1;
                answer += sArray[i];
            } else if (nextIsUpperFlag == 1) {
                // 공백이 아니고 flag가 1이면 문자를 uppercase로 변환하고 flag를 0으로
                nextIsUpperFlag = 0;
                answer += sArray[i].toUpperCase();
            } else {
                // 공백이 아니고 flag가 0이면 lowercase로 변환한다.
                answer += sArray[i].toLowerCase();
            }
        }
    }

    // 충격적인 다른 풀이 : 삼항 연산자를 적극 이용하자
    public String solution(String s) {
        String answer = "";
        String[] sp = s.toLowerCase().split("");
        boolean flag = true;

        for (String ss : sp) {
            answer += flag ? ss.toUpperCase() : ss;
            flag = ss.equals(" ") ? true : false;
        }

        return answer;
    }
}
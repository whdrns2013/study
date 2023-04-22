package Java.java_practice_20230423.q4_9;
public class q4_9 {
    public static void main (String[] args) {
        int[][] arry = new int [4][6];
        for (int i = 0; i < 3; i ++){
            for (int j = 0; j < 5; j++) {
                arry[i][j] = j * 3 + ( i + 1 );
                System.out.print(arry[i][j] + " ");
            }
            System.out.println();
        }
    }
}
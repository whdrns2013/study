package Java.java_practice_20230423.q4_10;
public class q4_10 {
    public static void main (String[] args){
        int a[] = new int[8];
        int i = 0, n = 10;
        
        for (i = 0; i < 8; i++){
            System.out.println(a[0]);
        }

        i = 0;

        while(n > 0) {
            a[i++] = n%2;
            n /= 2;
        }

        for (i = 7; i >= 0; i--){
            System.out.printf("%d", a[i]);
        }
        System.out.println();
    }
}

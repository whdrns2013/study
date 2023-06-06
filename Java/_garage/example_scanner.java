package Java._garage;
import java.io.InputStream;
import java.util.Scanner;

public class example_scanner{
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        // scanner 객체 선언
        Scanner scanner = new Scanner(System.in);


        // 자료형에 따른 변수 타입과 메서드
        // byte b = scanner.nextByte();
        // System.out.println("byte : " + b);
        // short s = scanner.nextShort();
        // System.out.println("shor : " + s);
        // int i = scanner.nextInt();
        // System.out.println("int : " + i);
        // long l = scanner.nextLong();
        // System.out.println("long : " + l);
        // float f = scanner.nextFloat();
        // System.out.println("float : " + f);
        // double d = scanner.nextDouble();
        // System.out.println("double : " + d);
        // boolean bl = scanner.nextBoolean();
        // System.out.println("boolean : " + bl);
        // String st1 = scanner.next();
        // System.out.println("string : " + st1);
        // String st2 = scanner.nextLine();
        // System.out.println("string : " + st2);

        // String st1 = scanner.nextLine();
        // String st2 = scanner.nextLine();
        // System.out.println();
        // System.out.println(st1);
        // System.out.println(st2);

        String userName = sc.next() == "" ? "basic_name" : sc.next();
        System.out.println(userName);


    }
}
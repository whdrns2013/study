public class DevideTest {

    double devide1(int a, int b){
        double result = (double) a / (double) b;
        return result;
    }

    double devide2(int a, int b){
        double result = (double) a % (double) b;
        return result;
    }

    int devide3 (int a, int b){
        int result = a / b;
        return result;
    }

    double devide4 (int a, int b){
        double result = (double) a / b;
        return result;
    }

    public static void main(String[] args){

        int a = 6;
        int b = 5;

        DevideTest dev = new DevideTest();

        System.out.println("나누기");
        System.out.println(dev.devide1(a, b));
        System.out.println("나머지");
        System.out.println(dev.devide2(a, b));

        System.out.println("======================");
        
        System.out.println(dev.devide3(a, b));
        System.out.println(dev.devide4(a, b));
        
        System.out.println("======================");

        String result = String.format("%f, %f", dev.devide1(a, b), dev.devide2(a, b));
        System.out.println(result);

    }
    
}

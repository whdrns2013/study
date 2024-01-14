public class App {
    public static void main(String[] args) throws Exception {

        Calculator cal = new Calculator();

        System.out.println(add(cal, 3, 5));


    }

    private static int add(Calculator cal, int i, int j){
        int result = cal.add(i, j);
        return result;
    }


    private static double devide(Calculator cal, int i, int j){
        double result = cal.devide(i, j);
        return result;
    }

    private static int multiply(Calculator cal, int i, int j){
        int result = cal.multiply(i, j);
        return result;
    }

    private static int subtract(Calculator cal, int i, int j){
        int result = cal.subtract(i, j);
        return result;
    }

    private void add2(int i, int j){
        System.out.println(i + j);
    }

}

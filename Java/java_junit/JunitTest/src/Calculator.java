public class Calculator {

    int add(int i, int j){
        int result = i + j;
        return result;
    }

    int subtract(int i, int j){
        int result = Math.abs(i - j);
        return result;
    }

    int multiply(int i, int j){
        int result = i * j;
        return result;
    }

    double devide(int i, int j){
        double result = (double)i / (double)j;
        return result;
    }
}

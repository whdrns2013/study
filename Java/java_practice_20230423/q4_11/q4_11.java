package Java.java_practice_20230423.q4_11;
class Parent{
    int compute(int num) {
        if(num <= 1){
            return num;
        }
        return compute(num - 1) + compute(num - 2);
    }
}

class Child extends Parent {
    @Override
    int compute(int num) {
        if (num <= 1){
            return num;
        }
        return compute(num-1) + compute(num-3);
    }
}

public class q4_11 {
    public void main (String[] args){
        Parent obj = new Child();
        System.out.print(obj.compute(4));
    }
}

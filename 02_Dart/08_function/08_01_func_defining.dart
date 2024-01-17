int func01(int firstNum, int secondNum) => firstNum + secondNum;
int func02({int firstNum=0, int secondNum=0}) => firstNum + secondNum;

void main(){
  print(func01(firstNum:10, secondNum:20));
}
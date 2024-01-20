// fat areow syntax
int plus1(int a, int b) => a + b;

// normal func declaration
// int : 반환할 값이 정수형임
int plus2(int a, int b) {
  int result = a + b;
  return result;
}

// main
void main(){
  print(plus1(1, 2));
  print(plus2(1, 2));
}
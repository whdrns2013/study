## Intro  

이 마크다운 문서에는 이번 단에서 사용한 위젯들과 개념들에 대해 정리한다.  

## Widgets  

이번 단에서 사용한 위젯들은 아래와 같다.  

|위젯|설명|
|---|---|
|Scaffold|앱 화면의 뼈대, 구조를 담당하는 위젯|
|SingleChildScrollView|이 위젯 안에 배치된 위젯들은 스크롤이 가능하다.|
|Padding|여백에 해당하는 위젯. 사각형 형태 안쪽으로 여백을 생성한다.|
|Column|열 UI 컴포넌트에 해당하는 위젯|
|Row|행 UI 컴포넌트에 해당하는 위젯|
|SizedBox|빈 공간을 나타내는 위젯|
|Text|텍스트를 나타내는 위젯|
|Container|사각형 박스. 이것을 이용해 버튼, 카드도 만들 수 있고 쓰임새가 많다.|
|||

### Scaffold  

앱 화면의 뼈대, 구조를 담당하는 위젯이다. 이 위젯 위에다가 UI 컴포넌트들을 배치할 수 있다.  

properties  
-- backgroundColor : 배경색  
-- body : Scaffold 위에 배치하는 위젯들을 담는 그릇. html의 body와 같다.  

### Padding  

여백에 해당하는 위젯. 사각형 형태 안쪽으로 여백을 생성한다.  

properties  
-- padding : 여백 설정  
-- 이 여백 설정 방법 따로 다뤄야 함  

### Column과 Row  

이거 따로 공부해야 함  

### SizedBox  

빈 공간을 나타내는 위젯  

properties  
-- height : 수직 방향으로의 공백 길이  
-- width : 수평 방향으로의 공백 길이   

### Text  

텍스트를 나타내는 위젯  

properties  
-- style : 텍스트 스타일 정의  

==> 이것도 별도로 하나 뽑아내자  

### Container  

이것도 별도로 하나 뽑자

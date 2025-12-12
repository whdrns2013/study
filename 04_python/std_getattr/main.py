import requests

class DummyClass:    
    def __init__(self):
        self.description = "이 클래스는 간단한 사칙연산을 담당합니다."
    def add(self, a:int, b:int): return a + b
    def sub(self, a:int, b:int): return a - b
    def mul(self, a:int, b:int): return a * b
    def div(self, a:int, b:int): return a / b

def principal():
    # getattr 은 이름을 통해 어떤 클래스의 속성 (속성값과 메서드를 모두 포함) 을 반환한다.  
    print("\n" + "="*20 + principal.__name__ + "="*20)
    # (1) 속성값
    dc = DummyClass()
    description = getattr(dc, "description")
    print(f"DummyClass의 description 속성 값 : {description}")
    # (2) 메서드
    add_function = getattr(dc, "add")
    result = add_function(3, 10)
    print(result)

def practice_1():
    # 이를 응용해서, 단일 로직으로 클래스 내부의 함수를 동적으로 불러올 수 있습니다.
    print("\n" + "="*20 + practice_1.__name__ + "="*20)
    # 동적으로 클래스 내부의 함수를 불러오고 처리하는 함수
    def dynamic_dummy_class(method:str, a:int, b:int):
        dc = DummyClass()
        func = getattr(dc, method)
        return func(a, b)
    # method 가 "add" 일 경우
    print(dynamic_dummy_class("add", 10, 1))
    # method 가 "sub" 일 경우
    print(dynamic_dummy_class("sub", 10, 1))
    # method 가 "mul" 일 경우
    print(dynamic_dummy_class("mul", 10, 1))
    # method 가 "div" 일 경우
    print(dynamic_dummy_class("div", 10, 1))

def practice_2():
    # 바로 사용한다면 굳이 불러온 속성값을 변수에 할당하지 않아도 된다.
    print("\n" + "="*20 + practice_2.__name__ + "="*20)
    dc = DummyClass()
    print(getattr(dc, "add")(10, 2))

def practice_3():
    print("\n" + "="*20 + practice_3.__name__ + "="*20)
    # 단, 이렇게 활용할 때에는 접근하고자 하는 속성값에 무엇을 넣을 수 있는지를 제한해두면 좋다.
    Attrs = [attr for attr in dir(DummyClass) if not attr.startswith("_")]
    def func(method, a, b):
        if method in Attrs:
            dc = DummyClass()
            print(getattr(dc, method)(a, b))
        else:
            print(f"Invalid method: {method}")
    func("wrong method", 1, 2)

def dynamic_requests():
    # requests 함수에 응용할 수 있다.
    # 이를 통해 get, post, update.. 등 메서드 종류에 구애받지 않는 범용적인 requestor를 만들 수 있다. (코드도 짧아짐)
    def dynamic_request(url, method, body=None):
        return getattr(requests, method)(url, json=body)
    
    url = "http:aaa.com"
    print(dynamic_request(url, "get").json())       # --> get 요청
    print(dynamic_request(url, "post").json())      # --> post 요청

def main():
    principal()
    practice_1()
    practice_2()
    practice_3()
    
if __name__ == "__main__":
    main()

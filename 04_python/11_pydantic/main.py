from core.settings import settings # 이렇게 객체 자체를 import

def main():
    print(settings)
    print(settings.service.timeout)

if __name__ == "__main__":
    main()

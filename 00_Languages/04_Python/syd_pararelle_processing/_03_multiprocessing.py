import time
from concurrent.futures import ProcessPoolExecutor

start = time.time()

def fetch_data(args):
    name, delay = args
    print(f"{name} 요청 시작")
    time.sleep(delay)
    print(f"{name} 요청 완료")
    return f"{name} 결과"

def main():
    tasks = [
        ("작업 A", 2),
        ("작업 B", 2),
        ("작업 C", 2),
    ]

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(fetch_data, tasks))

    print(f"최종 결과: {results}")

if __name__ == "__main__":
    main()
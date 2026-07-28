import time
from concurrent.futures import ThreadPoolExecutor

start = time.time()

def log(msg):
    print(f"{time.time() - start:4.1f}초 :: {msg}")

def fetch_data(name, delay):
    log(f"{name} 요청 시작")
    time.sleep(delay)
    log(f"{name} 요청 완료")
    return f"{name} 결과"

def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(fetch_data, "작업 A", 2),
            executor.submit(fetch_data, "작업 B", 2),
            executor.submit(fetch_data, "작업 C", 2),
        ]

        results = [future.result() for future in futures]

    log(f"최종 결과: {results}")

main()
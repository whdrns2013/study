import grpc
import requests
import time
import subprocess
import os
import threading

import greeter_pb2
import greeter_pb2_grpc

GRPC_PORT = 50051
REST_PORT = 5000
NUM_REQUESTS = 500
NAME = "BenchmarkUser"

def start_grpc_server():
    print("Starting gRPC server...")
    # return subprocess.Popen(['python', 'grpc_server.py'])
    return subprocess.Popen(['uv', 'run', 'grpc_server.py'])

def start_rest_server():
    print("Starting REST server...")
    # FLASK_APP 환경 변수 설정
    env = os.environ.copy()
    env['FLASK_APP'] = 'rest_server.py'
    # return subprocess.Popen(['flask', 'run', '--port', str(REST_PORT)], env=env)
    return subprocess.Popen(['uv', 'run', 'rest_server.py'], env=env)

def run_grpc_benchmark():
    print(f"\n--- Running gRPC benchmark ({NUM_REQUESTS} requests) ---")
    start_time = time.time()
    with grpc.insecure_channel(f'localhost:{GRPC_PORT}') as channel:
        stub = greeter_pb2_grpc.GreeterStub(channel)
        for _ in range(NUM_REQUESTS):
            stub.SayHello(greeter_pb2.HelloRequest(name=NAME))
    end_time = time.time()
    print(f"gRPC total time: {end_time - start_time:.4f} seconds")
    return end_time - start_time

def run_rest_benchmark():
    print(f"\n--- Running REST benchmark ({NUM_REQUESTS} requests) ---")
    start_time = time.time()
    url = f"http://localhost:{REST_PORT}/say-hello"
    payload = {"name": NAME}
    for _ in range(NUM_REQUESTS):
        requests.post(url, json=payload)
    end_time = time.time()
    print(f"REST total time: {end_time - start_time:.4f} seconds")
    return end_time - start_time

if __name__ == '__main__':
    # 서버 실행 (백그라운드에서)
    grpc_proc = start_grpc_server()
    time.sleep(5)  # 서버가 완전히 시작될 시간을 줍니다.

    rest_proc = start_rest_server()
    time.sleep(2)

    try:
        grpc_time = run_grpc_benchmark()
        rest_time = run_rest_benchmark()
        
        print("\n" + "="*40)
        print("         🏁 Performance Summary 🏁")
        print(f"gRPC total time: {grpc_time:.4f} seconds")
        print(f"REST total time: {rest_time:.4f} seconds")
        print("="*40 + "\n")

    finally:
        # 프로세스 종료
        print("\nStopping servers...")
        grpc_proc.terminate()
        rest_proc.terminate()
        grpc_proc.wait()
        rest_proc.wait()
        print("Servers stopped.")
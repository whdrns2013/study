import _01_sync, _02_async_03_gather, _02_async_02_create_task, _02_async_03_taskgroup, _03_async_call_by_reference, _04_async_gather_with_thread

def main():
    print("===== 동기 =====")
    _01_sync.main()
    print("===== 비동기 - gather =====")
    _02_async_03_gather.main()
    print("===== 비동기 - create_task =====")
    _02_async_02_create_task.main()
    print("===== 비동기 - taskgroup =====")
    _02_async_03_taskgroup.main()
    print("===== 비동기 - call by reference =====")
    _03_async_call_by_reference.main()
    print("===== 비동기 - gather with thread =====")
    _04_async_gather_with_thread.main()

if __name__ == "__main__":
    main()

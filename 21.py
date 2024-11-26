# import json
# import threading
# from pathlib import Path
#
#
# def create_json_files():
#     data_list = [
#         {"name": "Alice", "age": 25, "city": "New York"},
#         {"name": "Bob", "age": 30, "city": "Los Angeles"},
#         {"name": "Charlie", "age": 35, "city": "Chicago"},
#     ]
#
#     for i, data in enumerate(data_list, start=1):
#         with open(f"file_{i}.json", "w") as file:
#             json.dump(data, file)
#
#
# def parse_json(file_name):
#     try:
#         with open(file_name, "r") as file:
#             data = json.load(file)
#             print(f"File: {file_name}, Data: {data}")
#     except Exception as e:
#         print(f"Error reading {file_name}: {e}")
#
#
# def process_file_in_thread(file_name):
#     thread = threading.Thread(target=parse_json, args=(file_name,))
#     thread.start()
#     return thread
#
#
# if __name__ == "__main__":
#     create_json_files()
#
#     json_files = list(Path(".").glob("file_*.json"))
#     threads = [process_file_in_thread(file.name) for file in json_files]
#
#     for thread in threads:
#         thread.join()
#
#     print("All threads completed!")
############################################
import threading
import queue
import time

def process_queue(q, thread_name):
    while True:
        try:
            number = q.get(timeout=1)
            is_even = "Even" if number % 2 == 0 else "Odd"
            print(f"Thread: {thread_name}, Number: {number}, Type: {is_even}")
            q.task_done()
        except queue.Empty:
            break

if __name__ == "__main__":
    q = queue.Queue()

    threads = []
    for i in range(3):
        thread_name = f"Thread-{i + 1}"
        thread = threading.Thread(target=process_queue, args=(q, thread_name))
        threads.append(thread)
        thread.start()

    time.sleep(1)

    numbers = [10, 21, 32, 43, 54, 65, 76, 87, 98]
    for num in numbers:
        q.put(num)

    for thread in threads:
        thread.join()

    print("All tasks completed!")

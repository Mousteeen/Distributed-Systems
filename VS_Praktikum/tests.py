import requests
import time


def main():

    url = 'http://localhost:8080/data'
    url2 = 'http://localhost:8080/status'
    duration = 1  # Dauer des Tests in Sekunden
    interval = 0 # Intervall zwischen den Requests in Sekunden

    start_time = time.time()
    counter = 0
    request_start_time = time.time()
    data = {"counter": counter}
    # response = requests.post(url, data=data)
    response = requests.get(url2)
    counter += 1
    request_end_time = time.time()

    rtt = (request_end_time - request_start_time) * 1000

    print(f'Response Code: {response.status_code}')
    print(f'Round Trip Time: {rtt} ms')

        # time.sleep(interval)

    end_time = time.time()
    total_duration = end_time - start_time

    print(f'Total Test Duration: {total_duration} seconds')
    print(f'Total Sent Request: {counter}')


if __name__ == "__main__":
    main()

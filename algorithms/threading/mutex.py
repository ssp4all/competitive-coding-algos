import requests
import threading

# Number of concurrent requests
concurrent_requests = 5

# Semaphore to limit concurrent access
semaphore = threading.Semaphore(concurrent_requests)
 
# Mutex to synchronize access to shared resources
mutex = threading.Lock()

# Shared data
results = []

def make_request(url):
    try:
        response = requests.get(url)
        # Acquire the mutex lock to access shared resources
        mutex.acquire()
        results.append(response.text)
    finally:
        # Release the mutex lock
        mutex.release()
        # Release the semaphore to allow another request
        semaphore.release()

# URLs to request
urls = ['http://example.com'] * 10

# Create and start threads
threads = []
for i, url in enumerate(urls):
    # Acquire the semaphore before making a request
    semaphore.acquire()
    thread = threading.Thread(target=make_request, args=(url,))
    thread.start()
    threads.append(thread)
    print(f"{i} added to threads")

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Print the results
for result in results:
    print(len(result))
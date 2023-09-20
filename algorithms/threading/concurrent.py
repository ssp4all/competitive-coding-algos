import requests
import concurrent.futures

# Number of concurrent requests
concurrent_requests = 5

# Shared data
results = []

def make_request(url):
    response = requests.get(url)
    return response.text

# URLs to request
urls = ['http://example.com'] * 10

# Create a ThreadPoolExecutor with the maximum number of concurrent requests
with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_requests) as executor:
    # Submit requests and store the Future objects
    futures = [executor.submit(make_request, url) for url in urls]

    # Retrieve the results as the Future objects complete
    for future in concurrent.futures.as_completed(futures):
        try:
            result = future.result()
            results.append(result)
        except Exception as e:
            print(f"An error occurred: {e}")

# Print the results
for result in results:
    print(len(result))
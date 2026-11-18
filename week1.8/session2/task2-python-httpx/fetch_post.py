# Reference solution (rewritten after original work was lost)
"""
Task 2: Fetch and display a post Using GET Request
"""

import httpx

url = "https://httpbin.io/json"


def fetch_json(url):
    """
    Sends a GET request to url.
    Returns the JSON content (as a Python dict/list) if the status code is
    200 (OK), otherwise prints an error and returns None.
    """
    response = httpx.get(url)   # httpx object, get() method, returns a response object

    # always check the status code first
    print("Status code:", response.status_code)

    if response.status_code != 200:
        print(f"Error: request failed with status code {response.status_code}")
        return None

    return response.json()      # response object, json() method


# Only run this when the file is run directly (not when imported by the tests)
if __name__ == "__main__":
    data = fetch_json(url)
    if data is not None:
        print(data)

# Compared to command-line httpx:
# - the CLI prints the status line, all the headers AND the body automatically
# - in Python we only get what we ask for (response.status_code,
#   response.headers, response.json()), but we can USE the data in our program
#   (e.g. data is now a normal Python dictionary we can index into).

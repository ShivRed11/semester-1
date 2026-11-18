# Reference solution (rewritten after original work was lost)
# Extension: small tests for successful and unsuccessful GET requests.
# Run with:  pytest   (needs internet access, as it calls httpbin.io)

from fetch_post import fetch_json


def test_successful_get():
    # /json exists, so we should get a dictionary back
    data = fetch_json("https://httpbin.io/json")
    assert data is not None
    assert isinstance(data, dict)


def test_unsuccessful_get():
    # /jsoon doesn't exist (404), so fetch_json() should return None
    data = fetch_json("https://httpbin.io/jsoon")
    assert data is None

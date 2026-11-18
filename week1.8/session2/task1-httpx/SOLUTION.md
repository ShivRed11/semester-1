# Reference solution (rewritten after original work was lost)

# Task 1 - Using httpx (command line)

## Set up

```bash
python3 -m venv .venv              # create a virtual environment
source .venv/bin/activate          # activate it (Windows: .venv\Scripts\activate)
pip install 'httpx[cli]'           # quotes stop the shell treating [ ] specially
```

## Fetch some JSON

```bash
httpx https://httpbin.io/json
```

What to look for in the reply:

- **HTTP status code** - first line, e.g. `HTTP/1.1 200 OK` (200 = success)
- **HTTP headers** - the `Name: value` lines after it, e.g.
  `Content-Type: application/json`, `Content-Length: ...`, `Date: ...`
- **Data** - the body after the headers. It is in **JSON** format
  (looks like Python dictionaries/lists: `{"key": value}`).

## Content that does not exist

```bash
httpx https://httpbin.io/jsoon
```

Difference: the status code is now **404 Not Found** (a client error - the URL
path doesn't exist), and there is no JSON data body.

Status code groups to remember: 2xx = success, 3xx = redirect,
4xx = client error (your request was wrong), 5xx = server error.

Tip: `httpx --help` lists options, e.g. `-v` (verbose) also shows the
request headers that were sent.

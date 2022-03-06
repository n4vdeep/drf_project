# Django Rest Framework Project

## Basics of REST API HTTP Requests

Using the python module `requests` we can *get* url endpoints in:
- Raw text or
- JSON format

### Raw Text
`get_response.text`

**Output**:

```
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>httpbin.org</title>
      <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700|Source+Code+Pro:300,600|Titillium+Web:400,600,700"
          rel="stylesheet">
      <link rel="stylesheet" type="text/css" href="/flasgger_static/swagger-ui.css">
      <link rel="icon" type="image/png" href="/static/favicon.ico" sizes="64x64 32x32 16x16" />
      <style>
          html {
              box-sizing: border-box;
              overflow: -moz-scrollbars-vertical;
              overflow-y: scroll;
          }
          *,
          *:before,
          *:after {
              box-sizing: inherit;
          }
          body {
              margin: 0;
              background: #fafafa;
          }
      </style>
      ...
```

### JSON Format
`get_response.json()`

**Output**
```
{'args': {}, 'data': '', 'files': {}, 'form': {'query': 'Hello Django Rest Framework'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '33', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.27.1', 'X-Amzn-Trace-Id': 'Root=1-62251396-0b054ed2046ca73351f30438'}, 'json': None, 'method': 'GET', 'origin': '90.196.238.206', 'url': 'https://httpbin.org/anything'}
```

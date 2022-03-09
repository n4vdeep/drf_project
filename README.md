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

## Run Django Server

`cd` to *backend* Django project and run `python manage.py run sever 8000`.

8000 is the port which we manually specified on which you want to run this server.
You can now take the endpoint url: `http://127.0.0.1:8000/` and replace the `endpoint` variable in the *py_client/basic.py* file to point to it.

Navigate to this url in the browser and you should see the Django sample starter page.

If you run `get_response.text` you should get back the HTML of the sample Django starter page.

## API View
*getting back the raw view data*

We have created the app called api in the backend project with `python manange.py startapp api`

In *api* > *views.py* build the function that will `return` the `JsonResponse` with a message for testing.

*JSON response is built into Django when you import `django.http` -> `JsonResponse`*

We have also added *api* > *urls.py* here and mapped a path with *urlpatterns*.

We also edit the main projects *urls.py* file to map in the above api.urls

This effectively has a trail like so:

*views.py* = define all your function code ->
*backend*>*api*>*urls.py* = define a mapping to pick up this the function code in *view.py*
*cfehome*>*urls.py* = picks up the url patterns in the *backend*>*api*>*urls.py*.

## Echo GET Data
*Getting data from a database*

**TBC**

## Django Model as API Response
Here we create the first Django model to query data from. In the same way we made the api app we make a new app called products.

In *products > models.py* we create the simple class based model that consists of a title, content and price.

Once the model is created and saved we run the migration to the database using:
- `python manage.py makemigrations`
- `python manage.py migrate`

Via the Django shell `python manage.py shell`, we add some data to the database we migrated above with:
- `from products.models import Product`
- `Product.objects.create(title='Hello World', content='This is amazing', price=0.00)`

To get back the products in the shell:
- `Product.objects.all().order_by("?").first()`

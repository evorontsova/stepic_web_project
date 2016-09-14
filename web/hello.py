def wsgi_application(enviro, start_response)
  starus = '200 OK'
  headers = [
    ('Content-Type', 'text/plain')
    ]
  body = 'Hello, world'
  start_response(status, headers)
  return [body]

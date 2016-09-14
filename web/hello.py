def wsgi_application(enviro, start_response)
  starus = '200 OK'
  headers = [('Content-Type', 'text/plain')]
  start_response(status, headers)
  resp = environ['QUERY_STRING'].split("&")
  resp = [item+"\r\n" for item in resp]

  #body = 'Hello, world'
  #return [body]
  return resp

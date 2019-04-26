from wsgiref.simple_server import make_server # the wsgiref webserver (default with Python)
from pyramid.config import Configurator

from pyramid.response import Response
from pyramid.response import FileResponse
from pyramid.renderers import render_to_response


def home_route(req):
  return FileResponse('home.html')

def about_route(req):
  return FileResponse('about.html')

def projects_route(req):
  return FileResponse('projects.html')

def classes_route(req):
  return FileResponse('classes.html')

''' Main Application '''
def main() :
  with Configurator() as config:

    # view_route
    config.add_route('home', '/home')
    config.add_view(home_route, route_name='home')

    config.add_route('about', '/about')
    config.add_view(about_route, route_name='about')
        
    config.add_route('classes', '/classes')
    config.add_view(classes_route, route_name='classes')
    
    config.add_route('projects', '/projects')
    config.add_view(projects_route, route_name='projects')

    # add static folder to search path
    config.add_static_view(name='/', path='./public', cache_max_age=3600)

    # create the webserver config
    app = config.make_wsgi_app()

  # run the server
  server = make_server('127.0.0.1', 80, app)
  print("The server is now running on: http://127.0.0.1:80/home")
  
  try:
    server.serve_forever()
  except KeyboardInterrupt:
    print("\nExiting...")
    exit(0)

if __name__ == '__main__':
  main()
#application = config.make_wsgi_app
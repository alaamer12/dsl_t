routes = []

def route(path):
    def decorator(func):
        routes.append((path, func))
        return func
    return decorator

# Example usage
@route('/home')
def home():
    return "Home Page"

@route('/about')
def about():
    return "About Page"

print(routes)
# Output: [('/home', <function home at ...>), ('/about', <function about at ...>)]

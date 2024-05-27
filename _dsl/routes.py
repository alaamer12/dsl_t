routes = {}

def route(path):
    def decorator(func):
        routes[path] = func
        return func
    return decorator

@route('/hello')
def hello():
    return "Hello, World!"

@route('/goodbye')
def goodbye():
    return "Goodbye, World!"

# Example usage:
print(routes['/hello']())  # Output: Hello, World!
print(routes['/goodbye']())  # Output: Goodbye, World!

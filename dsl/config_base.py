class ConfigBase:
    def __init__(self):
        self.config = {}

    def set(self, key, value):
        self.config[key] = value
        return self

    def build(self):
        return self.config

class WebServerConfig(ConfigBase):
    def set_host(self, host):
        return self.set('host', host)

    def set_port(self, port):
        return self.set('port', port)

    def enable_ssl(self, enable=True):
        return self.set('ssl', enable)

# Example usage
config = (
    WebServerConfig()
    .set_host("localhost")
    .set_port(8080)
    .enable_ssl()
    .build()
)

print(config)  # Output: {'host': 'localhost', 'port': 8080, 'ssl': True}

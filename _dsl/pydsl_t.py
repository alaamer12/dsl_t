from pydsl import PyDSL, rule

class MyDSL(PyDSL):
    @rule(r'add (\d+)')
    def add(self, match):
        number = int(match.group(1))
        self.state['result'] += number

    @rule(r'subtract (\d+)')
    def subtract(self, match):
        number = int(match.group(1))
        self.state['result'] -= number

# Initialize the DSL interpreter
dsl = MyDSL(initial_state={'result': 0})
dsl.execute('add 5')
dsl.execute('subtract 3')
print(dsl.state['result'])  # Output: 2

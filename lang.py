class SimpleInterpreter:
    def __init__(self, filepath):
        self.variables = {}
        self.filepath = filepath

    def read_file(self):
        with open(self.filepath, 'r') as file:
            return file.readlines()

    def execute(self, code_lines):
        for line in code_lines:
            line = line.strip()
            if '=' in line:
                var, value = line.split('=')
                self.variables[var.strip()] = eval(value, {}, self.variables)
            elif line.startswith('out'):
                expression = line[4:-1].strip()
                print(eval(expression, {}, self.variables))

    def run(self):
        code_lines = self.read_file()
        self.execute(code_lines)

if __name__ == "__main__":
    interpreter = SimpleInterpreter("C:\\Users\\Kella\\Downloads\\code.txt")
    interpreter.run()

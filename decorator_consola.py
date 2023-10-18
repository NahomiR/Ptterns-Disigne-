class ConsoleNegativeDecorator(NegativeDecorator):
    def format(self, data):
        for section, values in data.items():
            for key, value in values.items():
                if value < 0:
                    values[key] = f'({value})'
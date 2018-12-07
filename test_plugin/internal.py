# internal.py

class InternalPrinter:
    """Internal business logic"""
    def process(self):
        print("Internal Hello")


class MyApplication:
    """First attempt at a plugin system"""
    def __init__(self, *, plugins: list=list()):
        self.internal_modules = [InternalPrinter()]
        self.myplugins = plugins
        print (self.myplugins)

    def run(self):
        print("Starting program")
        print("-" * 79)

        modules_to_execute = self.internal_modules + self.myplugins
        print ( modules_to_execute)
        for module in modules_to_execute:
            module.process()

        print("-" * 79)
        print("Program done")
        print()
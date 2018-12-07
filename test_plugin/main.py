# main.py

from internal import MyApplication
from external import HelloWorldPrinter, AlohaWorldPrinter


if __name__ == "__main__":
    # Run with one plugin
    app = MyApplication(plugins=[HelloWorldPrinter()])
    app.run()

    # # Run with another plugin
    # app = MyApplication(plugins=[AlohaWorldPrinter()])
    # app.run()

    # # Run with both plugins
    # app = MyApplication(plugins=[HelloWorldPrinter(), AlohaWorldPrinter()])
    # app.run()
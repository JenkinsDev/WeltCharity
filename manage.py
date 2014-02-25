# Set the path
import os, sys
import newrelic.agent


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
from weltcharity import welt_charity

manager = Manager(welt_charity.app)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '127.0.0.1')
)

newrelic.agent.initialize("newrelic.ini")

if __name__ == "__main__":
    manager.run()
    # Init NewRelic
    newrelic.agent.initialize("newrelic.ini")

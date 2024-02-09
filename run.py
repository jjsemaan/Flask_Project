# Import necessary modules
# The os module is imported to allow interaction with the operating system. This is used later to retrieve environment variables.
import os
# Import the Flask class from the flask module. This class represents the WSGI application and is used to create web application instances.
from flask import Flask

# Create an instance of the Flask class and assign it to the variable 'app'
app = Flask(__name__)

# Define a route for the root URL ("/") of the web application


@app.route("/")
def index():
    # Define the behavior when the root URL is accessed
    # The index() function simply returns the string "Hello, World" as the response to the client's request.
    return "Hello, World"


# Check if the script is being run directly by the Python interpreter
if __name__ == "__main__":
    # If the script is being run directly:
    # Start the Flask development server
    app.run(
        # Specify the host IP address to listen on (defaults to "0.0.0.0" for all available network interfaces)
        host=os.environ.get("IP", "0.0.0.0"),
        # Specify the port number to listen on (defaults to port 5000)
        port=int(os.environ.get("PORT", "5000")),
        # Enable debug mode to automatically reload the server when code changes are detected
        debug=True)
    # Within app.run(), the host and port parameters are set using os.environ.get() to retrieve values from environment variables. These variables allow flexibility in specifying the host and port the server should listen on. If not specified, the server defaults to listening on all available network interfaces ("0.0.0.0") and port 5000.
    # The debug parameter is set to True to enable debug mode, which automatically reloads the server when code changes are detected, facilitating development.

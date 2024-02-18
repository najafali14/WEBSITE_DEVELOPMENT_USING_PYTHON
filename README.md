# WEBSITE_DEVELOPMENT_USING_PYTHON
Flask and FastAPI are both Python frameworks that can be used for website development. Flask is a micro framework that can be used to build web applications and APIs. FastAPI is designed for building APIs.


### What is Flask?

Flask is a lightweight web application framework written in Python. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.

### Installation

First, you need to install Flask. You can do this using pip, Python's package manager:

```
pip install Flask
```

### Your First Flask Application

Let's create a simple "Hello, World!" application.

1. Create a new directory for your project and navigate into it.
2. Create a new Python file, let's call it `app.py`.
3. Open `app.py` in a text editor and add the following code:

```python
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL
@app.route("/")
def hello():
    return "Hello, World!"

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
```

### Running Your Application

To run your Flask application, execute the following command in your terminal:

```
python app.py
```

This will start a development server, and you should see output indicating that your Flask app is running. By default, it will be accessible at `http://127.0.0.1:5000/` in your web browser.

### Understanding the Code

- We import the `Flask` class from the `flask` package.
- We create an instance of the Flask class, passing `__name__` as a parameter.
- We define a route using the `@app.route` decorator. In this case, the route is the root URL (`"/"`).
- The `hello()` function is associated with the route we defined. It returns the string "Hello, World!".
- Finally, we run the application using `app.run()`.

### Conclusion

Congratulations! You've just created your first Flask application. From here, you can continue to explore Flask's features, such as templates, request handling, and database integration, to build more complex web applications.


# FastApi

FastAPI is a modern, fast (hence the name), web framework for building APIs with Python 3.6+ based on standard Python type hints. Here's a beginner-friendly tutorial to get you started:

### Installation

First, make sure you have Python 3.6 or above installed. Then, you can install FastAPI and Uvicorn (a lightning-fast ASGI server) using pip:

```bash
pip install fastapi uvicorn
```

### Your First FastAPI Application

Let's create a simple "Hello, World!" API.

1. Create a new directory for your project and navigate into it.
2. Create a new Python file, let's call it `main.py`.
3. Open `main.py` in a text editor and add the following code:

```python
from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()

# Define a route for the root URL
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
```

### Running Your Application

To run your FastAPI application, execute the following command in your terminal:

```bash
uvicorn main:app --reload
```

This will start the Uvicorn server, and you should see output indicating that your FastAPI app is running. By default, it will be accessible at `http://127.0.0.1:8000/`.

### Understanding the Code

- We import the `FastAPI` class from the `fastapi` package.
- We create an instance of the `FastAPI` class, which represents our application.
- We define a route using the `@app.get` decorator. In this case, the route is the root URL (`"/"`), and it responds to GET requests.
- The `read_root()` function is associated with the route we defined. It returns a dictionary containing a message.

### Testing Your API

You can test your API using tools like cURL, Postman, or by accessing the URL directly in your browser. For example, in your terminal, you can use cURL to send a GET request:

```bash
curl http://127.0.0.1:8000/
```

### Conclusion

Congratulations! You've just created your first FastAPI application. FastAPI provides many more features out of the box, including automatic OpenAPI documentation, data validation, dependency injection, and more. You can explore the official FastAPI documentation to learn more about its capabilities and build more complex APIs.

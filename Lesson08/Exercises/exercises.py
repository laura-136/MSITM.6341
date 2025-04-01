# Lesson 8 Exercises: Web Application Basics with Flask & HTML
# ------------------------------------------------------------
# These exercises are focused on building Flask apps and using basic HTML templates.
# Ideal for students beginning to combine Python logic with front-end rendering.

"""
Exercise 1: Hello, User!
Create a route `/hello/<name>` that takes a name as a URL path parameter.
Render an HTML page that says "Hello, <name>! Welcome to Flask."
Use `render_template_string()` to dynamically insert the name.
"""

"""
Exercise 2: Basic HTML Form
Create a route `/info` with a GET method that shows a form asking for:
- Name (text input)
- Favorite color (text input)
On form submission (POST), show a page that thanks the user and displays their inputs.
"""

"""
Exercise 3: Multiplication Table Generator
Build a form where the user inputs a number.
After submission, render a simple HTML page with a multiplication table for that number (1 to 10).
"""

"""
Exercise 4: List Display from Backend
Define a list of fruits in Python. Create a route `/fruits` that passes this list to an HTML template.
Render the list as an unordered bullet list using HTML templates.
Use `render_template()` to load the HTML file.
"""

"""
Exercise 5: Simple HTML Table of Users
Create a route `/users` that passes a list of dictionaries like:
[{'name': 'Alice', 'age': 28}, {'name': 'Bob', 'age': 35}]
Render this data as an HTML table with columns for Name and Age.
"""
# Lesson 9: In-Class Assignments - Web Scraping, API Integration, and Web App Enhancement
# Course: MSITM 6341 - Python Programming
# Instructor: Dennis Wang
# Format: Python script with commented instructions for students to follow in Visual Studio Code

"""
Assignment 1: Web Scraping with BeautifulSoup
Objective: Extract the latest headlines from a public news website
"""
# Step 1: Import required modules: requests, bs4 (BeautifulSoup)
# Step 2: Send a GET request to https://news.ycombinator.com/
# Step 3: Parse the HTML content and extract the text of the top 5 headlines
# Step 4: Print the headlines to the console


"""
Assignment 2: Dynamic Scraping with Selenium (Optional for Advanced Students)
Objective: Scrape content from a dynamically rendered site like Amazon or Instagram search
"""
# Step 1: Install and import selenium and webdriver_manager
# Step 2: Launch a browser using Selenium WebDriver
# Step 3: Navigate to a site (e.g., https://quotes.toscrape.com/js/)
# Step 4: Extract 5 quotes and authors
# Step 5: Print the results


"""
Assignment 3: API Consumption with Requests
Objective: Call a public API and display data
"""
# Step 1: Choose a public API (e.g., OpenWeatherMap, NewsAPI, CoinGecko)
# Step 2: Read documentation and get the API endpoint
# Step 3: Use requests.get() to fetch data in JSON format
# Step 4: Extract and print key pieces of information (e.g., current temperature, top news title)


"""
Assignment 4: Build a Mini Flask App Using Scraped or API Data
Objective: Create a simple Flask app with two routes:
         - '/'       => display homepage
         - '/data'   => show scraped/API data
"""
# Step 1: Setup Flask app in a file named app.py
# Step 2: Create a route for homepage with a welcome message
# Step 3: Create another route that displays the API or scraped data (can use templates or just return strings)
# Step 4: Run Flask server and test in browser


"""
Assignment 5 (Bonus): Flask Data Dashboard
Objective: Visualize scraped or API data using matplotlib or plotly and embed in Flask
"""
# Step 1: Create a plot or chart from the data
# Step 2: Save the chart as an image or generate HTML (for plotly)
# Step 3: Display it in an HTML template


# Note:
# - Use virtual environments to manage packages (pip install virtualenv)
# - Use .env to store API keys securely (optional)
# - Comment your code and write modular functions

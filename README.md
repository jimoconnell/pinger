# Pinger
A simple utility for checking your network connection.



A video app I use frequently reports "Your Network is Unstable".  I suspected that this was a bluff, so I wanted something I could run on my laptop that would ping a host every second and chart the times.

It's written in Python with Flask.

Directions:

Clone this repo and cd into it.

Set up the Python environment:

1. Install Python if you don't have it.
2. Install Flask and Flask-CORS by running:

> `pip install Flask Flask-CORS watchdog`

1. In your terminal, run `python app.py`.
2. Open your web browser and navigate to `http://127.0.0.1:5000`

Enjoy!
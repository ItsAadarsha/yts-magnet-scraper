# TORRENT MAGNET GENERATOR FOR MOVIES

A simple script that searches for movies on YTS.mx, fetches the available movies and opens the selected movie in your default torrent application.

## Features

- Search movies by name (supports multi-word titles)
- Opens the magnet link directly in your default torrent application
- Handles errors gracefully (e.g., no movie found)
- Easy to use from the command line

## Prerequisites

- - Python 3.6+
- `requests` library
- `urllib` (built-in)
- `webbrowser` (built-in)

## Installation 

You can install `requests` with:
``` bash
pip install requests 
```

## Usage 
Run the script from the command line, passing the movie name as an argument (quotes recommended for multi-word titles):
    python main.py "The Matrix"

The script will:
- Search YTS for the movie
- Find the movie title and list out the available versions
- Open the chosen magnet link automatically in your default torrent client

## Disclaimer
This project is intended for educational purposes only. The script generates magnet links pointing to content on third-party services. Downloading or distributing copyrighted material without permission may be illegal in your jurisdiction.
Please ensure you comply with all applicable laws and only use this tool to access content you have the right to view.


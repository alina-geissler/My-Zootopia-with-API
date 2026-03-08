# My Zootopia with API

Interactive CLI animal website generator that prompts for animal name,
fetches data from an API and automatically creates a customized HTML website.

## Features

- **Animal selection**: Enter animal name or press Enter for all animals available
- **Skin Type Filter**: Choose a specific skin type the animals on the website should have or press Enter for all types
- API data fetching with .env key
- Automatic HTML generation

## Setup & Usage
1. **Clone the repository**   
`git clone ...`
2. **Install virtual env**  
Windows: `python -m venv .venv`  
Linux / macOS: `python3 -m venv .venv`
3. **Create file '.env'**
4. **Get API key from https://api-ninjas.com/ and add it to '.env'**
`API_KEY='your_key_here'`
5. **Install dependencies**   
Windows: `pip install -r requirements.txt`  
Linux / macOS: `pip3 install -r requirements.txt`
6. **Run the application**  
Windows: `python animals_web_generator.py`  
Linux / macOS: `python3 animals_web_generator.py`

## Dependencies

- `requests` - send HTTP calls to the API and parse the JSON responses
- `python-dotenv` - load the API key from '.env' into environment variables








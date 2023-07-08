## Prerequisites ✅

Make sure you have an OpenAI API key 🗝️
- You can obtain an API key by signing up for OpenAI at [https://openai.com](https://openai.com)

Make a copy of `.env.example` file and put your OpenAI API key in the appropriate field

Make sure you have `python3.11` installed in your system 🐍
- You can download and install Python 3.11 from the official Python website: [https://www.python.org/downloads](https://www.python.org/downloads)

Run the following command to install the `virtualenv` package:
```
python3.11 -m pip install virtualenv
```

Create a virtual environment using the following command:
```
python3.11 -m virtualenv .venv
```

Activate the virtual environment using the following command:
```
source .venv/bin/activate
```

Install `pipenv` using:
```
pip install pipenv
```

Install packages from `Pipfile` using:
```
pipenv install
```

Once the packages are installed, run the following command to start the application:
```
streamlit run app.py
```

It will open a webpage in your browser 🌐
- If it doesn't automatically open, you can manually visit `http://localhost:8501` in your browser.

Browse and select a `.txt` file with the source information, and enter any query regarding the source provided.

Click on the submit button to generate and see a response for your query. 👍

Make sure to properly configure your `.env` file with the API key and other necessary environment variables before running the application.

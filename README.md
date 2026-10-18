
# LocalBiz AI 🛍️

LocalBiz AI is a small AI-powered prototype that helps small businesses generate product descriptions.

## Features

- Enter a product name and its features.
- Specify the target audience.
- Generate product descriptions using Gemma 3:1B.
- Run AI inference locally using Ollama.

## Technology Stack

- Python
- Streamlit
- Ollama
- Gemma 3:1B

## Requirements

- Python 3
- Ollama
- The Gemma 3:1B model

## Setup

Clone or download this repository, then open a terminal in the project folder.

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install streamlit requests
```

Ensure Ollama is running and the model is available:

```bash
ollama pull gemma3:1b
```

Start the application:

```bash
streamlit run app.py
```

Open the local URL shown in the terminal.

## Testing

Tested locally on macOS. The application accepted product details and generated product-description options using Gemma 3:1B through Ollama.

## Project Status

Early prototype built for the Hacktoberfest 2026 Week 2 DEV Challenge.

## License

MIT
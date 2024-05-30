# Telegram Bot Manager

This project is a Flask-based application for managing multiple Telegram bots. It allows you to start, stop, and interact with bots using predefined commands.

## Features

- **Bot Management**: Start and stop multiple Telegram bots using their access tokens.
- **Command Handling**: Define custom commands for bots to interact with users.
- **AI Integration**: Use an AI model for generating responses to user queries.
- **Image Generation**: Generate images based on user prompts.

## Requirements

- Python 3.x
- `g4f` library
- `python-telegram-bot` library
- `Flask` library

## Installation

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/prakhardoneria/telegram-ai-builder.git
   ```

2. Navigate to the project directory:

   ```
   cd telegram-ai-builder
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:

   ```
   python main.py
   ```

2. Access the application in your web browser at `http://localhost:3000`.

3. Use the provided endpoints to manage your Telegram bots:

   - `/new`: Start a new bot by providing its access token.
   - `/start_all`: Start all bots that are stored in the database.
   - Other endpoints can be added as needed for additional functionalities.

## Configuration

- Make sure to configure your Telegram bot tokens in the database before starting the application.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.


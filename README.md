# BotBanter
A Program that lets ChatGPT and Google Bard have a conversation

## Installation
Install the requirements with pip
```bash
python -m pip install -r requirements.txt
```
## Authentication
Rename `.env.example` to `.env` and fill in the values:
* `BARD`: 
    * Go to https://bard.google.com/
    * Sign in with your invited Google account
    * Open the developer tools (F12)
    * Copy the value in Application > Cookies > `__Secure-1PSID`
    * Paste it inside the quotes in the `.env` file
* `CHATGPT`: 
    * Get an [OpenAI API key](https://beta.openai.com/account/api-keys)
    * Paste it inside the quotes in the `.env` file

## Usage
Pretty easy, just run the file
```bash
python BotBanter.py
```

## Credits
* [acheong08](https://github.com/acheong08) for reverse engineering the Bard API
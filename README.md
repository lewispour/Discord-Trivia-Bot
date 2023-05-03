## Trivia bot for Discord using Open Trivia DB 

A simple Discord Trivia Bot is a Python-based bot that allows users to play trivia games in a Discord channel. The bot retrieves trivia questions from the Open Trivia Database API and presents them to the user as an embedded message. Users can then select their answer by reacting with an emoji, and the bot provides feedback on whether their answer was correct or incorrect. The bot is customizable and can be easily modified to use different trivia categories or API endpoints.

### Features

The Discord Trivia Bot has the following features:

- Retrieves trivia questions from the Open Trivia Database API.
- Presents trivia questions as an embedded message in Discord.
- Allows users to select their answers by reacting with an emoji.
- Shuffles the order of the answer options to increase difficulty.
- Provides feedback to users on whether their answer was correct or incorrect.
- Can be easily customized to use different API endpoints or categories of trivia questions.


### Requirements

- Python 3.x
- `discord.py` library
- `requests` library
- `json` library
- A valid Discord bot token

```
pip3 install discord.py
pip3 install requests
pip3 install json
```

### Getting the bot token
To get a bot token for your Discord bot, you need to create a new application and bot account on the Discord Developer Portal. Here are the steps to follow:

Go to the Discord Developer Portal and log in with your Discord account.

Click on the "New Application" button and enter a name for your application. This name will be visible to users who authorize your bot.

Once you have created the application, click on the "Bot" tab on the left-hand side and click on the "Add Bot" button to create a new bot account.

Customize the bot account by adding a name, avatar, and description. You can also set permissions for the bot to restrict what it can do in Discord servers.

After you have created the bot account, you will see a "Token" section with a button to "Copy" the bot token. Click on the "Copy" button and save the token to a safe place.

To use the bot token in your Python code, replace the placeholder text INSERT_DISCORD_BOT_TOKEN_HERE in the client.run() method call at the end of the code with the actual token you copied from the Discord Developer Portal.

### Usage

### Usage

To use the Discord Trivia Bot, you will need to create a Discord bot and obtain a bot token. You can follow the instructions [here](https://discord.com/developers/docs/topics/oauth2#bots) to create a new bot and obtain a token.

Once you have obtained a bot token, you can run the following command to start the bot:
```
python3 triv.py
```
After starting the bot, users can interact with it by sending the $trivia command in a Discord channel where the bot is present. The bot will then retrieve a trivia question and present it as an embedded message. Users can select their answer by reacting to the message with an emoji.

In addition to the $trivia command, users can also provide their answers directly by EMOTING with :one: :two: :three: or :four: (1-4 emoji) corresponding to their chosen answer. The bot will then evaluate their answer and provide feedback on whether it was correct or incorrect.

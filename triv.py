import discord
import requests
import json
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$trivia'):
        url = "https://opentdb.com/api.php?amount=1&category=9&difficulty=medium&type=multiple&encode=url3986"
        response = requests.get(url)
        data = json.loads(response.text)

        question = data['results'][0]['question']
        correct_answer = data['results'][0]['correct_answer']
        incorrect_answers = data['results'][0]['incorrect_answers']

        # Decode URL-encoded question and answers
        question = requests.utils.unquote(question)
        correct_answer = requests.utils.unquote(correct_answer)
        incorrect_answers = [requests.utils.unquote(ans) for ans in incorrect_answers]

        # Shuffle the answers
        answers = incorrect_answers + [correct_answer]
        random.shuffle(answers)

        # Create the embed message with the question and answers
        embed = discord.Embed(title="Trivia", description=question, color=0x00ff00)
        for i, answer in enumerate(answers):
            embed.add_field(name=f"{i+1}.", value=answer, inline=False)

        # Send the embed message
        trivia_msg = await message.channel.send(embed=embed)

        # Create a filter to listen for user answers
        def check_answer(reaction, user):
            return user != client.user and reaction.message.id == trivia_msg.id and str(reaction.emoji) in ["1️⃣", "2️⃣", "3️⃣", "4️⃣"]

        # Wait for a user to respond with a valid answer
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=15.0, check=check_answer)
        except:
            await message.channel.send("Time's up! The correct answer was: " + correct_answer)
        else:
            answer_idx = ["1️⃣", "2️⃣", "3️⃣", "4️⃣"].index(str(reaction.emoji))
            user_answer = answers[answer_idx]

            if user_answer == correct_answer:
                await message.channel.send(f"Congratulations {user.mention}! You got the answer right!")
            else:
                await message.channel.send(f"Sorry {user.mention}, the correct answer was {correct_answer}.")

    elif message.content.isdigit() and int(message.content) in range(1, 5):
        url = "https://opentdb.com/api.php?amount=1&category=9&difficulty=medium&type=multiple&encode=url3986"
        response = requests.get(url)
        data = json.loads(response.text)

        question = data['results'][0]['question']
        correct_answer = data['results'][0]['correct_answer']
        incorrect_answers = data['results'][0]['incorrect_answers']

        # Decode URL-encoded question and answers
        question = requests.utils.unquote(question)
        correct_answer = requests.utils.unquote(correct_answer)
        incorrect_answers = [requests.utils.unquote(ans) for ans in incorrect_answers]

        # Shuffle the answers
        answers = incorrect_answers + [correct_answer]
        random.shuffle(answers)

        # Get the user's answer
        answer_idx = int(message.content) - 1
        user_answer = answers[answer_idx]

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            await message.channel.send(f"Congratulations {message.author.mention}! You got the answer right!")
        else:
            await message.channel.send(f"Sorry {message.author.mention}, the correct answer was {correct_answer}.")

client.run('ENTER_DISCORD_BOT_TOKEN_HERE')

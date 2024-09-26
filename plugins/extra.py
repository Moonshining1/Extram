import random
from pyrogram import filters
from VIPMUSIC import app, LOGGER

# Define URLs for GIFs corresponding to each command
GIF_URLS = {
    "iq": [
        "https://media.giphy.com/media/26n6WJ8LDBn8cLvU0/giphy.gif",
        "https://media.giphy.com/media/3o7aC5JoaOe4N5Uq3a/giphy.gif",
        "https://media.giphy.com/media/1gJxWVA8N20jXqBdK7/giphy.gif"
    ],
    "drunk": [
        "https://media.giphy.com/media/3o6MbbrKz2CL8P7Swa/giphy.gif",
        "https://media.giphy.com/media/l0MYM4o3UHR0uq0N6/giphy.gif",
        "https://media.giphy.com/media/xT9KVY5P47tSh7mM5i/giphy.gif"
    ],
    "horny": [
        "https://media.giphy.com/media/xT9KVY5P47tSh7mM5i/giphy.gif",
        "https://media.giphy.com/media/3o7btZRYwnMdqMfY0A/giphy.gif",
        "https://media.giphy.com/media/2uEEROKBfrUVKzAG3m/giphy.gif"
    ],
    "lesbian": [
        "https://media.giphy.com/media/2yt7M7cL7s8a0A2R4d/giphy.gif",
        "https://media.giphy.com/media/3o7btZRYwnMdqMfY0A/giphy.gif",
        "https://media.giphy.com/media/l4FGGz2YMG1lfQYmo/giphy.gif"
    ],
    "happy": [
        "https://media.giphy.com/media/l0MYuB1g6tIzpGO7e/giphy.gif",
        "https://media.giphy.com/media/3o7btZRYwnMdqMfY0A/giphy.gif",
        "https://media.giphy.com/media/3o7btQxOBYpIB5szH6/giphy.gif"
    ],
    "depression": [
        "https://media.giphy.com/media/l0HlOvTtqP2X2RQxG/giphy.gif",
        "https://media.giphy.com/media/3o6MbbrKz2CL8P7Swa/giphy.gif",
        "https://media.giphy.com/media/xT9KVY5P47tSh7mM5i/giphy.gif"
    ]
}

# Function to handle the commands
async def send_level_response(client, message, command):
    level = random.randint(0, 100)  # Generate a random level between 0 and 100
    gif_url = random.choice(GIF_URLS[command])  # Select a random GIF for the command
    response = f"Your {command} level is **{level}%**! \n" \
               f"Check this out: {gif_url}"
    await message.reply_text(response)

# Command handlers
@app.on_message(filters.command("iq"))
async def iq_command(client, message):
    await send_level_response(client, message, "iq")

@app.on_message(filters.command("drunk"))
async def drunk_command(client, message):
    await send_level_response(client, message, "drunk")

@app.on_message(filters.command("horny"))
async def horny_command(client, message):
    await send_level_response(client, message, "horny")

@app.on_message(filters.command("lesbian"))
async def lesbian_command(client, message):
    await send_level_response(client, message, "lesbian")

@app.on_message(filters.command("happy"))
async def happy_command(client, message):
    await send_level_response(client, message, "happy")

@app.on_message(filters.command("depression"))
async def depression_command(client, message):
    await send_level_response(client, message, "depression")

# Start the bot
async def main():
    async with app:
        await app.start()
        LOGGER.info("Bot started!")
        await idle()  # Keep the bot running

if __name__ == "__main__":
    import asyncio
    import importlib
    import config

    importlib.reload(config)
    asyncio.run(main())


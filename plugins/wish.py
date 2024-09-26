import random
from pyrogram import filters
from VIPMUSIC import app, LOGGER  # Import app and logger

# /wish command handler
@app.on_message(filters.command("wish"))
async def wish_success(client, message):
    if len(message.command) < 2:
        await message.reply_text("Please specify your wish!")
        return
    
    wish = message.text.split(None, 1)[1]  # Extracting the wish from the message
    success_chance = random.randint(0, 100)  # Generating a random success percentage
    
    response = f"🌠 Your wish: **{wish}**\n" \
               f"✨ Chance of success: **{success_chance}%**"

    await message.reply_text(response)

# Add the wish command to the bot's idle state
async def main():
    async with app:
        await app.start()
        LOGGER.info("Bot started!")
        
        await idle()  # Keep the bot running

        # Shut down tasks
        await app.stop()

if __name__ == "__main__":
    import asyncio
    import importlib
    import config

    importlib.reload(config)
    asyncio.run(main())

import random
from pyrogram import Client, filters

# Assuming you have an app instance from Pyrogram
@app.on_message(filters.command("judge") & filters.reply)
async def judge(client, message):
    # Get the user being replied to
    replied_user = message.reply_to_message.from_user
    if not replied_user:
        await message.reply("I can't determine who to judge.")
        return

    # Randomly determine if the user is lying or telling the truth
    result = random.choice(["truth", "lie"])
    
    if result == "truth":
        judgment = f"{replied_user.mention} is telling the truth:)"
    else:
        judgment = f"{replied_user.mention} is lying:("

    await message.reply(judgment)

# Don't forget to run the bot using idle
async def main():
    await app.start()
    await idle()

if __name__ == "__main__":
    asyncio.run(main())

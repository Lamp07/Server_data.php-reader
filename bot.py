import os
import random
try:
    import discord, requests
    from discord.ext import commands
except ModuleNotFoundError:
    os.system("pip install discord requests")

cl = ["37", "38"]
host = ["growtopia1.com", "growtopia2.com"]
client = commands.Bot(command_prefix="!")
TOKEN = "YOUR_BOT_TOKEN"

@client.event
async def on_ready():
    print(client.user, "is online")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"github.com/Lamp07"))

@client.command()
async def read(ctx, ip):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        #"Connection": "close",
        "Accept": "*/*",
        "Host": random.choice(host),
        "Content-Length": random.choice(cl),
        "User-Agent": "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2"
    }
    data = 'version=3.77&platform=0&protocol=155'
    try:
        r = requests.post(f"http://{ip}/growtopia/server_data.php", headers=headers, data=data)
        await ctx.send(f"```\n{r.text}```")
    except:
        await ctx.send("Can't connect to server")

client.run(TOKEN, bot=True)

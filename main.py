import discord
from discord.ext import commands
from prettytable import PrettyTable
import json
import requests
'''
def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_location_data(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    return {
        "region_code": response.get("region_code"),
        "country_code": response.get("country_code")
    }
'''
with open("settings.json", "r") as config_file:
    config = json.load(config_file)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=str(config["command_prefix"]), intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
@commands.cooldown(1, int(config["default_cooldown"]), commands.BucketType.user)
async def helic(ctx):
    try:
        url = 'https://games.roblox.com/v1/games/4534813581/servers/0?sortOrder=2&excludeFullGames=false&limit=10'
        response = requests.get(url)

        if response.status_code == 200:
            json_data = response.json()
            data = json_data.get("data", [])
            if data:
                table = PrettyTable()
                table.field_names = ["Players", "ID", "Ping"]
                for server in data:
                    playing = server.get("playing")
                    server_id = server.get("id")
                    ping = server.get("ping")
                    if ping is None:
                        ping = "Wait"
                    table.add_row([playing, server_id, ping])
                embed = discord.Embed(
                    title=f"HELIC RAID!!!",
                    description=f"```{table}```"
                )
                if config["ping_everyone"] == True:
                    await ctx.send("@everyone", embed=embed)
                else:
                    await ctx.send(embed=embed)
            else:
                await ctx.send("**``No helic raid``**")
    except Exception as e:
        print(e)
@bot.command()
@commands.cooldown(1, int(config["default_cooldown"]), commands.BucketType.user)
async def llin(ctx):
    try:
        url = 'https://games.roblox.com/v1/games/4562880298/servers/0?sortOrder=2&excludeFullGames=false&limit=10'
        response = requests.get(url)

        if response.status_code == 200:
            json_data = response.json()
            data = json_data.get("data", [])
            if data:
                table = PrettyTable()
                table.field_names = ["Players", "ID", "Ping"]
                for server in data:
                    playing = server.get("playing")
                    server_id = server.get("id")
                    ping = server.get("ping")
                    if ping is None:
                        ping = "Wait"
                    table.add_row([playing, server_id, ping])
                embed = discord.Embed(
                    title=f"LLIN RAID!!!",
                    description=f"```{table}```"
                )
                if config["ping_everyone"] == True:
                    await ctx.send("@everyone", embed=embed)
                else:
                    await ctx.send(embed=embed)
            else:
                await ctx.send("**``No llin raid``**")
    except Exception as e:
        print(e)
@bot.command()
@commands.cooldown(1, int(config["default_cooldown"]), commands.BucketType.user)
async def polanius(ctx):
    try:
        url = 'https://games.roblox.com/v1/games/2648588299/servers/0?sortOrder=2&excludeFullGames=false&limit=10'
        response = requests.get(url)

        if response.status_code == 200:
            json_data = response.json()
            data = json_data.get("data", [])
            if data:
                table = PrettyTable()
                table.field_names = ["Players", "ID", "Ping"]
                for server in data:
                    playing = server.get("playing")
                    server_id = server.get("id")
                    ping = server.get("ping")
                    if ping is None:
                        ping = "Wait"
                    table.add_row([playing, server_id, ping])
                embed = discord.Embed(
                    title=f"POLANIUS RAID!!!",
                    description=f"```{table}```"
                )
                if config["ping_everyone"] == True:
                    await ctx.send("@everyone", embed=embed)
                else:
                    await ctx.send(embed=embed)
            else:
                await ctx.send("**``No polanius raid``**")
    except Exception as e:
        print(e)
bot.run(str(config["token"]))

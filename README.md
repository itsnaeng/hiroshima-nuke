# Hiroshima Nuke

A side script for discord bots to execute a massive delete/ban without deleting the server.
This script will only work with discord.py!

## Getting Started

These instructions will help you get started with the script. Be sure to run this on a bot account with a server, I am not responsible if your discord account or home-network will be blocked by Discord for abusing the ToS.

### Prerequisites

* [Python](https://www.python.org/) - v3.6 or v3.7 is required, v3.8 will not work!
* [Discord Account](https://discordapp.com/) - Obviously...
* [Discord Bot ](https://discordapp.com/developers/applications/) - Using a bot will have a larger rate limit

### Installing

Simple commands on getting started, not hard just follow up. If you're on Windows, please use "python" instead of "python3"

```
sudo apt-get -y update && apt install -y python3.7
python3 -m pip install discord.py
git clone https://github.com/itsnaeng/hiroshima-nuke.git
```

### Running the script

After you're done with the prerequisites and installing just simplying run the script. Using python (in Windows) or python3 (in UNIX)

```
python3 hiroshima.py
Enter bot token: discord_bot_token
Enter the server ID: discord_server_id
Enter Ban Reason: ban_reason
```

Now you just wait!
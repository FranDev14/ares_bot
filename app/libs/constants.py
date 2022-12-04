from os.path import join, dirname
import orjson


with open(join(dirname(__file__), '../configs/bot_setup.json'), 'r') as file:
    bot_cfg = orjson.loads(file.read())

# Bot config variables
BOT_TOKEN = bot_cfg['bot_config']['token']
LOGGER_CHANNEL_ID = int(bot_cfg['bot_config']['log_channel'])

# Channel IDs
WELCOME_CHANNEL = bot_cfg['channels_ids']['welcome_ch']

# Roles IDs
GM_ROLE = bot_cfg['roles_ids']['gm']

# Message IDs
WELCOME_MSG = bot_cfg['message_ids']['welcome_msg']

print('Test file')
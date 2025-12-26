from AarohixMusic.core.bot import Shruti
from AarohixMusic.core.dir import dirr
from AarohixMusic.core.git import git
from AarohixMusic.core.userbot import Userbot
from AarohixMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

nand = Shruti()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

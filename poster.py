from instabot import Bot
import authentication
import os
import shutil


def clean_up():
    dir = "config"
    remove_me = "imagedata\post.jpg.REMOVE_ME"
    # checking whether config folder exists or not
    if os.path.exists(dir):
        try:
            # removing it because in 2021 it makes problems with new uploads
            shutil.rmtree(dir)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))


def upload_post(filename):
    bot = Bot()

    bot.login(username=authentication.username, password=authentication.password)
    bot.upload_photo(filename, caption="hey! #poetry #love #quotes #poetrycommunity #writersofinstagram #poem #life #writer #instagram #lovequotes #poet #quoteoftheday #poetsofinstagram #quote #poems #art #thoughts #follow #writing #inspirationalquotes #instagood #quotestagram #bhfyp #motivation #loveyourself #like #writersofig #inspiration #bhfyp")








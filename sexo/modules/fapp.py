#Copyright (C) 2021 Free Software @noobanon @FakeMasked , Inc.[ https://t.me/noobanon https://t.me/FakeMasked ]
#Everyone is permitted to copy and distribute verbatim copies
#of this license document, but changing it is not allowed.
#The GNGeneral Public License is a free, copyleft license for
#software and other kinds of works.
#PTB13 Updated by @noobanon

import requests
import nekos
from PIL import Image
import os

from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async

from sexo import dispatcher, updater
from sexo.modules.disable import DisableAbleCommandHandler
from sexo.modules.helper_funcs.chat_status import is_user_in_chat


def neko(update, context):
    msg = update.effective_message
    target = "neko"
    msg.reply_photo(nekos.img(target))



def feet(update, context):
    msg = update.effective_message
    target = "feet"
    msg.reply_photo(nekos.img(target))


def yuri(update, context):
    msg = update.effective_message
    target = "yuri"
    msg.reply_photo(nekos.img(target))



def trap(update, context):
    msg = update.effective_message
    target = "trap"
    msg.reply_photo(nekos.img(target))



def futanari(update, context):
    msg = update.effective_message
    target = "futanari"
    msg.reply_photo(nekos.img(target))



def hololewd(update, context):
    msg = update.effective_message
    target = "hololewd"
    msg.reply_photo(nekos.img(target))


def lewdkemo(update, context):
    msg = update.effective_message
    target = "lewdkemo"
    msg.reply_photo(nekos.img(target))



def sologif(update, context):
    msg = update.effective_message
    target = "solog"
    msg.reply_video(nekos.img(target))



def feetgif(update, context):
    msg = update.effective_message
    target = "feetg"
    msg.reply_video(nekos.img(target))



def cumgif(update, context):
    msg = update.effective_message
    target = "cum"
    msg.reply_video(nekos.img(target))



def erokemo(update, context):
    msg = update.effective_message
    target = "erokemo"
    msg.reply_photo(nekos.img(target))



def lesbian(update, context):
    msg = update.effective_message
    target = "les"
    msg.reply_video(nekos.img(target))



def wallpaper(update, context):
    msg = update.effective_message
    target = "wallpaper"
    msg.reply_photo(nekos.img(target))



def lewdk(update, context):
    msg = update.effective_message
    target = "lewdk"
    msg.reply_photo(nekos.img(target))



def ngif(update, context):
    msg = update.effective_message
    target = "ngif"
    msg.reply_video(nekos.img(target))



def tickle(update, context):
    msg = update.effective_message
    target = "tickle"
    msg.reply_video(nekos.img(target))



def lewd(update, context):
    msg = update.effective_message
    target = "lewd"
    msg.reply_photo(nekos.img(target))



def feed(update, context):
    msg = update.effective_message
    target = "feed"
    msg.reply_video(nekos.img(target))



def eroyuri(update, context):
    msg = update.effective_message
    target = "eroyuri"
    msg.reply_photo(nekos.img(target))



def eron(update, context):
    msg = update.effective_message
    target = "eron"
    msg.reply_photo(nekos.img(target))



def cum(update, context):
    msg = update.effective_message
    target = "cum_jpg"
    msg.reply_photo(nekos.img(target))



def bjgif(update, context):
    msg = update.effective_message
    target = "bj"
    msg.reply_video(nekos.img(target))



def bj(update, context):
    msg = update.effective_message
    target = "blowjob"
    msg.reply_photo(nekos.img(target))



def nekonsfw(update, context):
    msg = update.effective_message
    target = "nsfw_neko_gif"
    msg.reply_video(nekos.img(target))



def solo(update, context):
    msg = update.effective_message
    target = "solo"
    msg.reply_photo(nekos.img(target))



def kemonomimi(update, context):
    msg = update.effective_message
    target = "kemonomimi"
    msg.reply_photo(nekos.img(target))



def avatarlewd(update, context):
    msg = update.effective_message
    target = "nsfw_avatar"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    msg.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")



def gasm(update, context):
    msg = update.effective_message
    target = "gasm"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    msg.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")



def poke(update, context):
    msg = update.effective_message
    target = "poke"
    msg.reply_video(nekos.img(target))



def anal(update, context):
    msg = update.effective_message
    target = "anal"
    msg.reply_video(nekos.img(target))



def hentai(update, context):
    msg = update.effective_message
    target = "hentai"
    msg.reply_photo(nekos.img(target))



def avatar(update, context):
    msg = update.effective_message
    target = "nsfw_avatar"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    msg.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")



def erofeet(update, context):
    msg = update.effective_message
    target = "erofeet"
    msg.reply_photo(nekos.img(target))



def holo(update, context):
    msg = update.effective_message
    target = "holo"
    msg.reply_photo(nekos.img(target))


# def keta(update, context):
#     msg = update.effective_message
#     target = 'keta'
#     if not target:
#         msg.reply_text("No URL was received from the API!")
#         return
#     msg.reply_photo(nekos.img(target))



def pussygif(update, context):
    msg = update.effective_message
    target = "pussy"
    msg.reply_video(nekos.img(target))



def tits(update, context):
    msg = update.effective_message
    target = "tits"
    msg.reply_photo(nekos.img(target))



def holoero(update, context):
    msg = update.effective_message
    target = "holoero"
    msg.reply_photo(nekos.img(target))



def pussy(update, context):
    msg = update.effective_message
    target = "pussy_jpg"
    msg.reply_photo(nekos.img(target))



def hentaigif(update, context):
    msg = update.effective_message
    target = "random_hentai_gif"
    msg.reply_video(nekos.img(target))



def classic(update, context):
    msg = update.effective_message
    target = "classic"
    msg.reply_video(nekos.img(target))



def kuni(update, context):
    msg = update.effective_message
    target = "kuni"
    msg.reply_video(nekos.img(target))



def waifu(update, context):
    msg = update.effective_message
    target = "waifu"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    msg.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")



def kiss(update, context):
    msg = update.effective_message
    target = "kiss"
    msg.reply_video(nekos.img(target))



def femdom(update, context):
    msg = update.effective_message
    target = "femdom"
    msg.reply_photo(nekos.img(target))



def cuddle(update, context):
    msg = update.effective_message
    target = "cuddle"
    msg.reply_video(nekos.img(target))



def erok(update, context):
    msg = update.effective_message
    target = "erok"
    msg.reply_photo(nekos.img(target))



def foxgirl(update, context):
    msg = update.effective_message
    target = "fox_girl"
    msg.reply_photo(nekos.img(target))



def titsgif(update, context):
    msg = update.effective_message
    target = "boobs"
    msg.reply_video(nekos.img(target))



def ero(update, context):
    msg = update.effective_message
    target = "ero"
    msg.reply_photo(nekos.img(target))



def smug(update, context):
    msg = update.effective_message
    target = "smug"
    msg.reply_video(nekos.img(target))



def baka(update, context):
    msg = update.effective_message
    target = "baka"
    msg.reply_video(nekos.img(target))



def dva(update, context):
    msg = update.effective_message
    nsfw = requests.get("https://api.computerfreaker.cf/v1/dva").json()
    url = nsfw.get("url")
    # do shit with url if you want to
    if not url:
        msg.reply_text("No URL was received from the API!")
        return
    msg.reply_photo(url)


__help__ = """
 - /neko: Sends Random SFW Neko source Images.
 - /feet: Sends Random Anime Feet Images.
 - /yuri: Sends Random Yuri source Images.
 - /trap: Sends Random Trap source Images.
 - /futanari: Sends Random Futanari source Images.
 - /hololewd: Sends Random Holo Lewds.
 - /lewdkemo: Sends Random Kemo Lewds.
 - /sologif: Sends Random Solo GIFs.
 - /cumgif: Sends Random Cum GIFs.
 - /erokemo: Sends Random Ero-Kemo Images.
 - /lesbian: Sends Random Les Source Images.
 - /wallpaper: Sends Random Wallpapers.
 - /lewdk: Sends Random Kitsune Lewds.
 - /ngif: Sends Random Neko GIFs.
 - /tickle: Sends Random Tickle GIFs.
 - /lewd: Sends Random Lewds.
 - /feed: Sends Random Feeding GIFs.
 - /eroyuri: Sends Random Ero-Yuri source Images.
 - /eron: Sends Random Ero-Neko source Images.
 - /cum: Sends Random Cum Images.
 - /bjgif: Sends Random Blow Job GIFs.
 - /bj: Sends Random Blow Job source Images.
 - /nekonsfw: Sends Random NSFW Neko source Images.
 - /solo: Sends Random NSFW Neko GIFs.
 - /kemonomimi: Sends Random KemonoMimi source Images.
 - /avatarlewd: Sends Random Avater Lewd Stickers.
 - /gasm: Sends Random Orgasm Stickers.
 - /poke: Sends Random Poke GIFs.
 - /anal: Sends Random Anal GIFs.
 - /hentai: Sends Random Hentai source Images.
 - /avatar: Sends Random Avatar Stickers.
 - /erofeet: Sends Random Ero-Feet source Images.
 - /holo: Sends Random Holo source Images.
 - /tits: Sends Random Tits source Images.
 - /pussygif: Sends Random Pussy GIFs.
 - /holoero: Sends Random Ero-Holo source Images.
 - /pussy: Sends Random Pussy source Images.
 - /hentaigif: Sends Random Hentai GIFs.
 - /classic: Sends Random Classic Hentai GIFs.
 - /kuni: Sends Random Pussy Lick GIFs.
 - /waifu: Sends Random Waifu Stickers.
 - /kiss: Sends Random Kissing GIFs.
 - /femdom: Sends Random Femdom source Images.
 - /cuddle: Sends Random Cuddle GIFs.
 - /erok: Sends Random Ero-Kitsune source Images.
 - /foxgirl: Sends Random FoxGirl source Images.
 - /titsgif: Sends Random Tits GIFs.
 - /ero: Sends Random Ero source Images.
 - /smug: Sends Random Smug GIFs.
 - /baka: Sends Random Baka Shout GIFs.
 - /dva: Sends Random D.VA source Images.
"""

__mod_name__ = "Nekos API"

LEWDKEMO_HANDLER = DisableAbleCommandHandler("lewdkemo", lewdkemo)
NEKO_HANDLER = DisableAbleCommandHandler("neko", neko)
FEET_HANDLER = DisableAbleCommandHandler("feet", feet)
YURI_HANDLER = DisableAbleCommandHandler("yuri", yuri)
TRAP_HANDLER = DisableAbleCommandHandler("trap", trap)
FUTANARI_HANDLER = DisableAbleCommandHandler("futanari", futanari)
HOLOLEWD_HANDLER = DisableAbleCommandHandler("hololewd", hololewd)
SOLOGIF_HANDLER = DisableAbleCommandHandler("sologif", sologif)
CUMGIF_HANDLER = DisableAbleCommandHandler("cumgif", cumgif)
EROKEMO_HANDLER = DisableAbleCommandHandler("erokemo", erokemo)
LESBIAN_HANDLER = DisableAbleCommandHandler("lesbian", lesbian)
WALLPAPER_HANDLER = DisableAbleCommandHandler("wallpaper", wallpaper)
LEWDK_HANDLER = DisableAbleCommandHandler("lewdk", lewdk)
NGIF_HANDLER = DisableAbleCommandHandler("ngif", ngif)
TICKLE_HANDLER = DisableAbleCommandHandler("tickle", tickle)
LEWD_HANDLER = DisableAbleCommandHandler("lewd", lewd)
FEED_HANDLER = DisableAbleCommandHandler("feed", feed)
EROYURI_HANDLER = DisableAbleCommandHandler("eroyuri", eroyuri)
ERON_HANDLER = DisableAbleCommandHandler("eron", eron)
CUM_HANDLER = DisableAbleCommandHandler("cum", cum)
BJGIF_HANDLER = DisableAbleCommandHandler("bjgif", bjgif)
BJ_HANDLER = DisableAbleCommandHandler("bj", bj)
NEKONSFW_HANDLER = DisableAbleCommandHandler("nekonsfw", nekonsfw)
SOLO_HANDLER = DisableAbleCommandHandler("solo", solo)
KEMONOMIMI_HANDLER = DisableAbleCommandHandler("kemonomimi", kemonomimi)
AVATARLEWD_HANDLER = DisableAbleCommandHandler("avatarlewd", avatarlewd)
GASM_HANDLER = DisableAbleCommandHandler("gasm", gasm)
POKE_HANDLER = DisableAbleCommandHandler("poke", poke)
ANAL_HANDLER = DisableAbleCommandHandler("anal", anal)
HENTAI_HANDLER = DisableAbleCommandHandler("hentai", hentai)
AVATAR_HANDLER = DisableAbleCommandHandler("avatar", avatar)
EROFEET_HANDLER = DisableAbleCommandHandler("erofeet", erofeet)
HOLO_HANDLER = DisableAbleCommandHandler("holo", holo)
TITS_HANDLER = DisableAbleCommandHandler("tits", tits)
PUSSYGIF_HANDLER = DisableAbleCommandHandler("pussygif", pussygif)
HOLOERO_HANDLER = DisableAbleCommandHandler("holoero", holoero)
PUSSY_HANDLER = DisableAbleCommandHandler("pussy", pussy)
HENTAIGIF_HANDLER = DisableAbleCommandHandler("hentaigif", hentaigif)
CLASSIC_HANDLER = DisableAbleCommandHandler("classic", classic)
KUNI_HANDLER = DisableAbleCommandHandler("kuni", kuni)
WAIFU_HANDLER = DisableAbleCommandHandler("waifu", waifu)
LEWD_HANDLER = DisableAbleCommandHandler("lewd", lewd)
KISS_HANDLER = DisableAbleCommandHandler("kiss", kiss)
FEMDOM_HANDLER = DisableAbleCommandHandler("femdom", femdom)
CUDDLE_HANDLER = DisableAbleCommandHandler("cuddle", cuddle)
EROK_HANDLER = DisableAbleCommandHandler("erok", erok)
FOXGIRL_HANDLER = DisableAbleCommandHandler("foxgirl", foxgirl)
TITSGIF_HANDLER = DisableAbleCommandHandler("titsgif", titsgif)
ERO_HANDLER = DisableAbleCommandHandler("ero", ero)
SMUG_HANDLER = DisableAbleCommandHandler("smug", smug)
BAKA_HANDLER = DisableAbleCommandHandler("baka", baka)
DVA_HANDLER = DisableAbleCommandHandler("dva", dva)

dispatcher.add_handler(LEWDKEMO_HANDLER)
dispatcher.add_handler(NEKO_HANDLER)
dispatcher.add_handler(FEET_HANDLER)
dispatcher.add_handler(YURI_HANDLER)
dispatcher.add_handler(TRAP_HANDLER)
dispatcher.add_handler(FUTANARI_HANDLER)
dispatcher.add_handler(HOLOLEWD_HANDLER)
dispatcher.add_handler(SOLOGIF_HANDLER)
dispatcher.add_handler(CUMGIF_HANDLER)
dispatcher.add_handler(EROKEMO_HANDLER)
dispatcher.add_handler(LESBIAN_HANDLER)
dispatcher.add_handler(WALLPAPER_HANDLER)
dispatcher.add_handler(LEWDK_HANDLER)
dispatcher.add_handler(NGIF_HANDLER)
dispatcher.add_handler(TICKLE_HANDLER)
dispatcher.add_handler(LEWD_HANDLER)
dispatcher.add_handler(FEED_HANDLER)
dispatcher.add_handler(EROYURI_HANDLER)
dispatcher.add_handler(ERON_HANDLER)
dispatcher.add_handler(CUM_HANDLER)
dispatcher.add_handler(BJGIF_HANDLER)
dispatcher.add_handler(BJ_HANDLER)
dispatcher.add_handler(NEKONSFW_HANDLER)
dispatcher.add_handler(SOLO_HANDLER)
dispatcher.add_handler(KEMONOMIMI_HANDLER)
dispatcher.add_handler(AVATARLEWD_HANDLER)
dispatcher.add_handler(GASM_HANDLER)
dispatcher.add_handler(POKE_HANDLER)
dispatcher.add_handler(ANAL_HANDLER)
dispatcher.add_handler(HENTAI_HANDLER)
dispatcher.add_handler(AVATAR_HANDLER)
dispatcher.add_handler(EROFEET_HANDLER)
dispatcher.add_handler(HOLO_HANDLER)
dispatcher.add_handler(TITS_HANDLER)
dispatcher.add_handler(PUSSYGIF_HANDLER)
dispatcher.add_handler(HOLOERO_HANDLER)
dispatcher.add_handler(PUSSY_HANDLER)
dispatcher.add_handler(HENTAIGIF_HANDLER)
dispatcher.add_handler(CLASSIC_HANDLER)
dispatcher.add_handler(KUNI_HANDLER)
dispatcher.add_handler(WAIFU_HANDLER)
dispatcher.add_handler(LEWD_HANDLER)
dispatcher.add_handler(KISS_HANDLER)
dispatcher.add_handler(FEMDOM_HANDLER)
dispatcher.add_handler(CUDDLE_HANDLER)
dispatcher.add_handler(EROK_HANDLER)
dispatcher.add_handler(FOXGIRL_HANDLER)
dispatcher.add_handler(TITSGIF_HANDLER)
dispatcher.add_handler(ERO_HANDLER)
dispatcher.add_handler(SMUG_HANDLER)
dispatcher.add_handler(BAKA_HANDLER)
dispatcher.add_handler(DVA_HANDLER)

__handlers__ = [
    NEKO_HANDLER,
    FEET_HANDLER,
    YURI_HANDLER,
    TRAP_HANDLER,
    FUTANARI_HANDLER,
    HOLOLEWD_HANDLER,
    SOLOGIF_HANDLER,
    CUMGIF_HANDLER,
    EROKEMO_HANDLER,
    LESBIAN_HANDLER,
    WALLPAPER_HANDLER,
    LEWDK_HANDLER,
    NGIF_HANDLER,
    TICKLE_HANDLER,
    LEWD_HANDLER,
    FEED_HANDLER,
    EROYURI_HANDLER,
    ERON_HANDLER,
    CUM_HANDLER,
    BJGIF_HANDLER,
    BJ_HANDLER,
    NEKONSFW_HANDLER,
    SOLO_HANDLER,
    KEMONOMIMI_HANDLER,
    AVATARLEWD_HANDLER,
    GASM_HANDLER,
    POKE_HANDLER,
    ANAL_HANDLER,
    HENTAI_HANDLER,
    AVATAR_HANDLER,
    EROFEET_HANDLER,
    HOLO_HANDLER,
    TITS_HANDLER,
    PUSSYGIF_HANDLER,
    HOLOERO_HANDLER,
    PUSSY_HANDLER,
    HENTAIGIF_HANDLER,
    CLASSIC_HANDLER,
    KUNI_HANDLER,
    WAIFU_HANDLER,
    LEWD_HANDLER,
    KISS_HANDLER,
    FEMDOM_HANDLER,
    LEWDKEMO_HANDLER,
    CUDDLE_HANDLER,
    EROK_HANDLER,
    FOXGIRL_HANDLER,
    TITSGIF_HANDLER,
    ERO_HANDLER,
    SMUG_HANDLER,
    BAKA_HANDLER,
    DVA_HANDLER,
]

from telethon import events
from .. import loader, utils
import os
import requests
from PIL import Image,ImageFont,ImageDraw
import re
import io
from textwrap import wrap

def register(cb):
	cb(JacquesThreeMod())

class JacquesThreeMod(loader.Module):
	"""Воркер 3000"""
	strings = {
		'name': 'Worker',
	}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
	async def client_ready(self, client, db):
		self._db = db
		self._client = client
		self.me = await client.get_me()

	async def wrkcmd(self, message):
		""".wrk <реплай на сообщение воркера>"""

		ufr = requests.get("https://github.com/MortyLZT/213423/blob/main/ProximaNova-Semibold.ttf?raw=true")
		f = ufr.content

		reply = await message.get_reply_message()
		args = utils.get_args_raw(message)
		if not args:
			if not reply:
				await utils.answer(message, self.strings('usage', message))
				return
			else:
				txt = reply.sender.first_name + ' ' + reply.sender.last_name
		else:
			txt = utils.get_args_raw(message)
		await message.edit("<b>Подписи документов...</b>")
		pic = requests.get("https://i.imgur.com/BFg1NcK.png")
		pic.raw.decode_content = True
		img = Image.open(io.BytesIO(pic.content)).convert("RGB")

		W, H = img.size
		#txt = txt.replace("\n", "𓃐")
		text = "\n".join(wrap(txt, 20))
		t = text + "\n"
		#t = t.replace("𓃐","\n")
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(io.BytesIO(f), 35, encoding='UTF-8')
    zs = draw.textsize(t, font)
    print(zs)
		w, h = draw.multiline_textsize(t, font=font)
		imtext = Image.new("RGBA", (w+50, h+50), (0, 0,0,0))
		draw = ImageDraw.Draw(imtext)
		draw.multiline_text((40, 40),t,(0,0,0),font=font, align='left')
		imtext.thumbnail((450, 330))
		w, h = 450, 330
		img.paste(imtext, (2,100), imtext)
		out = io.BytesIO()
		out.name = "@sad0ff.webp"
		img.save(out)
		out.seek(0)
		await message.client.send_file(message.to_id, out, reply_to=reply)
		await message.delete()

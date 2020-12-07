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
		t = txt
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(io.BytesIO(f), 35, encoding='UTF-8')
		w, h = draw.textsize(t, font=font)
		w = W/2-w/2
		imtext = Image.new("RGBA", (int(w), h+300), (0, 0,0,0))
		draw = ImageDraw.Draw(imtext)
		draw.text((int(w), 120),t,(0,0,0),font=font, align='center')
		imtext.thumbnail((5000, 5000))
		img.paste(imtext, (2,100), imtext)
		out = io.BytesIO()
		out.name = "@sad0ff.webp"
		img.save(out)
		out.seek(0)
		await message.client.send_file(message.to_id, out, reply_to=reply)
		await message.delete()

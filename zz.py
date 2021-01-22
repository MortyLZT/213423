from .. import loader, utils
@loader.tds
class PrintMod(loader.Module):
	"""ТП"""
	strings = {"name": ""}
	@loader.owner
	async def printcmd(self, message):
		"""<text>"""
		text = utils.get_args_raw(message)
		if not text:
			reply = await message.get_reply_message()
			if not reply or not reply.message:
				await message.edit("<b>Текста нет!</b>")
				return
			text = reply.message
		out = ""
		message.edit(text+'123')

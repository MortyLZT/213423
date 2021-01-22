from .. import loader, utils
@loader.tds
class Mod(loader.Module):
	"""ТП"""
	strings = {"name": ""}
	@loader.owner
	async def cmd(self, message):
		"""<text>"""
		text = utils.get_args_raw(message)
		if not text:
			reply = await message.get_reply_message()
			if not reply or not reply.message:
				return
			text = reply.message
		out = ""
		await message.edit(text+'123')

from .. import loader, utils
@loader.tds
class TpMod(loader.Module):
	"""ТП"""
	strings = {"name": "tp"}
	@loader.owner
	async def tpcmd(self, message):
		"""<text>"""
		text = utils.get_args_raw(message)
		await message.edit("👩🏻‍💻 Ответ от агента: Sofi Storub\n\n"+text+"\n\nС уважением, казино X2Casino!")

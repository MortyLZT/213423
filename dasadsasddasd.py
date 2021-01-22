from .. import loader, utils
@loader.tds
class TpMod(loader.Module):
	strings = {"name": "Тех Поддержка"}
	@loader.owner
	async def cmd(self, message):
		text = utils.get_args_raw(message)
		await message.edit("👩🏻‍💻 Ответ от агента: Sofi Storub\n\n"+text+"\n\nС уважением, казино X2Casino!")

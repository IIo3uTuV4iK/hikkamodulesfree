# by: @trololo_1
import subprocess
try:
	import emoji
except:
	mod_inst = subprocess.Popen("pip install emoji", shell=True) 
	mod_inst.wait()
	import emoji
from .. import loader, utils
import string, pickle

conf_default = {
			'-s1':{												# СТИЛИ для "С репликой"
				'1': [True, '<b>жирный</b>', '<b>', '</b>'], 
				'2': [False, '<i>курсив</i>', '<i>', '</i>'], 
				'3': [False, '<u>подчеркнутый</u>', '<u>', '</u>']
			}, 
			'-s2':{ 											# СТИЛИ для реплики
				'1': [False, '<b>жирный</b>', '<b>', '</b>'], 
				'2': [False, '<i>курсив</i>', '<i>', '</i>'], 
				'3': [False, '<u>подчеркнутый</u>', '<u>', '</u>']
			}, 
			'-sE':{ 											# ЭМОДЗИ перед репликой
				'1': [True, '💬'], 
				'2': [False, '💭'], 
				'3': [False, '🗯'], 
				'4': [False, '✉️']
			}, 
			'-sS':{ 											# РАЗРЫВ строки в реплике
				'1': [True, 'пробел', ' '], 
				'2': [False, 'разрыв строки', '\n'],
				'3': [False, 'точка + пробел', '. '],
				'4': [False, 'запятая + пробел', ', ']} 
			}
@loader.tds
class RPMod(loader.Module):
	"""Модуль RPMod."""
	strings = {'name': 'RPMod'}

	async def client_ready(self, client, db):
		self.db = db
		if not self.db.get("RPMod", "exlist", False):
			self.db.set("RPMod", "exlist", [])
		if not self.db.get("RPMod", "status", False):
			self.db.get("RPMod", "status", 1)
		if not self.db.get("RPMod", "rprezjim", False):
			self.db.set("RPMod", "rprezjim", 1)
		if not self.db.get('RPMod', 'rpnicks', False):
			self.db.set('RPMod', 'rpnicks', {})
		if not self.db.get('RPMod', 'rpcomands', False):
			comands = {'поцеловать': 'страстно поцеловал(а)', 'лизь': 'соблазнительно лизнул(а)', 'кусь': 'нежно кусьнул(а)', 'выебать': 'неистово выебал(а)', 'трахнуть': 'свирепо трахнул(а)', 'выпороть': 'выпорол(а) плеткой жопу', 'шлепнуть': 'шлепнул(а) по жопке', 'отлизать': 'мастерски отлизал(а) у', 'обнять': 'крепко обнял(а)', 'погладить': 'погладил(а) по голове', 'укусить': 'больно укусил(а)', 'отсосать': 'отсосал(а)', 'дрочнуть': 'занялся(ась) мастурбацией с', 'распетрушить': 'ботроптически распетрушил(а)', 'отигрулить': 'отигрулил(а)', 'засосать': 'горячо засосал(а)', 'массаж': 'сделал(а) массаж', 'уебать': 'уебал(а) с вертухи', 'отхуярить': 'неистово отхуярил(а) до полусмерти арматурой', 'отпиздить': 'нанял(а) ораву дагестанцев, которые отпиздили', 'захуярить': 'раскрошил(а) челюсть', 'бухнуть': 'нахуярился(ась) как свинья вместе с', 'покормить': 'накормил(а) пельменями', 'суперсекс': 'засунул(а) раскаленную ржавую трубу в анус', 'суперсекс2': 'с помощью 4-х домкратов разорвал(а) изнутри', 'суперженсекс': 'отрезал тупым ржавым ножом клитор, вытянул через анус кишечник и задушил(а) им', 'супермужсекс': 'при помощи волка и наждачки разделил(а) на 3 части хуй', 'мяу': 'помяукал(а) с', 'пять': 'дал(а) пятюню', 'изнасиловать': 'жестоко и страстно выебал(а)', 'кастрировать': 'насильно лишил(а) половых органов', 'отравить': 'подсыпал(а) ртути и мышьяка в еду', 'отдаться': 'предоставил(а) свое тело в распоряжение', 'прижать': 'прижал(а)', 'рука': 'с уважением пожал(а) руку', 'нахуй': 'яростно послал(а) на хуй', 'понюхать': 'наслаждаясь понюхал(а)', 'чай': 'пригласил(а) на чай', 'пнуть': 'со всей дури отвесил(а) пинка', 'расстрелять': 'выпустил(а) обойму в тело', 'ущипнуть': 'ехидно ущипнул(а)', 'ударить': 'прописал(а) похоронный', 'сжечь': 'достал(а) из очка огнемет и испепелил(а)'}
			self.db.set('RPMod', 'rpcomands', comands)
		if not self.db.get('RPMod', 'rpemoji', False):
			self.db.set('RPMod', 'rpemoji', {'лизь': '👅', 'поцеловать': '💋', 'кусь': '😺', 'выебать': '🦓', 'трахнуть': '🐩', 'выпороть': '😡', 'шлепнуть': '❤', 'отлизать': '👅', 'обнять': '🐯', 'погладить': '🐯', 'укусить': '😺', 'отсосать': '💓', 'дрочнуть': '💓', 'распетрушить': '🐍', 'отигрулить': '🐯', 'засосать': '💋', 'массаж': '🤤', 'отхуярить': '😡', 'отпиздить': '🐩', 'захуярить': '🐯', 'бухнуть': '🍾', 'покормить': '🤤', 'суперсекс': '🐯', 'суперсекс2': '🐯', 'суперженсекс': '🐯', 'супермужсекс': '🐯', 'мяу': '😺', 'пять': '🙌', 'изнасиловать': '💓', 'кастрировать': '😭', 'отравить': '🤢', 'отдаться': '💋', 'прижать': '😳', 'нахуй': '😡', 'рука': '🤝', 'понюхать': '😳', 'чай': '🍵', 'пнуть': '😡', 'расстрелять': '🎉', 'ущипнуть': '😃', 'ударить': '😈', 'сжечь': '🔥'})
		if not self.db.get('RPMod', 'useraccept', False):
			self.db.set('RPMod', 'useraccept', [])

	async def dobrpcmd(self, message):
		"""Используй: .dobrp (команда) / (действие) / (эмодзи) чтобы добавить команду. Можно и без эмодзи."""
		args = utils.get_args_raw(message)
		dict_rp = self.db.get('RPMod', 'rpcomands')
		
		try:
			key_rp = str(args.split('/')[0]).strip()
			value_rp = str(args.split('/', maxsplit=2)[1]).strip()
			lenght_args = args.split('/')
			count_emoji = 0
			
			if len(lenght_args) >= 3:
				emoji_rp = str(args.split('/', maxsplit=2)[2]).strip()
				dict_emoji_rp = self.db.get('RPMod', 'rpemoji')
				
				r = emoji_rp
				lst = []
				count_emoji = 1
				for x in r:
					if x in emoji.UNICODE_EMOJI['en'].keys(): lst.append(x)
					if x.isalpha() or x.isspace() or x.isdigit() or x in string.punctuation:
						await utils.answer(message, f"<b>Были введены не только эмодзи(пробел тоже символ). </b>")
						return
				if len(lst) > 3:
					await utils.answer(message, f"<b>Было введено более 3 эмодзи.</b>")
					return
				elif not emoji_rp or not emoji_rp.strip():
					await utils.answer(message, f"<b>Разделитель для эмодзи есть, а их нет? хм.</b>")
					return
				
		
			key_len = [len(x) for x in key_rp.split()]
		
			if len(dict_rp) >= 70:
				await utils.answer(message, '<b>Достигнут лимит рп команд.</b>')
			elif not key_rp or not key_rp.strip():
				await utils.answer(message, '<b>Вы не ввели название рп команды.</b>')
			elif not value_rp or not value_rp.strip():
				await utils.answer(message, '<b>Вы не ввели действие для рп команды.</b>')
			elif int(len(key_len)) > 1:
				await utils.answer(message, '<b>В качестве рп команды было введено больше одного слова.</b>')
			elif key_rp == 'all':
				await utils.answer(message, '<b>Использовать \'<code>all</code>\' в качестве названия команды запрещено!</b>')
			elif count_emoji == 1:
				dict_emoji_rp[key_rp] = emoji_rp
				dict_rp[key_rp]= value_rp
				self.db.set('RPMod', 'rpcomands', dict_rp)
				self.db.set('RPMod', 'rpemoji', dict_emoji_rp)
				await utils.answer(message, f'<b>Команда \'<code>{key_rp}</code>\' успешно добавлена с эмодзи \'{emoji_rp}\'!</b>')
			else:
				 dict_rp[key_rp]= value_rp
				 self.db.set('RPMod', 'rpcomands', dict_rp)
				 await utils.answer(message, f'<b>Команда \'<code>{key_rp}</code>\' успешно добавлена!</b>')
		except:
			await utils.answer(message, '<b>Вы не ввели разделитель /, либо вовсе ничего не ввели.</b>')

	async def delrpcmd(self, message):
		"""Используй: .delrp (команда) чтобы удалить команду.\n Используй: .delrp all чтобы удалить все команды."""
		args = utils.get_args_raw(message)
		dict_rp = self.db.get('RPMod', 'rpcomands')
		dict_emoji_rp = self.db.get('RPMod', 'rpemoji')
		key_rp = str(args)
		count = 0
		if key_rp == 'all':
			dict_rp.clear()
			dict_emoji_rp.clear()
			self.db.set('RPMod', 'rpcomands', dict_rp)
			self.db.set('RPMod', 'rpemoji', dict_emoji_rp)
			await utils.answer(message, '<b>Список рп команд очищен.</b>')
			return
		elif not key_rp or not key_rp.strip():
			await utils.answer(message, '<b>Вы не ввели команду.</b>')
		else:
			try:
				if key_rp in dict_emoji_rp:
					dict_rp.pop(key_rp)
					dict_emoji_rp.pop(key_rp)
					self.db.set('RPMod', 'rpcomands', dict_rp)
					self.db.set('RPMod', 'rpemoji', dict_emoji_rp)
				else:
					dict_rp.pop(key_rp)
					self.db.set('RPMod', 'rpcomands', dict_rp)
				await utils.answer(message, f'<b>Команда \'<code>{key_rp}</code>\' успешно удалена!</b>')
			except KeyError:
				await utils.answer(message, '<b>Команда не найдена.</b>')

	async def rpmodcmd(self, message):
		"""Используй: .rpmod чтобы включить/выключить RP режим.\nИспользуй: .rpmod toggle чтобы сменить режим на отправку или изменение смс."""
		status = self.db.get("RPMod", "status")
		rezjim = self.db.get("RPMod", "rprezjim")
		args = utils.get_args_raw(message)
		if not args:
			if status == 1:
				self.db.set("RPMod", "status", 2)
				await utils.answer(message, "<b>RP Режим <code>выключен</code></b>")
			else:
				self.db.set("RPMod", "status", 1)
				await utils.answer(message, "<b>RP Режим <code>включен</code></b>")
		elif args.strip() == 'toggle':
			if rezjim == 1:
				self.db.set("RPMod", "rprezjim", 2)
				await utils.answer(message, "<b>RP Режим изменён на <code>отправку смс.</code></b>")
			else:
				self.db.set("RPMod", "rprezjim", 1)
				await utils.answer(message, "<b>RP Режим изменён на <code>изменение смс.</code></b>")
		else:  	
			await utils.answer(message, 'Что то не так.. ')

	async def rplistcmd(self, message):
		"""Используй: .rplist чтобы посмотреть список рп команд."""
		com = self.db.get('RPMod', 'rpcomands')
		emojies = self.db.get('RPMod', 'rpemoji')
		l = len(com)
		
		listComands = f'У вас рп команд: <b>{l}</b> из <b>70</b>. '
		if len(com) == 0:
			await utils.answer(message, '<b>Увы, у вас нету рп команд. :(</b>')
			return
		for i in com:
			if i in emojies.keys():
				listComands+=f'\n• <b><code>{i}</code> - {com[i]} |</b> {emojies[i]}'
			else:
				listComands+=f'\n• <b><code>{i}</code> - {com[i]}</b>'
		await utils.answer(message, listComands)

	async def rpnickcmd(self, message):
		"""Используй: .rpnick (ник) чтобы сменить свой ник. Если без аргументов, то вернётся ник из тг."""
		r = utils.get_args_raw(message).strip()
		nicks = self.db.get('RPMod', 'rpnicks')
		me = await message.client.get_entity(message.sender_id)
		if not r:
			nicks[str(me.id)] = me.first_name
			self.db.set('RPMod', 'rpnicks', nicks)
			await utils.answer(message, f"<b>Ник изменён на {me.first_name}</b>")
			return
		lst = []
		nick = ''
		for x in r:
			if x in emoji.UNICODE_EMOJI['en'].keys(): lst.append(x)
			if x not in emoji.UNICODE_EMOJI['en'].keys(): nick+=x
		if len(lst) > 3:
			await utils.answer(message, f"<b>Ник '{r}' содержит более трёх эмодзи.</b>")
		elif len(lst) + len(nick) >= 45:
			await utils.answer(message, f"<b>Ник превышает лимит в 45 символов(возможно эмодзи имеют длину более 1 символа).</b>")
		else:
			nicks[str(me.id)] = r
			self.db.set('RPMod', 'rpnicks', nicks)
			await utils.answer(message, f"<b>Ник изменён на {r}</b>")

	async def rpbackcmd(self, message):
		"""Бекап рп команд.\n .rpback для просмотра аргументов. """
		args = utils.get_args_raw(message).strip()
		comands = self.db.get('RPMod', 'rpcomands')
		emojies = self.db.get('RPMod', 'rpemoji')
		file_name = 'RPModBackUp.pickle'
		id = message.to_id
		reply = await message.get_reply_message()
		if not args:
			await utils.answer(message, '<b>Аргументы:</b>\n<code>-b</code> <b>-- сделать бекап.</b>\n<code>-r</code> <b>загрузить бекап.(используй с реплаем на файл)</b>')
		if args == '-b':
			try:
				await message.delete()
				dict_all = { 'rp': comands, 'emj': emojies}
				with open(file_name, 'wb') as f:
					pickle.dump(dict_all, f)
				await message.client.send_file(id, file_name)
			except Exception as e:
				await utils.answer(message, f"<b>Ошибка:\n</b>{e}")
		elif args == '-r' and reply:
			try:
				if not reply.document:
					await utils.answer(message, f"<b>Это не файл.</b>")
				await reply.download_media(file_name)
				with open(file_name, 'rb') as f:
					data = pickle.load(f)
				rp = data['rp']
				emj = data['emj']
				result_rp = dict(comands, **rp)
				result_emj = dict(emojies, **emj)
				self.db.set('RPMod', 'rpcomands', result_rp)
				self.db.set('RPMod', 'rpemoji', result_emj)
				await utils.answer(message, f"<b>Команды обновлены!</b>")
			except Exception as e:
				await utils.answer(message, f"<b>Ошибка:\n</b>{e}")
			
	async def rpblockcmd(self, message):
		"""Используй: .rpblock чтобы добавить/удалить исключение(использовать в нужном чате).\nИспользуй: .rpblock list чтобы просмотреть чаты в исключениях.\nИспользуй .rpblock (ид) чтобы удалить чат из исключений."""
		args = utils.get_args_raw(message)
		ex = self.db.get("RPMod", "exlist")
		if not args:
			a = await message.client.get_entity(message.to_id)
			if a.id in ex:
				ex.remove(a.id)
				self.db.set("RPMod", "exlist", ex)
				try:
					name = a.title
				except:
					name = a.first_name
				await utils.answer(message, f'<i>Чат <b><u>{name}</u></b>[<code>{a.id}</code>] удален из исключений.</i>')
			else:
				ex.append(a.id)
				self.db.set("RPMod", "exlist", ex)
				try:
					name = a.title
				except:
					name = a.first_name
				await utils.answer(message, f'<i>Чат <b><u>{name}</u></b>[<code>{a.id}</code>] добавлен в исключения.</i>')
		elif args.isdigit():
			args = int(args)
			if args in ex:
				ex.remove(args)
				self.db.set("RPMod", "exlist", ex)
				a = await message.client.get_entity(args)
				try:
					name = a.title
				except:
					name = a.first_name
				await utils.answer(message, f'<i>Чат <b><u>{name}</u></b>(<code>{args}</code>) удален из исключений.</i>')
			else:
				try:
					a = await message.client.get_entity(args)
				except:
					await utils.answer(message, '<b>Неверный ид.</b>')
				ex.append(args)
				self.db.set("RPMod", "exlist", ex)
				try:
					name = a.title
				except:
					name = a.first_name
				await utils.answer(message, f'<i>Чат <b><u>{name}</u></b>[<code>{a.id}</code>] добавлен в исключения.</i>')
		elif args == 'list':
			ex_len = len(ex)
			if ex_len == 0:
				await utils.answer(message, f'<b>Список исключений пуст.</b>')
				return
			sms = f'<i> Чаты, которые есть в исключениях({ex_len}):</i>'
			for i in ex:
				try:
					a = await message.client.get_entity(i)
				except:
					await utils.answer(message, f'<b>Неверный ид -- {a}</b>')
					return
				try:
					name = a.title
				except:
					name = a.first_name
				sms+=f'\n• <b><u>{name}</u> --- </b><code>{i}</code>'
			await utils.answer(message, sms)
		else:
			await utils.answer(message, 'Что то пошло не так..')

	async def useracceptcmd(self, message):
		""" Добавление/удаление пользователей, разрешенным использовать ваши команды.\n .useraccept {id/reply} """
		reply = await message.get_reply_message()
		args = utils.get_args_raw(message)
		userA = self.db.get('RPMod', 'useraccept')
		if not reply and not args:
			await utils.answer(message, 'Нет ни реплая, ни аргрументов.')
		elif args == '-l':
			sms = '<b>Пользователи, у которых есть доступ к командам:</b>'
			for i in userA:
				try:
					user = await message.client.get_entity(int(i))
					sms+= f'\n<b>• <u>{user.first_name}</u> ---</b> <code>{i}</code>'
				except:
					sms+= f'\n<b>•</b> <code>{i}</code>'
			await utils.answer(message, sms)
		elif args or reply:
			args = int(args) if args.isdigit() else reply.sender_id
			if args in userA:
				userA.remove(args)
				self.db.set('RPMod', 'useraccept', userA)
				await utils.answer(message, f'<b>Пользователю <code>{args}</code> был закрыт доступ.</b>')
			else:
				userA.append(args)
				self.db.set('RPMod', 'useraccept', userA)
				await utils.answer(message, f'<b>Пользователю <code>{args}</code> был открыт доступ.</b>')
		else:
			await utils.answer(message, 'Что то не так..')

	async def rpconfcmd(self, message):
		"""Настройка шаблона для рп"""
		conf = self.db.get("RPMod", "rpconfigurate", conf_default)
		args = utils.get_args_raw(message)
		if not args:
			sms = '⚙️ <b>Настройка шаблона для команды:</b>\n'
			s1 = '\n'.join([' | '.join([key, value[1], '✅' if value[0] else '❌']) for key, value in conf['-s1'].items()])
			s2 = '\n'.join([' | '.join([key, value[1], '✅' if value[0] else '❌']) for key, value in conf['-s2'].items()])
			sE = '\n'.join([' | '.join([key, value[1], '✅' if value[0] else '❌']) for key, value in conf['-sE'].items()])
			sS = '\n'.join([' | '.join([key, value[1], '✅' if value[0] else '❌']) for key, value in conf['-sS'].items()])
			return await utils.answer(message, f'⚙️ <b>Настройка шаблона для команды:</b>\n<code>-s1</code> --- включить/выключить стиль для "С репликой":\n{s1}\n-s2 --- аналогично для s1, но действует на саму реплику:\n{s2}\n-sE --- выбор эмодзи перед репликой:\n{sE}\n-sS --- выбор символа для разрыва строк в реплике:\n{sS}\n\nПример:\n<code>.rpconf -s1 2</code>')
		args = args.split(' ')
		if len(args) <= 1:
			return await utils.answer(message, 'Было введено меньше двух аргументов.')
		try:
			if args[0] == '-s1' or args[0] == '-s2':
				if conf[args[0]][args[1]][0]:
					conf[args[0]][args[1]][0] = False
				else:
					conf[args[0]][args[1]][0] = True
			elif args[0] == '-sE' or args[0] == '-sS':
				for i in conf[args[0]].keys():
					conf[args[0]][i][0] = False
				conf[args[0]][args[1]][0] = True
			else:
				return await utils.answer(message, 'Неизвестный аргумент.')
		except:
			return await utils.answer(message, 'Неверная цифра.')
		self.db.set("RPMod", "rpconfigurate", conf)
		await utils.answer(message, f'Конфигурация успешно изменена.')

	async def watcher(self, message):
		try:
			status = self.db.get("RPMod", "status")
			comand = self.db.get('RPMod', 'rpcomands')
			rezjim = self.db.get('RPMod', 'rprezjim')
			emojies = self.db.get('RPMod', 'rpemoji')
			ex = self.db.get("RPMod", "exlist")
			nicks = self.db.get('RPMod', 'rpnicks')
			users_accept = self.db.get('RPMod', 'useraccept')
			conf = self.db.get("RPMod", "rpconfigurate", conf_default)
			
			chat_rp = await message.client.get_entity(message.to_id)
			if status != 1 or chat_rp.id in ex: return
			me_id = (await message.client.get_me()).id
			if message.sender_id not in users_accept and message.sender_id != me_id: return
			me = (await message.client.get_entity(message.sender_id))
			
			if str(me.id) in nicks.keys():
				nick = nicks[str(me.id)]
			else:
				nick = me.first_name
			args = message.text.lower()
			
			
			lines = args.splitlines()
			tags = lines[0].split(' ')
			if not tags[-1].startswith('@'):
				reply = await message.get_reply_message()
				user = await message.client.get_entity(reply.sender_id)
			else:
				if not tags[-1][1:].isdigit():
					user = await message.client.get_entity(tags[-1])
				else:
					user = await message.client.get_entity(int(tags[-1][1:]))
				lines[0] = lines[0].rsplit(' ', 1)[0]
			detail = lines[0].split(' ',maxsplit=1)
			if len(detail) < 2:
				detail.append(' ')
			if detail[0] not in comand.keys(): return
			detail[1] = ' ' + detail[1] 
			user.first_name = nicks[str(user.id)] if str(user.id) in nicks else user.first_name
			sE = ''.join([''.join([ value[1] if value[0] else '']) for key, value in conf['-sE'].items()])
			s1 = [''.join([ value[2] if value[0] else '' for value in conf['-s1'].values()]), ''.join([ value[3] if value[0] else '' for value in dict(reversed(list(conf['-s1'].items()))).values()])]
			s2 = [''.join([ value[2] if value[0] else '' for key, value in conf['-s2'].items()]), ''.join([ value[3] if value[0] else '' for value in dict(reversed(list(conf['-s2'].items()))).values()])]
			sS = ''.join([''.join([ value[2] if value[0] else '']) for key, value in conf['-sS'].items()])
	
			rpMessageSend = ''
			if detail[0] in emojies.keys(): rpMessageSend += emojies[detail[0]] + ' | '
			rpMessageSend += f"<a href=tg://user?id={me.id}>{nick}</a> {comand[detail[0]]} <a href=tg://user?id={user.id}>{user.first_name}</a>{detail[1]}"
			if len(lines) >= 2: rpMessageSend += "\n{0} {1[0]}С репликой: {1[1]}{2[0]}{3}{2[1]}".format(sE, s1, s2, f'{sS}'.join(lines[1:]))
			if rezjim == 1:
				return await utils.answer(message, rpMessageSend)
			else:
				return await message.respond(rpMessageSend)

		except:  pass

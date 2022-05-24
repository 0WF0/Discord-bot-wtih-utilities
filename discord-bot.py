import discord
import random
from translate import Translator
import time


class MyClient(discord.Client):

    async def on_ready(self):
        print('Бот зашёл как', self.user)


    async def on_message(self, message):
        if message.author == self.user:
            return

        mes = message.content.lower()
        mess = message.content

        if mes == '!help':
            await message.channel.send('Все возможные команды и их правильное написание:' + ' ' +'1. Переводчик:!translate <с какого языка> <на какой язык> <фраза>' + ' ' + '2. Таймер:!timer <s/m/h>(сек./мин./часы) <число> <комментарий>' + ' ' + '3. Математические вычисления:!+ <1число> <2число> / !- <1число> <2число> / !* <1число> <2число> / !: <1число> <2число>' + ' ' + '4. Рандомайзеры:!r letter rus/eng(рандомная буква из рус./англ. алфавитов) / !r digit <мин.число> <макс.число>')

        if mes.startswith('!r digit'):
            await message.channel.send(random.randint(int(mess.split()[-2]), int(mess.split()[-1])))

        if mes == '!coinflip':
            s = ('Head - Орёл', 'Tail - Решка')
            await message.channel.send(random.choice(s))

        if mes == '!r letter eng':
            eng = ('abcdefghijklmnopqrstuvwxyz')
            await message.channel.send(random.choice(eng))

        if mes == '!r letter rus':
            rus = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
            await message.channel.send(random.choice(rus))

        if mes.startswith('!translate'):
            tr = Translator(from_lang = mes.split()[1], to_lang = mes.split()[2])
            await message.channel.send(tr.translate(' '.join(mess.split()[3:])))

        if mes.startswith('!*'):
            await message.channel.send(int(mess.split()[1]) * int(mess.split()[2]))

        if mes.startswith('!+'):
            await message.channel.send(int(mess.split()[1]) + int(mess.split()[2]))

        if mes.startswith('!-'):
            await message.channel.send(int(mess.split()[1]) - int(mess.split()[2]))

        if mes.startswith('!:'):
            await message.channel.send(int(mess.split()[1]) / int(mess.split()[2]))

        if mes == '!stop timer':
            global fl
            fl = False
            await message.channel.send('Таймер остановлен!')

        if mes.startswith('!timer'):

            t = int(mes.split()[2])

            if mes.split()[1] == 's':
                fl = True
                await message.channel.send('Таймер запущен!')
                while fl == True:
                    time.sleep(t)
                    await message.channel.send(mess.split(' ', 3)[3])

            if mes.split()[1] == 'm':
                fl = True
                await message.channel.send('Таймер запущен!')
                while fl == True:
                    time.sleep(t*60)
                    await message.channel.send(mess.split(' ', 3)[3])

            if mes.split()[1] == 'h':
                fl = True
                await message.channel.send('Таймер запущен!')
                while fl == True:
                    time.sleep(t*3600)
                    await message.channel.send(mess.split(' ', 3)[3])


client = MyClient()
client.run('ТОКЕН БОТА')

import config
import re

from pyrogram import Client, types, enums
from plugins import Database, Helper

        

async def send_with_pic_handler(client: Client, msg: types.Message, key: str, hastag: list):
    db = Database(msg.from_user.id)
    helper = Helper(client, msg)
    user = db.get_data_pelanggan()
    if msg.text or msg.photo or msg.video or msg.voice:
        coin = user.coin

        if coin >= config.biaya_kirim:
            coin = user.coin - config.biaya_kirim
        else:
            return await msg.reply(f'🙅🏻‍♀️ Post gagal terkirim. Koin Anda tidak mencukupi untuk mengirim pesan. Anda dapat membeli koin lebih banyak.', quote=True)

        if key == hastag[0]:
            picture = config.pic_girl
        elif key == hastag[1]:
            picture = config.pic_boy

        if user.status == 'talent':
            picture = config.pic_talentgirl
        if user.status == 'admin':
            if key == hastag[0]:
                picture = config.pic_admingirl
            elif key == hastag[1]:
                picture = config.pic_adminboy
        if user.status == 'daddy sugar':
            picture = config.pic_daddysugar
        if user.status == 'boyfriend rent':
            picture = config.pic_bfrent
        if user.status == 'girlfriend rent':
            picture = config.pic_gfrent
        if user.status == 'moans boy':
            if key == hastag[1]:
                picture = config.pic_moansboy
            elif key == hastag[0]:
                picture = config.pic_moansgirl
        elif user.status == 'moans girl':
            if key == hastag[1]:
                picture = config.pic_moansboy
            elif key == hastag[0]:
                picture = config.pic_moansgirl

        link = await get_link()
        caption = msg.text or msg.caption
        entities = msg.entities or msg.caption_entities

        kirim = await client.send_photo(config.channel_1, picture, caption, caption_entities=entities)
        await helper.send_to_channel_log(type="log_channel", link=link + str(kirim.id))
        await db.update_coin(coin)  # Perbarui jumlah koin di database
        await msg.reply(f"pesan telah berhasil terkirim. Koin Anda sekarang {coin}.")
    else:
        await msg.reply('media yang didukung photo, video dan voice')

async def send_menfess_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    db = Database(msg.from_user.id)
    db_user = db.get_data_pelanggan()
    db_bot = db.get_data_bot(client.id_bot).kirimchannel
    if msg.text or msg.photo or msg.video or msg.voice:
        if msg.photo and not db_bot.photo:
            if db_user.status in ['member', 'talent']:
                return await msg.reply('Tidak bisa mengirim photo, karena sedang dinonaktifkan oleh admin', True)
        elif msg.video and not db_bot.video:
            if db_user.status in ['member', 'talent']:
                return await msg.reply('Tidak bisa mengirim video, karena sedang dinonaktifkan oleh admin', True)
        elif msg.voice and not db_bot.voice:
            if db_user.status in ['member', 'talent']:
                return await msg.reply('Tidak bisa mengirim voice, karena sedang dinonaktifkan oleh admin', True)

        coin = db_user.coin

        if coin >= config.biaya_kirim:
            coin = db_user.coin - config.biaya_kirim
        else:
            return await msg.reply(f'🙅🏻‍♀️ post gagal terkirim. Koin Anda tidak mencukupi untuk mengirim pesan. Anda dapat membeli koin lebih banyak.', quote=True)

        link = await get_link()
        kirim = await client.copy_message(config.channel_1, msg.from_user.id, msg.id)
        await helper.send_to_channel_log(type="log_channel", link=link + str(kirim.id))
        await db.update_coin(coin)  # Perbarui jumlah koin di database
        await msg.reply(f"pesan telah berhasil terkirim. Koin Anda sekarang {coin}.")
    else:
        await msg.reply('media yang didukung photo, video dan voice')

async def get_link():
    anu = str(config.channel_1).split('-100')[1]
    return f"https://t.me/c/{anu}/"

async def transfer_coin_handler(client: Client, msg: types.Message):
    if re.search(r"^[\/]tf_coin(\s|\n)*$", msg.text or msg.caption):
        err = "<i>perintah salah /tf_coin [jmlh_coin]</i>" if msg.reply_to_message else "<i>perintah salah /tf_coin [id_user] [jmlh_coin]</i>"
        return await msg.reply(err, True)
    helper = Helper(client, msg)
    if re.search(r"^[\/]tf_coin\s(\d+)(\s(\d+))?", msg.text or msg.caption):
        if x := re.search(
            r"^[\/]tf_coin\s(\d+)(\s(\d+))$", msg.text or msg.caption
        ):
            target = x[1]
            coin = x[3]
        if y := re.search(r"^[\/]tf_coin\s(\d+)$", msg.text or msg.caption):
            if not msg.reply_to_message:
                return await msg.reply('sambil mereply sebuah pesan', True)

            if msg.reply_to_message.from_user.is_bot == True:
                return await msg.reply('🤖Bot tidak dapat ditranfer coin', True)
            elif msg.reply_to_message.sender_chat:
                return await msg.reply('channel tidak dapat ditranfer coin', True)
            else:
                target = msg.reply_to_message.from_user.id
                coin = y[1]
        if msg.from_user.id == int(target):
            return await msg.reply('<i>Tidak dapat transfer coin untuk diri sendiri</i>', True)

        user_db = Database(msg.from_user.id)
        anu = user_db.get_data_pelanggan()
        my_coin = anu.coin
        if my_coin < int(coin):
            return await msg.reply(f'<i>coin kamu ({my_coin}) tidak dapat transfer coin.</i>', True)
        db_target = Database(int(target))
        if not await db_target.cek_user_didatabase():
            return await msg.reply_text(
                text=f"<i><a href='tg://user?id={str(target)}'>user</a> tidak terdaftar didatabase</i>", quote=True,
                parse_mode=enums.ParseMode.HTML
            )
        target_db = db_target.get_data_pelanggan()
        ditransfer = my_coin - int(coin)
        diterima = target_db.coin + int(coin)
        nama = (
            "Admin"
            if anu.status in ['owner', 'admin']
            else msg.from_user.first_name
        )
        nama = await helper.escapeHTML(nama)
        try:
            await client.send_message(target, f"Coin berhasil ditambahkan senilai {coin} coin, cek /status\n└Oleh <a href='tg://user?id={msg.from_user.id}'>{nama}</a>")
            await user_db.transfer_coin(ditransfer, diterima, target_db.coin_full, int(target))
            await msg.reply(f'<i>berhasil transfer coin sebesar {coin} coin💰</i>', True)
        except Exception as e:
            return await msg.reply_text(
                text=f"❌<i>Terjadi kesalahan, sepertinya user memblokir bot</i>\n\n{e}", quote=True,
                parse_mode=enums.ParseMode.HTML
            )

    db = Database(msg.from_user.id)
    db_user = db.get_data_pelanggan()
    db_bot = db.get_data_bot(client.id_bot).kirimchannel
    if msg.text or msg.photo or msg.video or msg.voice:
        if msg.photo and not db_bot.photo:
            if db_user.status in ['member', 'talent']:
                return await msg.reply('Tidak bisa mengirim photo, karena sedang dinonaktifkan oleh admin', True)
        elif msg.video and not db_bot.video:
            if db_user.status in ['member', 'talent']:
                return await msg.reply('Tidak bisa mengirim video, karena sedang dinonaktifkan oleh admin', True)
        elif msg.voice and not db_bot.voice:
            if db_user.status in ['member', 'talent']:
                return await msg.reply('Tidak bisa mengirim voice, karena sedang dinonaktifkan oleh admin', True)

        coin = db_user.coin

        if coin >= config.biaya_kirim:
            coin = db_user.coin - config.biaya_kirim
        else:
            return await msg.reply(f'🙅🏻‍♀️ post gagal terkirim. Koin Anda tidak mencukupi untuk mengirim pesan. Anda dapat membeli koin lebih banyak.', quote=True)

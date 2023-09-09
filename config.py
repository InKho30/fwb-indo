import os

api_id = int(os.environ.get("API_ID", "24465982"))
api_hash = os.environ.get("API_HASH", "2b3131b7d3f6a42bd4ae1ba3b58c11c4")
bot_token = os.environ.get("BOT_TOKEN", "6630444051:AAF5uKmL1nlcnKX9NUI7hDslNk_8cKMdv7E")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://fwb-indo:<password>@cluster0.1upxmf0.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "menfess")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001802473399"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001626036340"))
channel_3 = int(os.environ.get("CHANNEL_3", "-1001825244023"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1001973698894"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "5633222043"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "2"))
batas_talent = int(os.environ.get("BATAS_TALENT", "2"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "2"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "2"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "2"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "2"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "2"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "12"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "10"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "10"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "10"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "10"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "10"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "10"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#FwbGirl #FwbBoy #FwbAsk #FwbFind #FwbSpill #FwbStory #NekoTalent").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://neko.ueuo.com/img/fwb-indopack/boy.jpg")
pic_girl = os.environ.get("PIC_GIRL", "https://neko.ueuo.com/img/fwb-indopack/girl.jpg")
pic_talentgirl = os.environ.get("PIC_TALENTGIRL", "https://neko.ueuo.com/img/fwb-indopack/talent.jpg")
pic_daddysugar = os.environ.get("PIC_DADDYSUGAR", "https://neko.ueuo.com/img/fwb-indopack/daddysugar.jpg")
pic_moansgirl = os.environ.get("PIC_MOANSGIRL" , "https://neko.ueuo.com/img/fwb-indopack/moansgirl.jpg")
pic_moansboy = os.environ.get("PIC_MOANSBOY" , "https://neko.ueuo.com/img/fwb-indopack/moansboy.jpg")
pic_gfrent = os.environ.get("PIC_GFRENT" , "https://neko.ueuo.com/img/fwb-indopack/gfrent.jpg")
pic_bfrent = os.environ.get("PIC_BFRENT" , "https://neko.ueuo.com/img/fwb-indopack/bfrent.jpg")
pic_owner = os.environ.get("PIC_OWNER" , "https://telegra.ph/file/f58b957f34a978524f07a.jpg")
pic_neko = os.environ.get("PIC_NEKO" , "https://telegra.ph/file/2d46007dd7d22645c4ec3.jpg")
pic_admingirl = os.environ.get("PIC_ADMINGIRL" , "https://telegra.ph/file/30c7b36f68d69840a762c.jpg")
pic_adminboy = os.environ.get("PIC_ADMINBOY" , "https://telegra.ph/file/192be803ec6722b3935ab.jpg")
# ============================================================#
pic_rekberboy = os.environ.get("PIC_REKBERBOY", "https://telegra.ph/file/78acf322385616cb5bab0.jpg")

# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Tidak dapat diakses harap join terlebih dahulu")
start_msg = os.environ.get("START_MSG", """"
{mention},Silahkan gunakan hastag:

#FwbBoy / #FwbGirl untuk Mencari Pasangan,Teman , Partner dll
#FwbAsk untuk Bertanya
#FwbStory untuk Berbagi Cerita
#FwbSpill untuk Spill Masalah
#FwbFind untuk Mencari Pasangan, Teman, Partner dll

{fullname} 🌱\n\nIni adalah bot menfess, semua pesan yang kamu kirim akan masuk ke channel secara anonymous. ketik /help""")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, pesan mu gagal terkirim silahkan gunakan hastag:

#FwbBoy / #FwbGirl untuk Mencari Pasangan,Teman , Partner dll
#FwbAsk untuk Bertanya
#FwbStory untuk Berbagi Cerita
#FwbSpill untuk Spill Masalah
#FwbFind untuk Mencari Pasangan, Teman, Partner dll
""")

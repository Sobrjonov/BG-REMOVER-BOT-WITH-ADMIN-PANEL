import sqlite3
import time
from rembg import remove
import telebot
from telebot import types
admin = "Admins ID"
bot = telebot.TeleBot("TOKEN @BotFasther dan olinadi")
@bot.message_handler(commands='start')
def start(message):
    bot.send_message(message.chat.id,"Salom Menga Rasm Yuboring Va Men Orqa Fonni Ochraman")
    try:
        con=sqlite3.connect('baza.db')
        cur=con.cursor()
        cur.execute("create table if not exists users(id integer,name text,time text)")
        cur.execute("select id from users")
        user=cur.fetchall()
        l=[]
        for i in user:
            l.append(i[0])
        if message.chat.id not in l:
            cur.execute(f"""insert into users values({message.chat.id},
                                                    '{message.from_user.first_name}',
                                                    '{time.localtime()[:5]}')""")
        con.commit()
        con.close()
    except:
        pass
panel = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
a = types.KeyboardButton("📤  Xabar  yuborish")
b = types.KeyboardButton("📊  Userlar  soni")
c = types.KeyboardButton("📤  Reklama  yuborish")
d = types.KeyboardButton("📂  Malumotlar  bazasi")
e = types.KeyboardButton("👤  Userga  yuborish")
ads=types.KeyboardButton("ADS Chat")
akt=types.KeyboardButton("Aktivlar Soni")
o = types.KeyboardButton("♻️  START")
x = types.KeyboardButton("🆘  HELP")
panel.row(a, c)
panel.row(d, b)
panel.row(e,ads)
panel.row(o, x)
panel.row(akt)

cancel = types.ReplyKeyboardMarkup(resize_keyboard=True)
l = types.KeyboardButton("❌  BEKOR  QILISH  ❌")
cancel.row(l)

def reklama(message):
    con=sqlite3.connect('baza.db')
    cur=con.cursor()

    cur.execute("SELECT rek FROM adse")
    starts=cur.fetchall()
    con.commit()
    con.close()
    bot.send_message(message.chat.id, starts[-1])


@bot.message_handler(content_types=['text'])
def admin_panel(message):
    try:
        con=sqlite3.connect('baza.db')
        cur=con.cursor()
        cur.execute("create table if not exists users(id integer,name text,time text)")
        cur.execute("select id from users")
        user=cur.fetchall()
        l=[]
        for i in user:
            l.append(i[0])
        if message.chat.id not in l:
            cur.execute(f"""insert into users values({message.chat.id},
                                                    '{message.from_user.first_name}',
                                                    '{time.localtime()[:5]}')""")
        con.commit()
        con.close()

    except:
        pass
    global link
    link = message.text
    ## -- ##  commands  ## -- ##
    if message.text == '/panel':
       bot.send_message(admin, "<b>Admin panelga hush kelipsiz !</b>", parse_mode='html', reply_markup=panel)

    elif message.text == '♻️  START':
        bot.send_message(message.chat.id, "/start - commandasini malumotlarini o'zgartirish\n\nmalumot kiriting  :", reply_markup=cancel)
        bot.register_next_step_handler(message, starts)

    elif message.text == '🆘  HELP':
        bot.send_message(message.chat.id, "/help - commandasini malumotlarini o'zgartirish\n\nmalumot kiriting  :", reply_markup=cancel)
        bot.register_next_step_handler(message, helps)

    elif message.text == '/help':
        try:
            bot.send_message(message.chat.id, helper)
        except:
            bot.send_message(message.chat.id, """Qanday ishlatish:
   1. Ijtimoiy tarmoqlardan biriga o'ting.
   2. Sizni qiziqtirgan videoni tanlang.
   3. "Nusxa olish" tugmasini bosing.
   4. Bizning botimizga yuboring va faylingizni oling!

Botni quyidagi manzildan yuklab olish mumkin:
    1. TikTok
    2. YouTube
    3.Pinterest
    4. Instagram
    5. Like""")


    ## -- ##  button  ## -- ##
    elif message.text=="ADS Chat":
        bot.send_message(message.chat.id,"'Text Ads Chat'ni Yuboring 🔼 ")
        bot.register_next_step_handler(message, adse)

    elif message.text == "👤  Userga  yuborish":
        bot.send_message(admin, "<b>👤  Userni  🆔-sini  kiriting  :</b>", parse_mode='html', reply_markup=cancel)
        bot.register_next_step_handler(message, id_ga)

    elif message.text == "📂  Malumotlar  bazasi":
        bot.send_document(message.chat.id, open("baza.db", "rb"))

    elif message.text == "📤  Xabar  yuborish":
        msg = bot.send_message(admin, "<b>Knopkasiz habar yuboring  : </b>", parse_mode='html', reply_markup=cancel)
        bot.register_next_step_handler(msg, send)

    elif message.text == "📤  Reklama  yuborish":
        msg = bot.send_message(admin, "<b>Knopkali xabar yuboring  : </b>", parse_mode='html', reply_markup=cancel)
        bot.register_next_step_handler(msg, forwar)
    elif message.text == 'Aktivlar Soni':
        aktive(message)
    elif message.text == "📊  Userlar  soni":
        con=sqlite3.connect('baza.db')
        cur=con.cursor()
        cur.execute("select id from users")
        user=cur.fetchall()
        con.commit()
        con.close()
        l=[]
        for i in user:
            l.append(i[0])
        for i in l:
            a=len(l)
        try:
            bot.send_message(admin, f"<b>👥 Umumiy foydalanuvchilar soni : {a} ta\n\n✅ Aktivlar soni : {ketti} ta\n\n❌ Spam berganlar soni {ketmadi} ta</b>", parse_mode='html')
        except:
            bot.send_message(admin, f"<b>👥 Umumiy foydalanuvchilar soni : {a} ta</b>", parse_mode='html')

    elif message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin, "<b>Bekor  qilindi  ❗</b>", parse_mode='html', reply_markup=panel)


    else:
        tphoto(message)
#Hamma userlarga habar yuborish
def aktive(message):
    
        boshi = time.time()
        con=sqlite3.connect('baza.db')
        cur=con.cursor()
        cur.execute("select id from users")
        user=cur.fetchall()
        con.commit()
        con.close()
        l=[]
        for i in user:
            l.append(i[0])
        ketti = 0
        ketmadi = 0
        for i in l:
            a = len(l)
        for i in l:
            try:
                bot.send_chat_action(i, action='typing')    
                ketti += 1
            except:
                ketmadi += 1
        oxiri = time.time()
        bot.send_message(admin, f"<b>{a}  :  ta  USER  👥\n\n{ketti}  :  tasi Aktiv  ✅\n\n{ketmadi}  :  tasi  Aktiv Emas  ❌\n\nHisoblash Vaqti  {round(boshi-oxiri)} - secundda ⏳</b>", parse_mode='html', reply_markup=panel)

    
    
    
    
def starts(message):
    global starter
    if message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin, "<b>Bekor  qilindi  ❗</b>", parse_mode='html', reply_markup=panel)
    else:
        starter = message.text
        bot.send_message(message.chat.id, "/start - commadndasi muvafaqiyatli o'zgartirildi ✅", reply_markup=panel)

def helps(message):
    global helper
    if message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin, "<b>Bekor  qilindi  ❗</b>", parse_mode='html', reply_markup=panel)
    else:
        helper = message.text
        bot.send_message(message.chat.id, "/help - comandasi muvafaqiyatli o'zgartirildi ✅", reply_markup=panel)
#Hamma userlarga habar yuborish
def adse(message):
    con=sqlite3.connect('baza.db')
    cur=con.cursor()
    cur.execute("create table if not exists ads(reklama text)")
    cur.execute("select  reklama from ads")
    user=cur.fetchall()
    l=[]
    for i in user:
        l.append(i[0])
    if message.chat.id not in l:
      cur.execute(f"""insert into ads values('{message.text}')""")
    con.commit()
    con.close()
def send(message):
    global ketti
    global ketmadi
    if message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin,"<b>Xabarni jo'natish bekor qilindi ❗</b>", parse_mode='html', reply_markup=panel)
    else:
        boshi = time.time()
        con=sqlite3.connect('baza.db')
        cur=con.cursor()
        cur.execute("select id from users")
        user=cur.fetchall()
        con.commit()
        con.close()
        l=[]
        for i in user:
            l.append(i[0])
        ketti = 0
        ketmadi = 0
        for i in l:
            a = len(l)
        for i in l:
            try:
                bot.copy_message(i, message.chat.id, message.id,disable_notification=True)
                ketti += 1
            except:
                ketmadi += 1
        oxiri = time.time()
        bot.send_message(admin, f"<b>{a}  :  ta  foydalanuvchidan  👥\n\n{ketti}  :  tasiga  yuborildi  ✅\n\n{ketmadi}  :  tasiga  yuborilmadi  ❌\n\nXabar  {round(boshi-oxiri)} - secundda userlarga yuborildi ✅</b>", parse_mode='html', reply_markup=panel)

def forwar(message):
    global ketti
    global ketmadi
    if message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin,"<b>Xabarni jo'natish bekor qilindi ❗</b>", parse_mode='html', reply_markup=panel)
    else:
        boshi = time.time()
        con=sqlite3.connect('baza.db')
        cur=con.cursor()
        cur.execute("select id from users")
        user=cur.fetchall()
        con.commit()
        con.close()
        l=[]
        for i in user:
            l.append(i[0])
        ketti = 0
        ketmadi = 0
        for i in l:
            a = len(l)
        for i in l:
            try:
                bot.forward_message(i, message.chat.id, message.id,disable_notification=True)
                ketti += 1
            except:
                ketmadi += 1
        oxiri = time.time()
        bot.send_message(admin, f"<b>{a}  :  ta  foydalanuvchidan  👥\n\n{ketti}  :  tasiga  yuborildi  ✅\n\n{ketmadi}  :  tasiga  yuborilmadi  ❌\n\nXabar  {round(boshi-oxiri)} - secundda userlarga yuborildi ✅</b>", parse_mode='html', reply_markup=panel)

#User id-siga habar yuborish
def id_ga(message):
    if message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin,"<b>Xabarni jo'natish bekor qilindi ❗</b>", parse_mode='html', reply_markup=panel)
    else:
        global id_si
        id_si = message.text
        bot.send_message(admin, "<b>Userga  yubormoqchi  bo'lgan  habaringizni  yuboring   :</b>", parse_mode='html')
        bot.register_next_step_handler(message, yub)

def yub(message):
    if message.text == "❌  BEKOR  QILISH  ❌":
        bot.send_message(admin,"<b>Xabarni jo'natish bekor qilindi ❗</b>", parse_mode='html', reply_markup=panel)
    else:
        try:
            bot.copy_message(id_si, message.chat.id, message.id,disable_notification=True)
            bot.send_message(admin, "Xabaringiz yuborildi ✅")
        except:
            bot.send_message(admin, "Xabaringiz yuborilmadi ❌")
@bot.message_handler(content_types=['photo'])
def text(message):
    try:
        con=sqlite3.connect('baza.db')
        cur=con.cursor()
        cur.execute("create table if not exists users(id integer,name text,time text)")
        cur.execute("select id from users")
        user=cur.fetchall()
        l=[]
        for i in user:
            l.append(i[0])
        if message.chat.id not in l:
         cur.execute(f"""insert into users values({message.chat.id},
                                                    '{message.from_user.first_name}',
                                                    '{time.localtime()[:5]}')""")
        con.commit()
        con.close()
    except:
        pass
    try:
        time = bot.send_message(message.chat.id,"⏳")
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)

        with open("image.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
        output_path = 'output.png'
        with open('image.jpg', 'rb') as i:
            with open(output_path, 'wb') as o:
                input = i.read()
                output = remove(input)
                o.write(output)
                bot.send_photo(message.chat.id,open('output.png','rb'))
                bot.send_document(message.chat.id,open('output.png','rb'))
                bot.send_sticker(message.chat.id,open('output.png','rb'),allow_sending_without_reply=True)
                bot.delete_message(message.chat.id, time.message_id)
    except Exception as e :
        print(e)

@bot.message_handler(content_types=['text'])
def tphoto(message):
    bot.send_message(message.chat.id,"Salom Menga Rasm Yuboring Va Men Orqa Fonni Ochraman")
bot.polling()

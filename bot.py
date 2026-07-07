from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN 8926445878:AAFRtsf2_ygxMec1_Ou8J9rQCYL1TryhjeM

# ضع هنا Chat ID الخاص بالكروب
GROUP_ID = -1000000000000


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلًا بك، أرسل رسالتك.")


async def receive_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    username = f"@{user.username}" if user.username else "لا يوجد"

    text = f"""📩 رسالة جديدة

👤 الاسم: {user.full_name}
🔗 اليوزر: {username}
🆔 ID: {user.id}

💬 الرسالة:-
{update.message.text}
"""

    await context.bot.send_message(chat_id=GROUP_ID, text=text)
    await update.message.reply_text("✅ تم إرسال رسالتك.")


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receive_message))

app.run_polling()

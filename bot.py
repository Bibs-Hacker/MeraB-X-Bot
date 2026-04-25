import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

import os
TOKEN = os.getenv("8618113338:AAHc_LBBdvat3jZ3-KIxYyYnfxGrWvar70Q")

# -------- DYNAMIC CONTENT ENGINE -------- #
categories = {
    "jokes": [f"😂 Joke #{i}: Random humor..." for i in range(1, 201)],
    "quotes": [f"💡 Quote #{i}: Stay winning." for i in range(1, 201)],
    "facts": [f"🧠 Fact #{i}: Knowledge drop." for i in range(1, 201)],
    "roasts": [f"🔥 Roast #{i}: That was embarrassing 💀" for i in range(1, 201)],
    "pickup": [f"❤️ Pickup #{i}: Smooth move..." for i in range(1, 201)],
}

# -------- START -------- #
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎮 Fun Zone", callback_data="fun")],
        [InlineKeyboardButton("🎲 Games", callback_data="games")],
        [InlineKeyboardButton("🤖 AI Chat", callback_data="ai")],
        [InlineKeyboardButton("💀 System", callback_data="system")]
    ]

    await update.message.reply_text(
        "⚠️ MERAB-X SYSTEM ONLINE ⚠️\nSelect module:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# -------- BUTTON HANDLER -------- #
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # MAIN
    if query.data == "fun":
        keyboard = [
            [InlineKeyboardButton("😂 Jokes", callback_data="jokes")],
            [InlineKeyboardButton("💡 Quotes", callback_data="quotes")],
            [InlineKeyboardButton("🧠 Facts", callback_data="facts")],
            [InlineKeyboardButton("🔥 Roasts", callback_data="roasts")],
            [InlineKeyboardButton("❤️ Pickup", callback_data="pickup")],
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ]
        await query.edit_message_text("🎮 Fun Zone:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data in categories:
        item = random.choice(categories[query.data])
        await query.edit_message_text(item)

    elif query.data == "games":
        keyboard = [
            [InlineKeyboardButton("🎲 Dice", callback_data="dice")],
            [InlineKeyboardButton("❓ Yes/No", callback_data="yesno")],
            [InlineKeyboardButton("🎯 Random", callback_data="random")],
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ]
        await query.edit_message_text("🎲 Game Zone:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "dice":
        await query.edit_message_text(f"🎲 You rolled: {random.randint(1,6)}")

    elif query.data == "yesno":
        await query.edit_message_text(random.choice(["Yes ✅", "No ❌", "Maybe 🤔"]))

    elif query.data == "random":
        all_items = sum(categories.values(), [])
        await query.edit_message_text(random.choice(all_items))

    elif query.data == "ai":
        await query.edit_message_text("🤖 AI Mode ON\nSend any message...")

    elif query.data == "system":
        await query.edit_message_text("💀 SYSTEM STATUS: ONLINE ⚡")

    elif query.data == "back":
        await start(query, context)

# -------- AI CHAT -------- #
async def ai_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if text.startswith("/"):
        return

    responses = [
        "⚡ Processing...",
        "🧠 Thinking...",
        "💀 Accessing knowledge...",
        "👁️ Observing..."
    ]

    if "love" in text:
        reply = "❤️ Emotional signal detected..."
    elif "hello" in text:
        reply = "👋 Hello human."
    elif "who are you" in text:
        reply = "💀 I am MeraB-X system."
    else:
        reply = random.choice(responses)

    await update.message.reply_text(reply)

# -------- APP -------- #
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ai_chat))

print("⚡ MeraB-X running...")
app.run_polling()

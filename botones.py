from config import *
from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton
import telebot
bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.callback_query_handler(func=lambda x: True)
def respuesta_botones_inline(call):
	cid = call.from_user.id
	mid = call.message.id
	if call.data == "lunes":
		markup = InlineKeyboardMarkup(row_width=2)
		b_atras = InlineKeyboardButton("◀️", callback_data="atras")
		b_delete = InlineKeyboardButton("❌", callback_data="delete")
		markup.add(b_atras,b_delete)
		bot.delete_message(cid, mid)
		archivo = open("turnos/lunes.td", "r", encoding="utf-8")
		contenido = archivo.read()
		archivo.close()
		bot.send_message(cid, contenido, reply_markup=markup)
		return
	if call.data == "martes":
		markup = InlineKeyboardMarkup(row_width=2)
		b_atras = InlineKeyboardButton("◀️", callback_data="atras")
		b_delete = InlineKeyboardButton("❌", callback_data="delete")
		markup.add(b_atras, b_delete)
		bot.delete_message(cid, mid)
		archivo = open("turnos/martes.td", "r", encoding="utf-8")
		contenido = archivo.read()
		archivo.close()
		bot.send_message(cid, contenido, reply_markup=markup)
	if call.data == "miercoles":
		markup = InlineKeyboardMarkup(row_width=2)
		b_atras = InlineKeyboardButton("◀️", callback_data="atras")
		b_delete = InlineKeyboardButton("❌", callback_data="delete")
		markup.add(b_atras, b_delete)
		bot.delete_message(cid, mid)
		archivo = open("turnos/miercoles.td", "r", encoding="utf-8")
		contenido = archivo.read()
		archivo.close()
		bot.send_message(cid, contenido, reply_markup=markup)
		return
	if call.data == "jueves":
		markup = InlineKeyboardMarkup(row_width=2)
		b_atras = InlineKeyboardButton("◀️", callback_data="atras")
		b_delete = InlineKeyboardButton("❌", callback_data="delete")
		markup.add(b_atras, b_delete)
		bot.delete_message(cid, mid)
		archivo = open("turnos/jueves.td", "r", encoding="utf-8")
		contenido = archivo.read()
		archivo.close()
		bot.send_message(cid, contenido, reply_markup=markup)
		return
	if call.data == "viernes":
		markup = InlineKeyboardMarkup(row_width=2)
		b_atras = InlineKeyboardButton("◀️", callback_data="atras")
		b_delete = InlineKeyboardButton("❌", callback_data="delete")
		markup.add(b_atras, b_delete)
		bot.delete_message(cid, mid)
		archivo = open("turnos/viernes.td", "r", encoding="utf-8")
		contenido = archivo.read()
		archivo.close()
		bot.send_message(cid, contenido, reply_markup=markup)
		return
	if call.data == "sabado":
		markup = InlineKeyboardMarkup(row_width=2)
		b_atras = InlineKeyboardButton("◀️", callback_data="atras")
		b_delete = InlineKeyboardButton("❌", callback_data="delete")
		markup.add(b_atras, b_delete)
		bot.delete_message(cid, mid)
		archivo = open("turnos/sabado.td", "r", encoding="utf-8")
		contenido = archivo.read()
		archivo.close()
		bot.send_message(cid, contenido, reply_markup=markup)
		return
	if call.data == "domingo":
		markup = InlineKeyboardMarkup(row_width=2)
		b_atras = InlineKeyboardButton("◀️", callback_data="atras")
		b_delete = InlineKeyboardButton("❌", callback_data="delete")
		markup.add(b_atras, b_delete)
		bot.delete_message(cid, mid)
		archivo = open("turnos/domingo.td", "r", encoding="utf-8")
		contenido = archivo.read()
		archivo.close()
		bot.send_message(cid, contenido, reply_markup=markup)
		return
	if call.data == "reservar":
		markup = InlineKeyboardMarkup(row_width=2)
		b_lunes = InlineKeyboardButton("Lunes", callback_data="lunes")
		b_martes = InlineKeyboardButton("Martes", callback_data="martes")
		b_miercoles = InlineKeyboardButton("Miercles", callback_data="miercoles")
		b_jueves = InlineKeyboardButton("Jueves", callback_data="jueves")
		b_viernes = InlineKeyboardButton("Viernes", callback_data="viernes")
		b_sabado = InlineKeyboardButton("Sabado", callback_data="sabado")
		b_domingo = InlineKeyboardButton("Domingo", callback_data="domingo")
		b_atras = InlineKeyboardButton("◀️", callback_data="atras")
		b_delete = InlineKeyboardButton("❌", callback_data="delete")
		markup.add(b_lunes, b_martes, b_miercoles, b_jueves, b_viernes, b_sabado, b_domingo, b_atras, b_delete)
		bot.delete_message(cid, mid)
		bot.send_message(cid, "Que dia quieres reservar", reply_markup=markup)
		return
	if call.data == "editar":
		bot.delete_message(cid, mid)
		bot.send_message(cid, "Introdisca la contraseña")
		return
	if call.data == "delete":
		bot.delete_message(cid, mid)
		return
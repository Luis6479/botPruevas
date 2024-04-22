import archivo
import botones
from config import *
from archivo import *
from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton
from botones import *
import telebot


bot = telebot.TeleBot(TELEGRAM_TOKEN)
port = process.env.PORT || 4000;
turns = [1]
turno = ""
#------------------Menseje de bienvenida---------------------------------------------------------
@bot.message_handler(commands=["start"])
def cmd_start(message):
	markups = InlineKeyboardMarkup(row_width=2)
	b_reserva = InlineKeyboardButton("Reservar", callback_data="reservar")
	b_editar = InlineKeyboardButton("Editar", callback_data="editar")
	markups.add(b_reserva,b_editar)
	bot.send_message(message.chat.id, "Hola", reply_markup=markups)
	bot.delete_message(message.chat.id, message.message_id)

#--------------------------Botones---------------------------------------------------------------- 
@bot.callback_query_handler(func=lambda x: True)
def respuesta_botones_inline(call):
	cid = call.from_user.id
	mid = call.message.id
	if call.data == "lunes":
		markup = InlineKeyboardMarkup(row_width=2)
		b_atras = InlineKeyboardButton("◀️", callback_data="atras")
		b_delete = InlineKeyboardButton("❌", callback_data="delete")
		markup.add(b_atras, b_delete)
		archivo = open("turnos/lunes.td", "r", encoding="utf-8")
		contenido = archivo.read()
		archivo.close()
		bot.send_message(cid, contenido, reply_markup=markup)
		bot.delete_message(cid, mid)
		return
	if call.data == "martes":
		markup = InlineKeyboardMarkup(row_width=2)
		b_atras = InlineKeyboardButton("◀️", callback_data="atras")
		b_delete = InlineKeyboardButton("❌", callback_data="delete")
		markup.add(b_atras, b_delete)
		archivo = open("turnos/martes.td", "r", encoding="utf-8")
		contenido = archivo.read()
		archivo.close()
		bot.send_message(cid, contenido, reply_markup=markup)
		bot.delete_message(cid, mid)
		return
	if call.data == "miercoles":
		markup = InlineKeyboardMarkup(row_width=2)
		b_atras = InlineKeyboardButton("◀️", callback_data="atras")
		b_delete = InlineKeyboardButton("❌", callback_data="delete")
		markup.add(b_atras, b_delete)
		archivo = open("turnos/miercoles.td", "r", encoding="utf-8")
		contenido = archivo.read()
		archivo.close()
		bot.send_message(cid, contenido, reply_markup=markup)
		bot.delete_message(cid, mid)
		return
	if call.data == "jueves":
		markup = InlineKeyboardMarkup(row_width=2)
		b_atras = InlineKeyboardButton("◀️", callback_data="atras")
		b_delete = InlineKeyboardButton("❌", callback_data="delete")
		markup.add(b_atras, b_delete)
		archivo = open("turnos/jueves.td", "r", encoding="utf-8")
		contenido = archivo.read()
		archivo.close()
		bot.send_message(cid, contenido, reply_markup=markup)
		bot.delete_message(cid, mid)
		return
	if call.data == "viernes":
		markup = InlineKeyboardMarkup(row_width=2)
		b_atras = InlineKeyboardButton("◀️", callback_data="atras")
		b_delete = InlineKeyboardButton("❌", callback_data="delete")
		markup.add(b_atras, b_delete)
		archivo = open("turnos/viernes.td", "r", encoding="utf-8")
		contenido = archivo.read()
		archivo.close()
		bot.send_message(cid, contenido, reply_markup=markup)
		bot.delete_message(cid, mid)
		return
	if call.data == "sabado":
		markup = InlineKeyboardMarkup(row_width=2)
		b_atras = InlineKeyboardButton("◀️", callback_data="atras")
		b_delete = InlineKeyboardButton("❌", callback_data="delete")
		markup.add(b_atras, b_delete)
		archivo = open("turnos/sabado.td", "r", encoding="utf-8")
		contenido = archivo.read()
		archivo.close()
		bot.send_message(cid, contenido, reply_markup=markup)
		bot.delete_message(cid, mid)
		return
	if call.data == "domingo":
		markup = InlineKeyboardMarkup(row_width=2)
		b_atras = InlineKeyboardButton("◀️", callback_data="atras")
		b_delete = InlineKeyboardButton("❌", callback_data="delete")
		markup.add(b_atras, b_delete)
		archivo = open("turnos/domingo.td", "r", encoding="utf-8")
		contenido = archivo.read()
		archivo.close()
		bot.send_message(cid, contenido, reply_markup=markup)
		bot.delete_message(cid, mid)
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
		bot.send_message(cid, "Que dia quieres reservar", reply_markup=markup)
		bot.delete_message(cid, mid)
		return
	if call.data == "editar":
		bot.delete_message(cid, mid)
		bot.send_message(cid, "Introdisca la contraseña")
		return
	if call.data == "delete":
		bot.delete_message(cid, mid)
		return

#--------------------------------------------------------------------------------------------------------------------------

                                    
if __name__ == '__main__':
   bot.set_my_commands([telebot.types.BotCommand("/start", "Da la Biembenida"),telebot.types.BotCommand("/turnos", "Muestar los Turnos"),telebot.types.BotCommand("/nuevos", "Crear turnos"),])
   print('Bot iniciado')
   bot.infinity_polling()
   print('Bot finalicado')

import time
import archivo
import botones
from config import *
from archivo import *
from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton
from botones import *
import telebot
from flask import Flask, request
from pyngrok import ngrok, conf
from waitress import serve


bot = telebot.TeleBot(TELEGRAM_TOKEN)
turns = [1]
turno = ""

web_server = Flask(__name__)
@web_server.route('/', methods=["POST"])
def webhook():
	if request.headers.get("content-type") == "application/json":
		update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
		bot.process_new_updates([update])
		return "OK",200
#------------------Menseje de bienvenida---------------------------------------------------------
@bot.message_handler(commands=["start"])
def cmd_start(message):
	markups = InlineKeyboardMarkup(row_width=1)
	b_reserva = InlineKeyboardButton("Reservar turnos", callback_data="reservar")
	b_editar = InlineKeyboardButton("Administrar turnos", callback_data="editar")
	markups.add(b_reserva,b_editar)
	bot.send_message(message.chat.id, "Hola que operacion desea realisar", reply_markup=markups)
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
   conf.get_default().config_path = "/config_ngrok.yml"
   conf.get_default().region = "eu"
   ngrok.set_auth_token(NGROK_TOKEN)
   ngrok_tunel = ngrok.connect(5000, bind_tls=True)
   ngrok_url = ngrok_tunel.public_url
   print("URL NGROG:", ngrok_url)
   bot.remove_webhook()
   time.sleep(1)
   bot.set_webhook(url=ngrok_url)
   serve(web_server, host="0.0.0.0", port=5000)
   print('Bot finalicado')

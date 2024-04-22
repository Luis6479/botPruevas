turnos=[1]
def guardar():
    archivo = open("turnos/turnos.td", "a", encoding="utf-8")
    for turnos in turns:
        archivo.write(str(turnos)+"\n")
        archivo.close()
        bot.send_message(message.chat.id, "Nuevos turnos Agregado")
	
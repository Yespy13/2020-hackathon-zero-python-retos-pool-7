import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start(update, context):
    update.message.reply_text("Hola, Geeks!")
    return "Hola, Geeks"

def help(update, context):
    update.message.reply_text("Ayudame!")
    return "Ayudame!"

def mayus(update, context):
    update.message.reply_text(context.args[0].upper())
    return context.args[0].upper()

def alreves(update, context):
    update.message.reply_text(context.args[0][::-1])
    return context.args[0][::-1]

def error(update, context):
    """Envia los errores por consola"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Inicio del Bot"""
    #Colocamos el Token creado por FatherBot
    updater = Updater("1095344826:AAGor_vw4ahEDnxIhXOPSbht9VMmWMGichM", use_context=True)

    # Es el Registro de Comandos a través del dispartcher
    #dp = 

    # Añadimos a la lista de Registro todos los comandos con su función [start - help - mayus]
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("help", help))
    updater.dispatcher.add_handler(CommandHandler("mayus", mayus))

    # Este comando es un Trigger que se lanza cuando no hay comandos [alreves]
    updater.dispatcher.add_handler(CommandHandler("", ))
    
    # Y este espera al error
    dp.add_error_handler(error)

    # Lanzamos el Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()

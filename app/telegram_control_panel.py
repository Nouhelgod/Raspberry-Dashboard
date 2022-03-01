#! /usr/bin/python3 

# Global modules
import os

# Third-party modules
import telebot

# Local modules
from lib import lib_json_wrapper as jsr
from lib import lib_telebot_keyboards as kb
from lib import lib_telebot_settings_wrapper as sw
from lib.lib_telebot_language import language_controller as locale

# Initialization
def init():
    global API_KEY, LANG, VERSION, POLLING
    POLLING = True
    API_KEY = jsr.read('user_settings.json', 'bot.api_key')
    LANG = jsr.read('app_settings.json', 'telebot.loc.language')
    VERSION = jsr.read('app_settings.json', 'app.version')
    
    if not jsr.check('app_settings.json', 'app.components.running', 'telegram_control_panel.py'):
        jsr.append('app_settings.json', 'app.components.running', 'telegram_control_panel.py')
    

# Misc functions
def delete_message(call, bot):
    bot.delete_message(chat_id=call.message.chat.id, 
                       message_id=call.message.message_id)
    
def stop(bot):
    bot.stop_polling()
    if jsr.check('app_settings.json', 'app.components.running', 'telegram_control_panel.py'):
        jsr.remove("app_settings.json", 'app.components.running', 'telegram_control_panel.py')
    


# Main loop
def main():
    try:
        bot = telebot.TeleBot(API_KEY, parse_mode='HTML')
        
        # Message handlers
        @bot.message_handler(commands=['start'])
        def message_start(message):
            response = locale.get_line(LANG, 'tag.greetings')
            
            if jsr.read('app_settings.json', 'telebot.config.slselect') == 'true':
                response += locale.get_line(LANG, 'tag.greetings.language_select')
                
            bot.send_message(chat_id=message.chat.id, 
                            text=response,
                            reply_markup=kb.start_message(LANG))
            
            
        @bot.message_handler(commands=['stop'])
        def message_stop(message):
            response = locale.get_line(LANG, 'tag.confirm_stop')
            bot.send_message(chat_id=message.chat.id,
                            text=response,
                            reply_markup=kb.generic_yn(LANG, 'confirm_stop'))
                    
            
        @bot.message_handler(commands=['select_language'])
        def message_select_language(message):
            response = locale.get_line(LANG, 'tag.select_language')
            bot.send_message(chat_id=message.chat.id, 
                            text=response,
                            reply_markup=kb.select_language(LANG, 'app_settings.json'))
        
        
        # Callback query handler              
        @bot.callback_query_handler(func=lambda call: True)
        def callback_query(call):
            callback = call.data
            
            
            if 'confirm_stop' in callback:
                if 'positive' in callback:
                    response = locale.get_line(LANG, 'tag.stop')
                    bot.send_message(chat_id=call.message.chat.id,
                                    text=response)
                    stop(bot)
                
                else:
                    delete_message(call, bot)
                    message_start(call.message)
                
                
            if 'set_language' in callback:                    
                jsr.write('app_settings.json', 'telebot.loc.language', callback.split('.')[1])
                init()
                delete_message(call, bot)
                message_start(call.message)
                
                
            if 'config' in callback and 'bot' in callback and 'set' not in callback and 'conf_bot' not in callback:
                delete_message(call, bot)
                response = f'<u><b>{locale.get_line(LANG, "button.start_message.settings_bot")}\n</b></u>'
                options_list = []
                
                # Select language
                key = 'tag.config.bot.language'
                value = 'telebot.loc.language'
                options_list = sw.add_option(LANG, options_list, key, value, 'language')
                
                # Select language with start
                key = 'tag.config.bot.slselect'
                value = 'telebot.config.slselect'
                options_list = sw.add_option(LANG, options_list, key, value, 'bool')
                
                
                for item in range(len(options_list)):
                    response += f'<b>[{item+1}] {options_list[item][3]}</b> {options_list[item][2]}\n'
                    
                bot.send_message(chat_id=call.message.chat.id,
                                text=response,
                                reply_markup=kb.generic_list(LANG, options_list, 'conf_bot'))
                    
            
            if('config' and '.rpi') in callback:
                delete_message(call, bot)
                response = f'<u><b>{locale.get_line(LANG, "button.start_message.settings_rpi")}\n</b></u>'
                response += locale.get_line(LANG, 'tag.config.rpi.main')
                
                bot.send_message(chat_id=call.message.chat.id, 
                                text=response,
                                reply_markup=kb.rpi_config(LANG))
            
            
            if 'start_message.about' in callback:
                delete_message(call, bot)
                bot.send_message(chat_id = call.message.chat.id, 
                                text = locale.get_line(LANG, 'tag.about'),
                                reply_markup=kb.about(LANG))
                
                
            if 'about.back' in callback:
                delete_message(call, bot)
                message_start(call.message)
                
                
            if 'conf_bot' in callback:
                tag = callback.split(':')[1]
                option = callback.split(':')[2]
                delete_message(call, bot)
                
                if option == 'telebot.config.slselect':
                    response = f'<b>{locale.get_line(LANG, tag)}</b>'
                    
                    bot.send_message(chat_id=call.message.chat.id,
                                    text=response,
                                    reply_markup=kb.generic_yn(LANG, option))
                    
                if option == 'telebot.loc.language':
                    response = f'<b>{locale.get_line(LANG, "tag.config.bot.lselect")}</b>'
                    
                    bot.send_message(chat_id=call.message.chat.id, 
                                    text=response,
                                    reply_markup=kb.select_language(LANG, 'app_settings.json'))
                    
            
            if 'conf_rpi' in callback:
                if 'components!' in callback:
                    delete_message(call, bot)
                    response = f'<u><b>{locale.get_line(LANG, "button.config_rpi.components")}:\n</b></u>'
                    
                    for component in jsr.read('app_settings.json', 'app.components'):
                        response += f'<code>{component}</code>\n'
                        
                    bot.send_message(chat_id=call.message.chat.id, 
                                     text=response,
                                     reply_markup=kb.start(LANG))
                
                
            if 'set:' in callback and not 'confirm_stop' in callback:
                key = callback.split(':')[1]
                param = callback.split(':')[2]
                
                if param == 'positive':
                    param = 'true'
                else:
                    param = 'false'
                    
                jsr.write('app_settings.json', key, param)
                init()
                delete_message(call, bot)
                message_start(call.message)
                
                
            if 'start!' in callback:
                delete_message(call, bot)
                message_start(call.message)
                
                        
        bot.polling()
    
    except:
        print('Fatal error in tcp.py')
        stop(bot)
    

if __name__ == '__main__':
    init()
    main()

    
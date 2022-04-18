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
    LANG = jsr.read('app_settings.json', 'tele_bot.loc.language')
    VERSION = jsr.read('app_settings.json', 'app.version')
    
    if not jsr.check('app_settings.json', 'app.components.running', 'tele_bot.py'):
        jsr.append('app_settings.json', 'app.components.running', 'tele_bot.py')
    

# Misc functions
def delete_message(call, bot):
    bot.delete_message(chat_id=call.message.chat.id, 
                       message_id=call.message.message_id)
    
def stop(bot):
    bot.stop_polling()
    if jsr.check('app_settings.json', 'app.components.running', 'tele_bot.py'):
        jsr.remove("app_settings.json", 'app.components.running', 'tele_bot.py')
    


# Main loop
def main():
    try:
        bot = telebot.TeleBot(API_KEY, parse_mode='HTML')
                
        # Message handlers
        @bot.message_handler(commands=['start'])
        def message_start(message):
            response = locale.get_line(LANG, 'tag.greetings')
            
            if jsr.read('app_settings.json', 'tele_bot.config.slselect') == 'true':
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
            
            # Stop bot
            # FIXME: (OLD METHOD)
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
                # Set language
                # FIXME: (OLD METHOD)                    
                jsr.write('app_settings.json', 'tele_bot.loc.language', callback.split('.')[1])
                init()
                delete_message(call, bot)
                message_start(call.message)
                
                
            if 'config' in callback and 'bot' in callback and 'set' not in callback and 'conf_bot' not in callback:
                delete_message(call, bot)
                
                
                response = f'<u><b>{locale.get_line(LANG, "button.start_message.settings_bot")}\n</b></u>'
                options_list = []
                
                # @ Bot configuration
                # !Select language
                key = 'tag.config.bot.language'
                value = 'tele_bot.loc.language'
                options_list = sw.add_option(LANG, options_list, key, value, 'language')
                
                # @ Bot configuration
                # !Select language with start
                key = 'tag.config.bot.slselect'
                value = 'tele_bot.config.slselect'
                options_list = sw.add_option(LANG, options_list, key, value, 'bool')
                
                
                # @ Bot configuration
                # Crate generic keyboard
                for item in range(len(options_list)):
                    response += f'<b>[{item+1}] {options_list[item][3]}</b> {options_list[item][2]}\n'
                    
                bot.send_message(chat_id=call.message.chat.id,
                                text=response,
                                reply_markup=kb.generic_list(LANG, options_list, 'conf_bot', stop=True, start=True))
                    
            # @ RPi configuration
            if('config' and '.rpi') in callback:
                delete_message(call, bot)
                
                response = f'<u><b>{locale.get_line(LANG, "button.start_message.settings_rpi")}\n</b></u>'
                response += locale.get_line(LANG, 'tag.config.rpi.main')
                
                bot.send_message(chat_id=call.message.chat.id, 
                                text=response,
                                reply_markup=kb.rpi_config(LANG))
            
            # About
            if 'start_message.about' in callback:
                delete_message(call, bot)
                bot.send_message(chat_id = call.message.chat.id, 
                                text = locale.get_line(LANG, 'tag.about'),
                                reply_markup=kb.about(LANG))
                
            # @ About
            # Back    
            if 'about.back' in callback:
                delete_message(call, bot)
                message_start(call.message)
                
            
            if 'conf_bot' in callback:
                tag = callback.split(':')[1]
                option = callback.split(':')[2]
                delete_message(call, bot)
                
                # @ Bot configuration
                # Select language on start
                if option == 'tele_bot.config.slselect':
                    response = f'<b>{locale.get_line(LANG, tag)}</b>'
                    
                    bot.send_message(chat_id=call.message.chat.id,
                                    text=response,
                                    reply_markup=kb.generic_yn(LANG, option))
                
                # @ Bot configuration
                # Select language    
                if option == 'tele_bot.loc.language':
                    response = f'<b>{locale.get_line(LANG, "tag.config.bot.lselect")}</b>'
                    
                    bot.send_message(chat_id=call.message.chat.id, 
                                    text=response,
                                    reply_markup=kb.select_language(LANG, 'app_settings.json'))
                    
            
            if 'conf_rpi' in callback:
                
                # @ RPi configuration
                # List of components
                if 'components!' in callback:
                    delete_message(call, bot)
                    response = f'<u><b>{locale.get_line(LANG, "button.config_rpi.components")}:\n</b></u>'
                    
                    for component in jsr.read('app_settings.json', 'app.components'):
                        response += f'<code>{component}</code>\n'
                        
                    bot.send_message(chat_id=call.message.chat.id, 
                                     text=response,
                                     reply_markup=kb.start(LANG))
                
                # @ RPi configuration
                # List of active components
                if 'components_running' in callback:
                    delete_message(call, bot)
                    response = f'<u><b>{locale.get_line(LANG, "button.config_rpi.components_running")}:\n</b></u>'
                    
                    for component in jsr.read('app_settings.json', 'app.components.running'):
                        response += f'<code>{component}</code>\n'
                        
                    bot.send_message(chat_id=call.message.chat.id,
                                     text = response,
                                     reply_markup=kb.start(LANG))
                
                # @ Rpi configuration
                # Autorun components
                if 'components_autorun' in callback:
                    delete_message(call, bot)
                    response = f'<u><b>{locale.get_line(LANG, "button.config_rpi.components_autorun")}:\n</b></u>'

                    options_list = []                    
                    
                    autorun = jsr.read('app_settings.json', 'app.components')
                    
                    for component in autorun:
                        component_name = component.split('.')[0]
                        
                        key = f'component.{component_name}'
                        value = f'{component_name}.autorun'
                        
                        options_list = sw.add_option(LANG, options_list, key, value, 'bool')
                        
                        
                    for item in range(len(options_list)):
                        response += f'<b>[{item+1}] {options_list[item][3]}</b> {options_list[item][2]}\n'
                    
                        
                    bot.send_message(chat_id=call.message.chat.id, 
                                     text=response,
                                     reply_markup=kb.generic_list(LANG, options_list, 'rpi.autorun', start=True)
                                     )
                        
                    
                
            # Generic settings change    
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
                
            if 'stop!' in callback:
                delete_message(call, bot)
                message_stop(call.message)
                
                        
        bot.polling()
    
    except Exception as e:
        print('Fatal error in tcp\n' + e)
        stop(bot)
    

if __name__ == '__main__':
    init()
    main()

    
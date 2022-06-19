from operator import ge
from aiogram import Dispatcher, types
from keyboards import keyboards_Client, keyboardDevice, addressInlineKeyboard
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from data_base import sqlite_db
import random
import pytesseract
import cv2
from aiogram.dispatcher.filters import Text
from aiogram import Bot 
from aiogram.dispatcher import Dispatcher
from test import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage #Хранение данных в ОЗУ

storage=MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

async def command_start(message: types.Message):
        await bot.send_message(message.from_user.id, f'Здравствуйте, <strong>{message.from_user.first_name} {message.from_user.last_name}.\n\
</strong>Вас приветствует телеграм бот <a href="https://cbmo.ru/">КГУ МО ЦБ МО</a>.\n\
Для дальнейшей работы выберите интересующий Вас раздел', reply_markup=keyboards_Client, parse_mode='HTML')
        await message.delete()

async def adress_start(message: types.Message):
    photo = open('admin/contact/contact_org.png', 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)

async def listWorker(message: types.Message):
    doc = open('admin/list/Телефоны сотрудников.pdf', 'rb')
    await message.reply_document(doc)



############################################################################################################################################################################################
#################                  callback   ######################################
async def list_menu(message: types.Message):
    await message.answer("Выберите из списка меню необходимую услугу", reply_markup=addressInlineKeyboard)

async def photo_sent(message: types.Message):
    #show_alert=True - Показывать на экране
    photo = open('admin/contact/contact_org.png', 'rb')
    await bot.send_photo(message.from_user.id,photo=photo)

async def doc_sent(message: types.Message):
    doc = open(('admin/list/Телефоны сотрудников') + '.pdf', 'rb')
    await bot.send_document(message.from_user.id, doc)






############################################################################################################################################################################################
#################                  Если "Помощь"  ОБРАБОТЧИК СОСТОЯНИЙ    ######################################
class FSMAdmin(StatesGroup):
    nameDevice = State()    
    description = State() 
    photoInventar = State()
    contactUser = State() 
    numberAppeal = State()                          

async def cm_start(message: types.Message):
    await FSMAdmin.next()
    await message.answer('Выберите устройство, которое необходимо починить', reply_markup=keyboardDevice)

async def nameDevice(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id_user'] = message.from_user.id
        data['firstname'] = message.from_user.first_name
        data['lastname'] = message.from_user.last_name
        data['name_device'] = message.text
        await FSMAdmin.next()
        await message.answer('Опишите кратко проблему, которую необходимо решить')

async def description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
        await FSMAdmin.next()
        await message.answer('Сфотографируйте инвентарный номер')

async def photoInventar(message: types.Message, state: FSMContext):
    async with state.proxy() as data:                            
        document_id = message.photo[0].file_id  # Получение уникального id для добавления в название файла
        file_info = await bot.get_file(document_id)
        path_photo = f'img/{file_info.file_unique_id}.jpg'
        print(path_photo)
        await message.photo[-1].download(path_photo)
        
        image = cv2.imread(path_photo)

###########################################################################################################################################################################################
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' #ОБЯЗАТЕЛЬНО УБРАТЬ ДЛЯ LINUX
###########################################################################################################################################################################################
        string = pytesseract.image_to_string (image, config = 'outputbase digits')
        getTextMain = string.split('\n')
        getText= [x for x in getTextMain if x]
        getUpdateText = getText.pop()  #Получение последнего элемента в списке для дальнейшей проверки на ДА/НЕТ - Корректировать!!!
       
     
      
        # print(getText2.pop())

        
        

        keyboards = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        buttons = ["Да", "Нет"]
        keyboards.add(*buttons)

        await message.answer('Подскажите, ваш инвентарный номер = ' + getUpdateText + ' ?', reply_markup = keyboards)
        await FSMAdmin.next()

        data['photo_inventar'] = getUpdateText # Для передачи в другую функцию
        data['photo_puth'] = str(path_photo)
       

async def contactUser(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if (message.text == "Да"):
            getUpdateText = data['photo_inventar']
            data['photo_puth'] = 'Считал с фото корректно'
        else:
            puth_fileUser = data['photo_puth']
            data['photo_puth'] = puth_fileUser
            data['photo_inventar'] = 'Не считал с фото'

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.KeyboardButton(text="Отправить номер 📱", request_contact=True))
        await message.answer("Отправить номер для обратной связи\n(Пожалуйста, нажмите на кнопку ниже)", reply_markup=keyboard)
        await FSMAdmin.next()

async def numberAppeal(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
         data['contact_user'] = message.contact.phone_number
         number = str(random.randint(1, 1000000))
         data['appeal'] = number        
    await message.answer('Спасибо за обращение. Номер вашей заявки = ' + data['appeal'],  reply_markup=keyboards_Client)
    await sqlite_db.sql_add_command(state)
    await state.finish()

############################################################################################################################################################################################

def register_handlers_callback(dp : Dispatcher):
    dp.register_message_handler(list_menu, commands="Другое")
    dp.register_callback_query_handler(photo_sent, Text(equals="address"))
    dp.register_callback_query_handler(doc_sent, Text(equals="numbers"))



def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(cm_start, commands=['Поддержка📝', 'support'], state=None) 
    dp.register_message_handler(listWorker, commands=['phoneorg'])
    dp.register_message_handler(adress_start, commands=['contact'])
    dp.register_message_handler(list_menu, commands=['Подробнее📋', 'other'])

    dp.register_message_handler(nameDevice, state = FSMAdmin.nameDevice)
    dp.register_message_handler(description, state = FSMAdmin.description)
    dp.register_message_handler(photoInventar, state = FSMAdmin.photoInventar, content_types='photo')
    dp.register_message_handler(contactUser, state = FSMAdmin.contactUser )
    dp.register_message_handler(numberAppeal, content_types=types.ContentType.CONTACT, state = FSMAdmin.numberAppeal)


    

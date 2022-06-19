# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


adressInlineButton = InlineKeyboardButton(text="Адрес и режим работы 🌉", callback_data="address")
numbersInlineButton = InlineKeyboardButton(text="Номера сотрудников организации 🔢", callback_data="numbers")


addressInlineKeyboard = InlineKeyboardMarkup()
addressInlineKeyboard.add(adressInlineButton).add(numbersInlineButton)



# ocrButton = KeyboardButton('/Поиск')
questionButton = KeyboardButton('/Поддержка📝')
questionButton_menu = KeyboardButton('support')
# contactButton = KeyboardButton('/Адрес🌉')
checkAppealButton = KeyboardButton('Проверить заявку 📖')
# onlineSupportButton = KeyboardButton('Онлайн-помощь 🆘')
inlineMenuButton = KeyboardButton('/Подробнее📋')

keyboards_Client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboards_Client.add(questionButton).row(checkAppealButton).add(inlineMenuButton)


##############################################################################################
#################                  КНОПКА "ПОМОЩЬ"    ######################################

devicePC = KeyboardButton('Компьютер 🖥')
devicePhone = KeyboardButton('Телефон ☎️')
devicePrinter = KeyboardButton('Принтер 🖨')
deviceOther = KeyboardButton('Другое🔌')
keyboardDevice = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboardDevice.row(devicePC,devicePhone).row(devicePrinter,deviceOther)

##############################################################################################
#################                  НОМЕР ТЕЛЕФОНА    ######################################

keyboardPhone = ReplyKeyboardMarkup(resize_keyboard=True)
keyboardPhone.add(KeyboardButton(text="Отправить номер телефона 📱", request_contact=True))
 

















 

# ##############################################################################################
# #################                  НОМЕР УПРАВЛЕНИЯ    ######################################
# buttonOne      = KeyboardButton('1️⃣')
# buttonTwo      = KeyboardButton('2️⃣')
# buttonThree    = KeyboardButton('3️⃣')
# buttonFour     = KeyboardButton('4️⃣')
# buttonFive     = KeyboardButton('5️⃣')
# buttonSix      = KeyboardButton('6️⃣')
# buttonSeven    = KeyboardButton('7️⃣')
# buttonEight    = KeyboardButton('8️⃣')
# buttonNine     = KeyboardButton('9️⃣')
# buttonTen      = KeyboardButton('🔟')
# buttonEleven   = KeyboardButton('1️⃣1️⃣')
# buttonTwelve   = KeyboardButton('1️⃣2️⃣')
# buttonThirteen = KeyboardButton('1️⃣3️⃣')
# buttonFourteen = KeyboardButton('1️⃣4️⃣')
# buttonFifteen  = KeyboardButton('1️⃣5️⃣')

# keyboards_OrgNumber= ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# keyboards_OrgNumber.row(buttonOne, buttonTwo, buttonThree).row(buttonFour, buttonFive, buttonSix)\
#     .row(buttonSeven, buttonEight, buttonNine).row(buttonTen, buttonEleven, buttonTwelve)\
#     .row(buttonThirteen, buttonFourteen, buttonFifteen)
# ##############################################################################################

##############################################################################################
#################                  ГЛАВНОЕ МЕНЮ   ######################################

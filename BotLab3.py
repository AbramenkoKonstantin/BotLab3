import telebot
import requests
import json
bot = telebot.TeleBot("1785272821:AAF0P6xd5OwL5T1cJ-kiHalnupP30tlhMng")
keyboard_change = telebot.types.ReplyKeyboardMarkup(True)
keyboard_change.row('1 задание', '/Диалог', '4 задание', '5 задание') 
button_back = telebot.types.KeyboardButton(text = '/Вернуться')
keyboard_change.add(button_back)
keyboard_first = telebot.types.ReplyKeyboardMarkup(True)
button_first = telebot.types.KeyboardButton(text = 'Новостные')
keyboard_first.add(button_first)
button_second = telebot.types.KeyboardButton(text = 'Блоги и форумы')
keyboard_first.add(button_second)
button_third = telebot.types.KeyboardButton(text = 'Подкасты')
keyboard_first.add(button_third)
keyboard_first.add(button_back)
keyboard_third = telebot.types.ReplyKeyboardMarkup(True)
keyboard_third.add(button_back)
keyboard_fourth = telebot.types.ReplyKeyboardMarkup(True)
keyboard_fourth.row('Удалить клавиатуру')
keyboard_fourth.add(button_back)
keyboard_fifth = telebot.types.ReplyKeyboardMarkup(True)
keyboard_fifth.add(button_back)



@bot.message_handler(commands=['start', 'Start'])
def startWork(startWork):
  tid = startWork.chat.id
  bot.send_message(tid, "start work!", reply_markup = keyboard_change) 

@bot.message_handler(commands=['Вернуться'])
def returnWork(returnWork):
  tid = returnWork.chat.id
  bot.send_message(tid, "start work!", reply_markup = keyboard_change)

@bot.message_handler(commands=['Диалог'])
def dialog(dialog):
  tid = dialog.chat.id
  sendName = bot.send_message(tid, "Введите свое имя")
  bot.register_next_step_handler(sendName, name)
  
def name(name):
  tid = name.chat.id
  bot.send_message(tid, "Ваше имя: " + name.text.split()[0])
  sendAge = bot.send_message(tid, "Сколько вам лет?")
  bot.register_next_step_handler(sendAge, age)

def age(age):
  tid = age.chat.id
  bot.send_message(tid, "Вам " + age.text.split()[0] + " лет")


@bot.message_handler(content_types=['voice'])
def voiceMessage(voiceMessage):
  tid = voiceMessage.chat.id
  bot.send_message(tid, "Вы отправили голосовое сообщение")


@bot.message_handler(content_types=['text'])
def textMessage(textMessage):
  tid = textMessage.chat.id
  if textMessage.text == "1 задание":
    bot.send_message(tid, "Выберите: ", reply_markup = keyboard_first)
    
  arrayNews = ([
    "Новостные:", 
    "1) 3DNews.ru – публикация новостей и аналитики в компьютерных технологиях, результатов тестирования компьютерной техники", 
    "2) Tproger.ru – интернет-издание о разработке, публикуют актуальные новости, авторские статьи и переводы.", 
    "3) Dou.ua – украинский новостной сайт с публикациями об IT-индустрии в стране и мире, а также со статистикой зарплат работников и рейтингом компаний.", 
    "4) DevBy.by – белорусский новостной сайт с публикациями об IT-индустрии в стране и мире. На сайте размещаются новости, интервью, репортажи, аналитика.", 
    "5) IXBT.com – новостной сайт с разборами техники, информационных технологий и новых программных продуктов."
  ])

  arrayBlogs = ([
    "Блоги и форумы:",
    "1) Securitylab.ru – портал, посвященный информационной безопасности.",
    "2) Nomobile.ru – журнал, посвященный гаджетам.",
    "3) Киберфорум – форум для программистов, системных администраторов, и администраторов баз данных, посвященный электронике и бытовой технике.",
    "4) Unetway.com – портал для общения между компаниями и IT-специалистами.",
    "5) Losst.ru – сайт, целиком посвященный Linux."
  ])

  arrayPodcasts = ([
    "Подкасты:",
    "1) Ted.com – собрание выступлений известных личностей – от изобретателей до обычных активистов в IT-сфере.",
    "2) Radio-t.com – разговоры на темы хайтек, высоких компьютерных технологий, гаджетов, облаков, программирования и прочего интересного из мира ИТ.",
    "3) It-trend.podster.fm – подкаст о новых продуктах от мировых компаний.",
    "4) DevZen.ru – обсуждение новостей IT, рассказы о работе и впечатления о новых продуктах.",
    "5) Razborpoletov.com – обсуждение программирования программистами."
  ])

  if textMessage.text == "Новостные":
    for counter in range(len(arrayNews)):
      bot.send_message(tid, arrayNews[counter])
      
  if textMessage.text == "Блоги и форумы":
    for counter in range(len(arrayBlogs)):
      bot.send_message(tid, arrayBlogs[counter])

  if textMessage.text == "Подкасты":
    for counter in range(len(arrayPodcasts)):
      bot.send_message(tid, arrayPodcasts[counter])

  if textMessage.text == "4 задание":
    bot.send_message(tid, "4 задание ", reply_markup = keyboard_fourth)

  if textMessage.text == "Удалить клавиатуру":
    bot.send_message(tid, "Клавиатура удалена", reply_markup=telebot.types.ReplyKeyboardRemove())

  if textMessage.text == "5 задание":
    tid = textMessage.chat.id
    urlSend = bot.send_message(tid, "Введите ссылку: ")
    bot.register_next_step_handler(urlSend, url)

def url(url):
  global req
  req = requests.get(url.text.split()[0])
  tid = url.chat.id
  bot.send_message(tid, req.text)
  infoSend = bot.send_message(tid, "Введите информацию для вывода: ")
  bot.register_next_step_handler(infoSend, info)

def info(info):
  tid = info.chat.id
  json_get = req.json()
  length = len(json_get['data'][0])
  for counter in range(length+1):
    bot.send_message(tid, json_get['data'][counter][info.text.split()[0]])



bot.polling()

import telebot
import requests
import redis
import os

botKey = '1896751220:AAE0pIOR3_nIszu2Rwka5wFDglUXLi13njI'
googleApiKey = 'AIzaSyDjGJU6nkuHjRfd1irqw9biU9ARwFsY2Ac'

bot = telebot.TeleBot(botKey)
db = redis.Redis()


class Restaurant:
    name: str
    photo: str
    location: dict

    def __init__(self, name=None, photo_path=None, location=None):
        self.name = name
        self.photo = photo_path
        self.location = location

    def __str__(self):
        return f"----------\n" \
               f"Name: {self.name}\nPhoto: {self.photo}\nLocation: {self.location}"


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Hello, I'm restaurant bot. Nice to meet you, {message.from_user.first_name}\n\n"
                          f"This bot is being used for finding restaurant near you. \n\n"
                          f"Also you can use it as notebook of restaurants which you want to visit.\n\n"
                          f"/add - To add new restaurant. You need to send 3 messages: Name, Photo, Location\n"
                          f"/list - To show all restaurants\n"
                          f"/reset - To delete all restaurants\n"
                          f"/nearby - To show all restaurants near you within 500 meters")


@bot.message_handler(commands=['add'])
def add_request(message):
    print('Add request started')
    restaurants.append(Restaurant())

    send = bot.send_message(message.chat.id, 'Enter Name of Restaurant')
    bot.register_next_step_handler(send, add_name)


@bot.message_handler(commands=['list'])
def show_restaurants(message):
    if restaurants:
        for i in restaurants:
            bot.send_message(message.chat.id, 'Restaurant Name: ' + i.name)

            with open(i.photo, 'rb') as photo:
                bot.send_photo(message.chat.id, photo)

            bot.send_location(message.chat.id, i.location.latitude, i.location.longitude)
    else:
        bot.reply_to(message, 'List is empty')


@bot.message_handler(commands=['reset'])
def del_restaurants(message):
    restaurants.clear()


@bot.message_handler(commands=['nearby'])
def nearby(message):
    print("Nearby has started")

    try:
        if message.text.lower == 'cancel':
            bot.reply_to(message, 'Canceled')
            return
    except Exception as e:
        pass

    send = bot.send_message(message.chat.id, "Send me your location")
    bot.register_next_step_handler(message, make_request)


@bot.message_handler(content_types=['location'])
def make_request(message):
    print("Make request has started")

    try:
        if message.text.lower() == 'cancel':
            bot.reply_to(message, 'Canceled')
            return
    except Exception as e:
        pass

    try:
        print(message.location)
        if message.location:
            req = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="
                               + str(message.location.latitude) + "," + str(message.location.longitude) +
                               "&radius=500&types=restaurant&key=" + googleApiKey)
            j_req = req.json()

            results = j_req['results']

            for i in results:
                name = i['name']
                location = i['geometry']['location']

                bot.send_message(message.chat.id, "Name: " + name)
                bot.send_location(message.chat.id, location['lat'], location['lng'])
        else:
            raise Exception()
    except Exception as e:
        bot.reply_to(message, "What is it?")

    pass


@bot.message_handler(content_types=['text'])
def add_name(message):
    print('Add name started')

    try:
        if message.text.lower() == 'cancel':
            bot.reply_to(message, 'Canceled')
            del restaurants[-1]
            return
    except Exception as e:
        pass

    try:
        restaurants[-1].name = message.text

        send = bot.send_message(message.chat.id, 'Send me Photo of Restaurant')
        bot.register_next_step_handler(message, add_photo)
    except Exception as e:
        bot.reply_to(message, 'What do you mean?')


@bot.message_handler(content_types=['photo'])
def add_photo(message):
    print('Add photo started')

    try:
        if message.text.lower() == 'cancel':
            bot.reply_to(message, 'Canceled')
            del restaurants[-1]
            return
    except Exception as e:
        pass

    try:
        file_id = message.photo[-1].file_id
        file = bot.get_file(file_id)
        path = file.file_path
        downloaded = bot.download_file(path)

        filename = path.split('/')[1]

        if not os.path.exists(str(message.chat.id) + '/'):
            os.mkdir(str(message.chat.id) + '/')

        photo_path = str(message.chat.id) + '/' + filename

        with open(photo_path, 'wb') as new_file:
            new_file.write(downloaded)

        restaurants[-1].photo = photo_path

        send = bot.send_message(message.chat.id, 'Send me Location of Restaurant')
        bot.register_next_step_handler(message, add_location)
    except Exception as e:
        bot.reply_to(message, 'Hahaha, lol')


@bot.message_handler(content_types=['location'])
def add_location(message):
    print('Add location started')

    try:
        if message.text.lower() == 'cancel':
            bot.reply_to(message, 'Canceled')
            del restaurants[-1]
            return
    except Exception as e:
        pass

    try:
        print(message.location)
        if message.location:
            restaurants[-1].location = message.location
        else:
            raise Exception()
        bot.send_message(message.chat.id, 'Restaurant has been added in list')
    except Exception as e:
        bot.reply_to(message, "What is it?")

    try:
        db.rpush(restaurants[-1].name, restaurants[-1].photo, restaurants[-1].location.latitude,
                 restaurants[-1].location.longitude)
    except Exception as e:
        print(e)


def read_db():
    for i in db.keys():
        name = i.decode('utf-8')
        item = db.lrange(name, 0, 3)
        photo = item[0].decode('utf-8')
        location = {'latitude': float(item[1].decode('utf-8')),
                    'longitude': float(item[2].decode('utf-8'))}

        restaurants.append(Restaurant(name, photo, location))


restaurants = []
read_db()

for i in restaurants:
    print(i)

bot.polling(none_stop=True)
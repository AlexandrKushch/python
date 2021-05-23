import redis

db = redis.Redis()


def read_db():
    results = []
    for i in db.keys():
        name = i.decode('utf-8')
        item = db.lrange(name, 0, 3)
        results[name] = {'photo': item[0].decode('utf-8'),
                             'location': {'latitude': float(item[1].decode('utf-8')),
                                          'longitude': float(item[2].decode('utf-8'))}}

    return results


restaurants = read_db()


# db = redis.Redis()
# item = {'name': 'Bufet', 'photo': '608404453/file_9.jpg', 'location_lat': 50.005959, 'location_lng': 36.248181}
# db.rpush(item['name'], item['photo'], item['location_lat'], item['location_lng'])
#
# print(db.keys())
#
# temp = db.lrange(item['name'], 0, 3)
# print(temp)
# print(type(temp[0].decode('utf-8')))
# a = float(temp[1].decode('utf-8'))
#
# restaurant = {'photo': temp[0].decode('utf-8'),
#               'location': {'latitude': float(temp[1].decode('utf-8')),
#                            'longitude': float(temp[2].decode('utf-8'))}}
#
# print(restaurant)

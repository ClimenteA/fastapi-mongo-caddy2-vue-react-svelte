import redis

r = redis.Redis()

r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})

data = r.get("Bahamas")

print(data)

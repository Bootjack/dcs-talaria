from os import environ
from olympus import Olympus

print("starting...")

truck = {
  "unitType":"VAZ Car",
  "location":{"lat":41.606128002838335,"lng":41.609857542610176},
  "liveryID":"autumn",
  "skill":"excellent"
}

olympus = Olympus({
    "port": environ["DCS_OLYMPUS_PORT"] or 5591,
    "username": environ["DCS_OLYMPUS_USERNAME"],
    "password": environ["DCS_OLYMPUS_PASSWORD"]
})
res = olympus.command("spawnGroundUnits", {"units": [truck]})

print(res.url)
print(res.request.method, res.request.url)
print(res.request.headers)
print(res.request.body)
print(res.status_code)
print(res.headers)
print(res.content)


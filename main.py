from providers import OpenMeteoProvider
from data.provinces import provinces

provider = OpenMeteoProvider()

print("Weather of Provinces:")
print("-" * 30)

for name, loc in provinces.items():
    try:
        w = provider.get_current_weather(loc["lat"], loc["lon"])
        print(f"{name}: {w['temp']:.1f}°C - Humidity {w['humidity']}%")
    except:
        print(f"{name}: Error fetching data") 
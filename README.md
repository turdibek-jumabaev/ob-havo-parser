# Ob-havo
Ob-havo malumotlarini oson olish

## O'rnatilishi kerak
```
requests==2.20.1
beautifulsoup4==4.9.3
```

## Foydalanish
Yangi `test.py` nomli fayl yaratamiz.
```python
from obHavo import Weather

obj = Weather("Ташкентe")

# bugungi malumotlarni olish
print(obj.today(max_temp=True)) # eng yuqori harorat
print(obj.today(min_temp=True)) # eng past harorat
print(obj.today(day=True))      # kun
print(obj.today(month=True))    # oy
print(obj.today(date=True))     # sana

```

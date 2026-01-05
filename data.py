# База данных процессоров: {модель: {"score": производительность, "price": цена}}
CPUS = {
    "Intel Core i3-10100": {"score": 5000, "price": 12000},
    "Intel Core i5-10400": {"score": 8000, "price": 18000},
    "Intel Core i5-12400": {"score": 12000, "price": 20000},
    "Intel Core i7-10700": {"score": 14000, "price": 28000},
    "Intel Core i7-12700": {"score": 18000, "price": 32000},
    "Intel Core i9-10900": {"score": 20000, "price": 40000},
    "Intel Core i9-12900": {"score": 25000, "price": 45000},
    "AMD Ryzen 3 3100": {"score": 6000, "price": 10000},
    "AMD Ryzen 5 3600": {"score": 10000, "price": 15000},
    "AMD Ryzen 5 5600": {"score": 13000, "price": 18000},
    "AMD Ryzen 7 3700X": {"score": 15000, "price": 25000},
    "AMD Ryzen 7 5800X": {"score": 20000, "price": 30000},
    "AMD Ryzen 9 5900X": {"score": 24000, "price": 40000},
}

# База данных видеокарт: {модель: {"score": производительность, "price": цена}}
GPUS = {
    "NVIDIA GTX 1650": {"score": 8000, "price": 20000},
    "NVIDIA GTX 1660": {"score": 12000, "price": 25000},
    "NVIDIA RTX 2060": {"score": 18000, "price": 35000},
    "NVIDIA RTX 3060": {"score": 22000, "price": 40000},
    "NVIDIA RTX 3070": {"score": 30000, "price": 60000},
    "NVIDIA RTX 3080": {"score": 40000, "price": 80000},
    "NVIDIA RTX 4060": {"score": 25000, "price": 35000},
    "NVIDIA RTX 4070": {"score": 35000, "price": 55000},
    "NVIDIA RTX 4080": {"score": 50000, "price": 90000},
    "AMD RX 580": {"score": 10000, "price": 18000},
    "AMD RX 6600": {"score": 20000, "price": 30000},
    "AMD RX 6700 XT": {"score": 28000, "price": 45000},
    "AMD RX 6800": {"score": 38000, "price": 70000},
    "AMD RX 7800 XT": {"score": 42000, "price": 60000},
}

# Масштаб разрешения экрана (влияет на нагрузку на GPU)
RESOLUTION_SCALE = {
    "1280x720": 0.5,
    "1920x1080": 1.0,
    "2560x1440": 1.8,
    "3840x2160": 3.5,
}




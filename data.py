# База данных процессоров: {модель: {"score": производительность, "price": цена}}
CPUS = {
    # Intel
    "Intel Core i3-10100": {"score": 5000, "price": 12000},
    "Intel Core i3-12100": {"score": 6500, "price": 14000},
    "Intel Core i5-10400": {"score": 8000, "price": 18000},
    "Intel Core i5-11400F": {"score": 9500, "price": 19000},
    "Intel Core i5-12400": {"score": 12000, "price": 20000},
    "Intel Core i5-12600K": {"score": 15000, "price": 27000},
    "Intel Core i7-10700": {"score": 14000, "price": 28000},
    "Intel Core i7-11700K": {"score": 17000, "price": 30000},
    "Intel Core i7-12700": {"score": 18000, "price": 32000},
    "Intel Core i9-10900": {"score": 20000, "price": 40000},
    "Intel Core i9-11900K": {"score": 24000, "price": 45000},
    "Intel Core i9-12900": {"score": 25000, "price": 45000},
    # AMD
    "AMD Ryzen 3 3100": {"score": 6000, "price": 10000},
    "AMD Ryzen 3 4100": {"score": 7000, "price": 12000},
    "AMD Ryzen 5 3600": {"score": 10000, "price": 15000},
    "AMD Ryzen 5 5600X": {"score": 13000, "price": 18000},
    "AMD Ryzen 5 7600X": {"score": 16000, "price": 22000},
    "AMD Ryzen 7 3700X": {"score": 15000, "price": 25000},
    "AMD Ryzen 7 5800X": {"score": 20000, "price": 30000},
    "AMD Ryzen 7 7700X": {"score": 23000, "price": 35000},
    "AMD Ryzen 9 5900X": {"score": 24000, "price": 40000},
    "AMD Ryzen 9 7950X": {"score": 30000, "price": 55000},
}
# База данных видеокарт: {модель: {"score": производительность, "price": цена}}
GPUS = {
    # NVIDIA
    "NVIDIA GTX 1050 Ti": {"score": 5000, "price": 15000},
    "NVIDIA GTX 1650": {"score": 8000, "price": 20000},
    "NVIDIA GTX 1660": {"score": 12000, "price": 25000},
    "NVIDIA RTX 2060": {"score": 18000, "price": 35000},
    "NVIDIA RTX 3060": {"score": 22000, "price": 40000},
    "NVIDIA RTX 3060 Ti": {"score": 26000, "price": 45000},
    "NVIDIA RTX 3070": {"score": 30000, "price": 60000},
    "NVIDIA RTX 3070 Ti": {"score": 33000, "price": 65000},
    "NVIDIA RTX 3080": {"score": 40000, "price": 80000},
    "NVIDIA RTX 4080": {"score": 50000, "price": 90000},
    "NVIDIA RTX 4090": {"score": 57000, "price": 120000},
    "NVIDIA RTX 5060": {"score": 30000, "price": 42000},
    "NVIDIA RTX 5060 Ti": {"score": 34000, "price": 47000},
    "NVIDIA RTX 5070": {"score": 40000, "price": 60000},
    "NVIDIA RTX 5070 Ti": {"score": 45000, "price": 70000},
    "NVIDIA RTX 5080": {"score": 55000, "price": 88000},
    "NVIDIA RTX 5090": {"score": 65000, "price": 120000},
    # AMD
    "AMD RX 570": {"score": 7000, "price": 10000},
    "AMD RX 580": {"score": 9000, "price": 15000},
    "AMD RX 590": {"score": 12000, "price": 20000},
    "AMD RX 6600": {"score": 20000, "price": 30000},
    "AMD RX 6600 XT": {"score": 22000, "price": 35000},
    "AMD RX 6700 XT": {"score": 28000, "price": 45000},
    "AMD RX 6800": {"score": 38000, "price": 70000},
    "AMD RX 6800 XT": {"score": 42000, "price": 75000},
    "AMD RX 7800 XT": {"score": 42000, "price": 65000},
    "AMD RX 7900 XT": {"score": 50000, "price": 80000},
}

# Масштаб разрешения экрана (влияет на нагрузку на GPU)
RESOLUTION_SCALE = {
    "1280x720": 1,
    "1920x1080": 1.5,
    "2560x1440": 1.8,
    "3840x2160": 3.5,
}








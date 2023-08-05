import asyncio

async def red_light():
    print("Red light")
    await asyncio.sleep(5)

async def yellow_light():
    print("Yellow light")
    await asyncio.sleep(3)

async def green_light():
    print("Green light")
    await asyncio.sleep(4)

# Создание цикла событий asyncio
async def main():
    await asyncio.gather(red_light(), yellow_light(), green_light())

# Запуск цикла событий asyncio
asyncio.run(main())
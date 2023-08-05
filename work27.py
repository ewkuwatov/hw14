from threading import Thread
import asyncio

# def show_products(products):
#     for i in products:
#         print(f"{i} \n цена: 20")
#
# all_pr= ["Apple", "Bread", "Burger"]
#
# t1 = Thread(target=show_products, args=(all_pr,))
# t1.start()
# print("Hello")
#
# def send_masseges(users):
#     for i in users:
#         print(f"{i} \n age:29")
#
# user_list= ["jordan", "Mike"]
#
# t1 = Thread(target=send_masseges, args=(user_list,))
# t1.start()
# print("Hello")

# async def show_products(products):
#     for i in products:
#         print(f"{i} \n цена: 20 ")
#
# all_pr= ["Apple", "Bread", "Burger"]
#
# asyncio.run(show_products(all_pr))
# print("Hello world")

# async def show_products(products):
#     for i in products:
#         print(f"{i} \n цена: 20 ")
#
# all_pr= ["Apple", "Bread", "Burger"]
#
# asyncio.run(show_products(all_pr))
# print("Hello world")
#
# async def main():
#     task1 = (asyncio.run(main()))

async def show_products(products):
    for i in products:
        print(f"{i} \nЦена: 20$")

all_pr = ["Apple", "Bread", "Burger"]

asyncio.run(show_products(all_pr))
print("Hello world")
    


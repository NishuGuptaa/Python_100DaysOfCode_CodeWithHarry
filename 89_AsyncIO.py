import asyncio
import time
import requests

async def function1():
    URL = "https://www.peakpx.com/en/hd-wallpaper-desktop-ambfb"
    response = requests.get(URL)
    open("wikipidia.jpg", "wb").write(response.content)
    # time.sleep(3)
    await asyncio.sleep(1)
    print("func 1")
    return "func 1"

async def function2():
    URL = "https://www.pinterest.com/pin/photography-logo-camera-concept-design--55239532907888725/"
    response = requests.get(URL)
    open("camera.jpg", "wb").write(response.content)
    # time.sleep(3)
    await asyncio.sleep(1)
    print("func 2")

async def function3():
    URL = "https://4kwallpapers.com/technology/google-logo-5k-8k-11298.html"
    response = requests.get(URL)
    open("google.jpg", "wb").write(response.content)
    # time.sleep(3)
    await asyncio.sleep(4)
    print("func 3")

async def main():
    # task = asyncio.create_task(function1())
    # await function1()
    # await function2()
    # await function3()

    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)

asyncio.run(main())
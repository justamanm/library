import aiohttp
import requests

import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://127.0.0.1:8080/", verify_ssl=False) as resp:
            ret = await resp.text()
            print(ret)


asyncio.run(main())
# resp = requests.get("https://www.baidu.com")
# print(resp.content.decode())

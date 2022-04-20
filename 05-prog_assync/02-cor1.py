import asyncio


async def diz_oi():
    print('Oi....')


el = asyncio.get_event_loop()
el.run_until_complete(diz_oi())
el.close()

import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response_status = response.status
            response_text = await response.text()
            return response_status, response_text

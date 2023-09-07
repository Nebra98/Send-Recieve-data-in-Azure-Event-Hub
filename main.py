import asyncio
from config import EVENT_HUB_FULLY_QUALIFIED_NAMESPACE, EVENT_HUB_NAME, SAS_POLICY_NAME, SAS_KEY
from http_utils import fetch_url
from event_hub_utils import send_log_to_event_hub

URLs_to_check = [
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4",
]

async def main():
    tasks = [fetch_url_and_log(url) for url in URLs_to_check]
    await asyncio.gather(*tasks)

async def fetch_url_and_log(url):
    response_status, response_text = await fetch_url(url)
    log_message = f"Request to {url} succeeded with response: {response_text}"
    
    if response_status == 200:
        await send_log_to_event_hub(
            log_message,
            EVENT_HUB_FULLY_QUALIFIED_NAMESPACE,
            EVENT_HUB_NAME,
            SAS_POLICY_NAME,
            SAS_KEY
        )
    else:
        print(f"Request to {url} failed with status code: {response_status}")

if __name__ == "__main__":
    asyncio.run(main())

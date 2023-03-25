import asyncio
import requests
from concurrent.futures import ThreadPoolExecutor


def fetch_urls(urls):
    return asyncio.gather(
        *[loop.run_in_executor(executor, requests.get, url) for url in urls]
    )


if __name__ == "__main__":
    executor = ThreadPoolExecutor(max_workers=3)
    loop = asyncio.get_event_loop()

    responses = loop.run_until_complete(
        fetch_urls(
            [
                "http://www.google.com",
                "http://www.linkedin.com",
                "http://www.facebook.com"
            ]
        )
    )

    print(responses)
from concurrent.futures import ThreadPoolExecutor
from concurrent import futures
from app.scrap import get_soup, get_title, get_paragraphs, get_links
from webs import websites
import json
from datetime import datetime

list_data = []


def scrap_web(link: str, title_selector: str, paragraph_selector: str) -> dict | None:
    soup = get_soup(link=link)
    title = get_title(soup=soup, selector=title_selector)
    paragraph = get_paragraphs(soup=soup, selector=paragraph_selector)
    print(title)
    if title and paragraph:
        return {"link": link, "title": title, "paragraph": paragraph}


for web in websites:
    links = get_links(web.get("index"))
    with ThreadPoolExecutor(max_workers=25) as executor:
        # results = list(executor.map(process_website, websites))
        futures_result = [
            executor.submit(
                scrap_web,
                link,
                web.get("title_selector"),
                web.get("paragraph_selector"),
            )
            for link in links
        ]
        for future in futures.as_completed(futures_result):
            result = future.result()
            if result:
                list_data.append(result)

json_obj = json.dumps(list_data, indent=4)

with open(f"data-{datetime.now()}.json", "w") as outfile:
    outfile.write(json_obj)

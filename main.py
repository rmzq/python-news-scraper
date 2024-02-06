from app.scrap import get_soup, get_title, get_paragraphs, get_links
from webs import websites
import json

web = websites[0]

list_data = []
for web in websites:
    links = get_links(web.get("index"))
    for l in links:
        soup = get_soup(link=l)
        title = get_title(soup=soup, selector=web.get("title_selector"))
        paragraph = get_paragraphs(soup=soup, selector=web.get("paragraph_selector"))
        if title and paragraph:
            list_data.append({"link": l, "title": title, "paragraph": paragraph})
        print(l, title)

json_obj = json.dumps(list_data, indent=4)

with open("data.json", "w") as outfile:
    outfile.write(json_obj)

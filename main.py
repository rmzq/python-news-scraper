from app.scrap import get_soup, get_title, get_paragraphs, get_links
from webs import websites
import json

# print(hello_world())

# soup = get_soup(
#     "https://www.cnnindonesia.com/olahraga/20240205084904-142-1058612/rincian-gaji-mbappe-di-real-madrid-dibarengi-bonus-fantastis"
# )

# title = get_title(soup)
# pr = get_paragraphs(soup)
# print(get_links("https://www.cnnindonesia.com/"))
web = websites[0]
links = get_links(web.get("index"))

list_data = []

for l in links:
    soup = get_soup(link=l)
    title = get_title(soup=soup, selector=web.get("title_selector"))
    paragraph = get_paragraphs(soup=soup, selector=web.get("paragraph_selector"))
    if title and paragraph:
        list_data.append({"link": l, "title": title, "paragraph": paragraph})
    print(title)

json_obj = json.dumps(list_data, indent=4)

with open("data.json", "w") as outfile:
    outfile.write(json_obj)

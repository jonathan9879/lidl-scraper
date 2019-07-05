from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://www.lidl.es/es/index.htm')

promo_links = r.html.links
print(promo_links)

promo_links = filter(lambda x: x.startswith("/es/promo"), promo_links)
promo_links = list(filter(lambda x: x.endswith("week=1"), promo_links))
print(promo_links)

list_of_desired_items = ["Pizza", "Gazpacho", "Pasta rellena", "salmón"]

for link in promo_links:
    r = session.get('https://www.lidl.es'+link)

    products_on_sale = r.html.find(".productgrid__item")

    for item in products_on_sale:
        if any(product in item.text for product in list_of_desired_items):
            print(item.text + "\n")




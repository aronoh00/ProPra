from bs4 import BeautifulSoup

# A1
with open("/home/aron/ws/propra/beautifulsoup/Python-Standardbibliothek.html", "r") as file:
    html_doc = file.read()

# A2
soup = BeautifulSoup(html_doc, "html.parser")

# A3 und A4
def is_difficulty_one_or_two(tag):
    if tag.name == "span" and tag.get("class") and any("difficulty1" in c or "difficulty2" in c for c in tag.get("class")):
        for parent in tag.parents:
            if parent.name == "nav":
                return True
    return False

tags = soup.find_all(is_difficulty_one_or_two)

number_of_tags = 0
for tag in tags:
    print(tag)
    number_of_tags += 1

# A5
print("number of <span> tags declaring difficulty 1 or 2:", number_of_tags)

# A6
timevalues_total = 0.00

for tags in tags:
    parent_div = tags.find_parent("div")
    if parent_div:
        timevalue_tag = parent_div.find("span", class_="timevalue-decoration")
        if timevalue_tag:
            try:
                timevalue = float(timevalue_tag.get_text(strip=True))
                timevalues_total += timevalue
            except ValueError:
                continue

print("Their total timevalue: %.2f" % timevalues_total)

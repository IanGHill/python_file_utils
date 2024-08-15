from bs4 import BeautifulSoup  # this module helps in web scrapping.
import requests  # this module helps us to download a web page

# html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
# soup = BeautifulSoup(html, "lxml")
# # print(soup.prettify())
# tag_object = soup.title
# print("tag object:", tag_object)
# tag_object = soup.h3
# print("tag object:", tag_object)
# sibling_1 = tag_object.next_sibling
# print("sibling 1:", sibling_1)
# tag_child = tag_object.b
# print("tag child id", tag_child["id"])
# print("tag child id", tag_child.get("id"))
# print("tag child attrs", tag_child.attrs)
# print("tag child string", tag_child.string)
# print(type(tag_child.string))
# unicode_string = str(tag_child.string)
# print(unicode_string)

table = "<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"

table_bs = BeautifulSoup(table, "lxml")
# print(table_bs.prettify())
table_rows = table_bs.find_all("tr")
first_row = table_rows[0]
print(first_row)
print(type(first_row))
print(first_row.td)

for i, row in enumerate(table_rows):
    print("row", i, "is", row)

for i, row in enumerate(table_rows):
    print("row", i)
    cells = row.find_all("td")
    for j, cell in enumerate(cells):
        print("column", j, "cell", cell)

list_input = table_bs.find_all(name=["tr", "td"])
print(list_input)

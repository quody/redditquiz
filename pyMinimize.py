with open('dist/index.html', 'r') as content_file:
	page = content_file.read()

with open('dist/styles/main.css', 'r') as content_file:
	styles = content_file.read()

with open('dist/mini.js', 'r') as content_file:
	script = content_file.read()

with open('dist/images.json', 'r') as content_file:
	data = content_file.read()

styled = page.split("<!-- style -->")
styled[1] = "<style>" + styles + "</style>"
page = "".join(styled)

dataed = script.split("a=\"Replace from here\"")
dataed[1] = "treeData=" + data
script = "".join(dataed)

scripted = page.split("<!-- script -->")
scripted[1] = "<script>" + script + "</script>"
page = "".join(scripted)

f = open("index.html", "w")
f.write(page)
f.close()

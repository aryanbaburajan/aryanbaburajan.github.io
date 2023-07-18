import os
import shutil
import markdown

shutil.rmtree("./docs")
shutil.copytree("./src", "./docs")

(header, footer) = open("./docs/template.html").read().split("<CONTENT/>")
os.remove("./docs/template.html")

for subdir, dirs, files in os.walk("./docs"):
    for file in files:
        if (file.endswith(".md")):
            os.rename(os.path.join(subdir, file), os.path.join(subdir, file).replace(".md", ".html"))
            md = open(os.path.join(subdir, file).replace(".md", ".html"), "r").read()
            html = open(os.path.join(subdir, file).replace(".md", ".html"), "w")
            html.write(header + markdown.markdown(md) + footer)
            html.close()

print("Static Site Generated.")
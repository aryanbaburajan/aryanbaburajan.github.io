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

for subdir, dirs, files in os.walk("./docs"):
    for file in files:
        if (file.endswith(".html")):
            md = open(os.path.join(subdir, file).replace(".md", ".html"), "r").read()

            if ("<py>" in md):
                code = md.split("<py>")[1]
                code = code.split("</py>")[0]

                context = {}
                exec(code, context)
                value = context['main']()

                s_idx = md.find('<py>')
                e_idx = md.find('</py>') + len('</py>')
                md = md[:s_idx] + value + md[e_idx:]

            htmlSite = header + markdown.markdown(md) + footer

            relative_path = os.path.relpath(os.path.join(subdir, file), start="./docs")
            depth = len(relative_path.split(os.path.sep))
            htmlSite = htmlSite.replace("<ROOT/>", depth * ".")

            html = open(os.path.join(subdir, file).replace(".md", ".html"), "w")
            html.write(htmlSite)
            html.close()


print("Static Site Generated.")
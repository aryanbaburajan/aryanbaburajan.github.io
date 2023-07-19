import os
import shutil
import markdown

def preprocess_py(htmlSite):
    start_tag = "<py>"
    end_tag = "</py>"

    while start_tag in htmlSite and end_tag in htmlSite:
        s_idx = htmlSite.find(start_tag)
        e_idx = htmlSite.find(end_tag) + len(end_tag)

        code = htmlSite[s_idx + len(start_tag):e_idx - len(end_tag)]
        context = {}
        exec(code, context)
        value = context['main']()

        htmlSite = htmlSite[:s_idx] + value + htmlSite[e_idx:]

    return htmlSite

def generate():
    shutil.rmtree("./docs")
    shutil.copytree("./src", "./docs")

    (header, footer) = open("./docs/template.html").read().split("<CONTENT/>")
    os.remove("./docs/template.html")

    for subdir, dirs, files in os.walk("./docs"):
        for file in files:
            if file.endswith(".md"):
                os.rename(os.path.join(subdir, file), os.path.join(subdir, file).replace(".md", ".html"))

    for subdir, dirs, files in os.walk("./docs"):
        for file in files:
            if file.endswith(".html"):
                md = open(os.path.join(subdir, file).replace(".md", ".html"), "r").read()

                htmlSite = header + markdown.markdown(md) + footer

                # <py> preprocessor
                htmlSite = preprocess_py(htmlSite)

                # <ROOT/> preprocessor
                relative_path = os.path.relpath(os.path.join(subdir, file), start="./docs")
                depth = len(relative_path.split(os.path.sep))
                htmlSite = htmlSite.replace("<ROOT/>", depth * ".")

                html = open(os.path.join(subdir, file).replace(".md", ".html"), "w")
                html.write(htmlSite)
                html.close()
    print("Static Site Generated.")

generate()
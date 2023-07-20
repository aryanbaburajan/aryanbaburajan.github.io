# Hey.
I'm **Aryan**, a **programmer**, **music enthusiast** and an
**inquisitive human**. I love building things — games, applications, libraries, or
tools that change the way things work. I specialize in C++, with which I'm
currently developing a game engine, [**Ducktape**](https://github.com/DucktapeEngine/Ducktape), 
using OpenGL.

Want to say hi? Feel free! [Mail](mailto:aryanbaburajan2007@gmail.com)

Got an internship? [Resume](./resume.pdf)

### Software Developer
- Ducktape - Open source, C++, OpenGL 3D game engine that focuses on being fast, and powerful.
- Speaker at KochiFOSS - Gave a talk about Ducktape as a Speaker in the KochiFOSS event held at Kochi by the FOSSUnited organization.
- Emotify - JavaScript library for adding custom emotes into your website.
- DirectShare - File sharing service made with Node.js.
- aryanbnb - Static Site Generator, just for this portfolio.

### Game Developer 
- Duck Duck Golf - 3d golf obstacle course.
- Chaos just kinda had its charm I guess - Explosive simulator where you drive over houses and Nuke an entire city.
- Woosh! - Train sandbox.
- Hectagon - Procedural island generator.

### Art Developer?
- The First Donut - First Donut made with Blender.

### Blog
<py>
import os
from datetime import datetime
def main():
    md = "<ul>"
    os.chdir("./src/blog/")
    files = os.listdir("./")
    files.sort(key=os.path.getmtime)
    files = reversed(files)
    os.chdir(os.path.dirname(os.path.dirname(os.getcwd())))
    for filename in files:
        f = os.path.join("./src/blog/", filename)
        if os.path.isfile(f) and filename.endswith(".md"):
            href = './blog/' + filename.replace(".md", ".html")
            title = filename.split(".")[0].title()
            time = os.path.getmtime('./src/blog/' + filename)
            date = date = datetime.fromtimestamp(time).strftime('%Y-%m-%d')
            md += f'<li>{date} — <a href="{href}">{title}</a></li>\n'
    md += "</ul>"
    return md
</py>
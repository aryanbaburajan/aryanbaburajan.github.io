# Hey.
I'm **Aryan**, a **programmer**, **music enthusiast** and an
**inquisitive human**. I love building things — games, applications, libraries, or
tools that change the way things work. I specialize in C++, with which I'm
currently developing a game engine, [**Ducktape**](https://github.com/DucktapeEngine/Ducktape), 
using OpenGL.

Want to say hi? Feel free! [Mail](mailto:aryanbaburajan2007@gmail.com)

Got an internship? [Resume](./resume.pdf)

### Software Developer
- [Ducktape](https://github.com/ducktapeengine/ducktape) - Open source, C++, OpenGL 3D game engine that focuses on being fast, and powerful.
- [Speaker at KochiFOSS](https://www.youtube.com/watch?v=m9-Aq3A2LyY) - Gave a talk about Ducktape as a Speaker in the KochiFOSS event held at Kochi by the FOSSUnited organization.
- [Emotify](https://emotify.js.org) - JavaScript library for adding custom emojies into your website.
- [DirectShare](https://github.com/aryanbaburajan/directshare) - File sharing service made with Node.js.
- [aryanbnb](https://github.com/aryanbaburajan/aryanbaburajan.github.io) - Static Site Generator, just for this portfolio.

### Game Developer 
- [Duck Duck Golf](https://aryanbaburajan.itch.io/duck-duck-golf) - 3d golf obstacle course.
- [Chaos just kinda had its charm I guess](https://aryanbaburajan.itch.io/chaos-just-kinda-had-its-charm-ig) - Explosive simulator where you drive over houses and Nuke an entire city.
- [Woosh!](https://aryanbaburajan.itch.io/woosh) - Train sandbox.
- [Hectagon](https://aryanbaburajan.itch.io/hectagon) - Procedural island generator.
- [VROOM](https://aryanbaburajan.itch.io/vroom) - Procedurally generated racing game prototype.

### Art Developer?
- [The First Donut](https://www.youtube.com/shorts/9RT5-4zbPNM) - First Donut made with Blender.

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
            title = filename.split(".")[0].replace("-", " ").title()
            time = os.path.getmtime('./src/blog/' + filename)
            date = date = datetime.fromtimestamp(time).strftime('%Y-%m-%d')
            md += f'<li>{date} — <a href="{href}">{title}</a></li>\n'
    md += "</ul>"
    return md
</py>
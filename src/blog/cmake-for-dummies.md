# CMake for Dummies
You want to get started with C++ projects, I get it.
CMake gives you manual control over how to build libraries/build applications/link libraries/include files etc. And you control these properties with the `CMakeLists.txt` file, which would be the base of your project.

To clear things up beforehand, as always in C++, there are multiple ways of doing things. And as such, I have my own preferred way of adding external libraries to my project. I use an in-source-build method, so the respective libraries are added in to my source code (by perhaps using git submodules, though it's not necessary).

Let's say we were making a game using [Raylib](https://raylib.com/). Here's how I would do it.

- Initial repository structure:
    - Extern/ (call it External/Lib/Libraries or whatever)
    - Include/ 
    - Src/
    - CMakeLists.txt

- Since we're using Raylib, get its source code from [Github](https://github.com/raysan5/raylib/releases), and extract it in `Extern/Raylib`
- Create `Src/Main.cpp` and copy paste the [basic window creation code](https://www.raylib.com/examples/core/loader.html?name=core_basic_window). (Note that this tutorial is about CMake, not Raylib, so we will not be getting into that.)
- Now's the time to get into writing the CMake configuration file.
- This is what it would look like at the end:
```
cmake_minimum_required(VERSION 3.25)
set (CMAKE_CXX_STANDARD 17)
project("Doom")
add_subdirectory("${PROJECT_SOURCE_DIR}/Extern/Raylib")
add_executable(Doom "${PROJECT_SOURCE_DIR}/Src/Main.cpp")
target_include_directories(Doom PUBLIC "${PROJECT_SOURCE_DIR}/Extern/Raylib/src")
target_link_libraries(Doom PUBLIC raylib)
```
- `cmake_minimum_required(VERSION 3.25)
set (CMAKE_CXX_STANDARD 17)`
	Take this as the boilerplate. The first line defines the minimum version of CMake required to build your project. The second, defines the C++ version to use (which in this case is C++17, which I mostly prefer.)
- `project("Doom")`
	Pretty obvious tbh, define the project name (yes I called it Doom).
- `add_subdirectory("${PROJECT_SOURCE_DIR}/Extern/Raylib")`
	Now this is where the magic happens.
	In short, `add_subdirectory()` adds a sub-cmake-project that exists within your project, to the list of projects to compile. Essentially, we're telling CMake to compile Raylib's source code before it compiles ours.
- `add_executable(Doom "${PROJECT_SOURCE_DIR}/Src/Main.cpp")`
	Compile the provided source files `Main.cpp` into an executable `Doom`
- `target_include_directories(Doom PUBLIC "${PROJECT_SOURCE_DIR}/Extern/Raylib/src")`
	Add the `Extern/Raylib/src` dir to the include directories of our project so we can include the right Raylib headers with `#include "raylib.h"`
- `target_link_libraries(Doom PUBLIC raylib)`
	Finally, link the Raylib library.

Now it's time to build it.
Go to the root of your project, and run these commands.
`mkdir Build`
`cd Build`
`cmake ..`
`make`

Reminds me, I never went through how to install CMake and Make. That's funny, but let's just hope you figure that part out somehow. Make is usually pre-installed when you install MinGW but if not, ([CMake](https://cmake.org/install/), [Make](https://stackoverflow.com/a/54086635))

Anyways, if you get the "Congrats! You created your first window!" window when running the program, which is in `Build/` Congratulations! You've succeeded.

You've got the basics of linking an external library. Though this process may differ for other libraries, I'm sure you can find resources on that.
Here's one:
- [OpenGL](https://stackoverflow.com/a/9469349)

Now this post is by no means an extensive tutorial on CMake. It's just to get your feets dipped. Go figure the rest of it yourself, that's what a programmer's job is.

For any help, feel free to ask on my [Discord server](https://dsc.gg/ducktape).
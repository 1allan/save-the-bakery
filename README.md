# Save The Bakery

This game was made as a assignement of "Object-Oriented Programming I", a course of Computer Science at UFSC.

The assignement consisted in develop a project and its class diagram containing the basic concepts of OOP: abstraction, encapsulation, inheritance and polymorphism. Since the deadline was too short and I had some tests to study and another assignements to do, I couldn't finish it how I wanted and there are still some bugs left.

I choose to use [Poetry](https://python-poetry.org/) as project manager due to its practicality - even it's bit overkill in this case, since I'm using only Pygame as external package - but you can install the dependencies directly or use a [virtualenv](https://docs.python.org/3/tutorial/venv.html).

<img src="images/stb.gif">

## How to run it

1. Clone the repository and go to `save-the-bakery/`
    ```bash 
    git clone http://github.com/1allan/save-the-bakery
    cd save-the-bakery/
    ``` 

2. Install dependencies
    ```bash
    python install -r requirements.txt
    ```

3. Go to `save_the_bakery/` and run the `__main__.py` file
    ```bash
    cd save_the_bakery/
    python __main__.py
    ```
# Coding Tutorials

## Learning to code in Python ...

### Python Tutorials

Here are useful ressources for teaching Python: 
1. [Hour of Code](https://hourofcode.com/),
2. [Using Python without installation](https://python.infobrisson.fr/),
3. [Learn to code using blocks and convert it into Python code](https://fr.vittascience.com/python)
4. [Install Python on your computer](https://www.python.org/)
5. [Free and open-source computing environment based on Python](https://pyzo.org/)
6. [Use the Turtle to learn and teach Python](https://docs.python.org/3/library/turtle.html)
7. [Think Python: Introduction to Python programming for beginners](https://greenteapress.com/wp/think-python/)
8. [Apprentissage de la programmation: Ressources didactiques Gérard Swinnen](https://inforef.be/swi/python.htm)
9. [Using Scratch knowledge of learners to teach Python  in class](https://www.pedagogie.ac-nantes.fr/mathematiques/enseignement/groupe-de-recherche/2017-2019/de-scratch-vers-python-1132341.kjsp?RH=1510509626265)
10. [EduPython](https://edupython.tuxfamily.org/)
11. [Teaching algorithms](https://www.ac-clermont.fr/disciplines/fileadmin/user_upload/Mathematiques/pages/Telecharger/Une_demarche_pedagogique_pour_l_apprentissage_de_l_algorithmique.pdf)
12. [Online debugging tool that helps you to visualize your code](http://pythontutor.com/visualize.html#mode=edit)
13. [Learn to code through Pygames](using-pygames.html)

### ... using MicroPython

[MicroPython: the *machine* library](http://docs.micropython.org/en/latest/library/machine.html)

### ... on a RaspberryPi

- The *MagPi* [magazines](https://magpi.raspberrypi.org/issues/) and [books](https://magpi.raspberrypi.org/books)
are a valuable (but free) source to find inspiration for projects related to your [Raspberry Pi](https://www.raspberrypi.org/).
- [Using Sense HAT](https://tarikgit.github.io/coding/using-sensehat.html): *The Sense HAT on the Raspberry Pi is an excellent tool for students to start scientific projects. Although it has been designed for the [Astro Pi](https://astro-pi.org/) it can be used in so many other interesting projects*.
- [Using Raspberry Pi Pico](https://tarikgit.github.io/coding/using-raspberry-pico): *The [Raspberry Pi Pico](https://www.raspberrypi.org/products/raspberry-pi-pico/) is a small, cheap and incredibly fast microcontroller board. The board is well-documented and extensions are cheap and simple to implement, as long as you have the right kit for your project*.
- [The Raspberry Pi GPIO pinout guide](https://pinout.xyz/)


### ... on a BBC micro:bit

[Using BBC micro:bit](https://tarikgit.github.io/coding/using-microbit.html): *The BBC micro:bit is microcontroller board is cheap and has many build-in sensors and LED's. Using the PIO the board can be easily extended*. This microcontroller can be turned into a robot by using the :Move mini and then be controlled using a [simple extension](https://makecode.microbit.org/pkg/kitronikltd/pxt-kitronik-servo-lite) to the MakeCode.


### Julia language

- [Julia](https://julialang.org/) is another language similar to Python, but much faster. Here are some [ressources](using-julia.html).


## Doing Maths on Raspberry Pi

[Using Mathematica on a RaspberryPi](https://tarikgit.github.io/coding/using-mathematica-on-raspberry.html): *The Wolfram Language has been around for decades and it offers great tools. Now you can use the [Wolfram language using Mathematica on your Raspberry](https://www.wolfram.com/raspberry-pi/) for free*.


## Advanced Maths in a Linux environment

### Dynamic Programming

- [Computational tools](https://tarikgit.github.io/coding/computational-tools.html): *Here are more advanced topics taken from dynamic programming (or optimal control theory), econometrics and statistics*
- [Value iteration in the gridworld](https://tarikgit.github.io/coding/valueiteration-gridworld.html): This page presents a simple example for value iteration in a 3-by-4 gridworld.

### Optimization

[A work-in-progess to model the decision-making of learners and teachers in the classroom.](https://tarikgit.github.io/coding/neos-server/neos-server.html)


### Great Tutorials From Others ...

- [QuantEcon](https://julia.quantecon.org/intro.html)
- [Computational Economics for PhDs](https://floswald.github.io/NumericalMethods/)

## Large-language model

### llama

- [Ollama — Get up and running with Llama 2 and other large language models locally.](https://github.com/jmorganca/ollama)
- [OllamaHub Discover, download, and explore Ollama Modelfiles](https://ollamahub.com/)
- [OllamaHub — Explore and Download Custom Ollama Modelfiles.](https://ollamahub.com/)
- [ollama library](https://ollama.ai/library)
- [Ollama Manual Install](https://github.com/jmorganca/ollama/blob/main/docs/linux.md)
- [Ollama Docker Image](https://hub.docker.com/r/ollama/ollama)
- [ollama-webui](https://github.com/ollama-webui/ollama-webui)
- [LlamaGPT](https://github.com/getumbrel/llama-gpt)
- [llama-gpt — A self-hosted, offline, ChatGPT-like chatbot. Powered by Llama 2. 100% private, with no data leaving your device. New: Code Llama support!](https://github.com/getumbrel/llama-gpt#benchmarks)
- [Uncensored AI on Linux (podcast)](https://linuxunplugged.com/540)

### quick start for ollama

To start the chat, type: <br>
```bash
ollama run llama2
```

Once youare in the chat, you can leave this mode by typing:
```bash
/bye
```

Remember that ollama is running in the backround as a server. If you want to disable it, type:
```bash
sudo systemctl stop ollama
```

If you want to relaunch the server, type: 
```bash
sudo systemctl start ollama
```

All the model files are stored in `/usr/share/ollama/.ollama/models/` . You should make a regular backup of this folder.

Use `ollama list` to list all the models installed on your system.




### coding assistants

- [Continue.dev — An open-source autopilot in your IDE](https://continue.dev/)
- [Refact is an open-source AI coding assistant with blazing-fast code completion, powerful code improvement tools, and chat.](https://refact.ai/)

## Deep learning models

- [Marker converts PDF, EPUB, and MOBI to markdown.](https://github.com/VikParuchuri/marker)


### speech note

- [Speech Note](https://flathub.org/apps/net.mkiol.SpeechNote)
- [Speech Note (Github)](https://github.com/mkiol/dsnote)
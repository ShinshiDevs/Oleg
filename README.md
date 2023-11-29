<p align="center">
  <h1 align="center" style="color: #FFCE4F"><img src="https://cdn.discordapp.com/avatars/1174060990111948854/87148b86800e9dca85d0740a938120f5.webp" width="30" style="border-radius: 100px"> Oleg</h1>
  <p align="center">Service bot for <a href="https://dsc.gg/shinshi">Shinshi Hub</a>, a support server. A bit similar to Shinshi, but much weaker in structure and content, but also serves as a good template for your future bot.<p>
  <p align="center">
    <a href="https://github.com/ShinshiDevs/Oleg/blob/main/LICENSE.txt">
      <img src="https://img.shields.io/badge/MIT%20License-yellow.svg" />
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/Python%203.11.6-yellow.svg" />
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/codestyle%20black-black.svg" />
    </a>
    <a href="https://discord.gg/3bXW7an2ke">
	<img src="https://img.shields.io/discord/1130589089658306672.svg">
    </a>
  </p>
</p>

### References
- [Changelog](CHANGELOG.md)
- [Support](https://dsc.gg/shinshi)

### Contribution
Any contributors are welcome, but please respect these rules:
- Clear commit messages.
- Refactor the code before publishing. 
`poetry init --dev-dependency` to install development packages, like: `black`.
- In the commit description, state as much as possible so we understand what you want to do.

Good luck! 🤝

### `Docker` In order to run the bot you need to
- Put all the necessary data in your `.env` file.
- Run the bot with either `docker compose up -d --build` or `docker run -it $(docker build -q .)`.

### `poetry` In order to run the bot you need to
- Install Python (recommend [3.11](https://www.python.org/downloads/release/python-3116/))
- Install poetry. [Instructions](https://python-poetry.org/docs/#installing-with-the-official-installer)
- Go to the project directory and type `poetry init`. 
- Run the bot with `poetry run python3 -OO -m oleg`

This way is not recommended.
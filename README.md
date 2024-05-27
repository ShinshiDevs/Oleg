<p align="center">
  <h1 align="center"><img src="assets/logo.svg" width="30"> Oleg</h1>
  <p align="center">Service bot for <a href="https://dsc.gg/shinshi">Shinshi Hub</a>, a support server. A bit similar to Shinshi, but much weaker in structure and content, but also serves as a good template for your future bot.<p>
  <p align="center">
    <a href="https://github.com/ShinshiDevs/Oleg/blob/main/LICENSE">
      <img src="https://img.shields.io/badge/MIT%20License-white.svg" />
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/Python%203.12-white.svg" />
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/ruff-white.svg" />
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
- Refactor the code before publishing with ruff.
  
  `poetry init --dev-dependency` to install development packages.
- In the commit description, state as much as possible, so we understand what you want to do.

Good luck! 🤝

### `Docker` In order to run the bot you need to
- Put all the necessary data in your `.env` file.
- Run the bot with `docker run -it $(docker build -q .)`.

### `poetry` In order to run the bot you need to
- Install Python (recommend [3.11](https://www.python.org/downloads/release/python-3116/))
- Install poetry. [Instructions](https://python-poetry.org/docs/#installing-with-the-official-installer)
- Go to the project directory and type `poetry init`. 
- Run the bot with `poetry run python3 -OO -m oleg`

> [!WARNING]  
> This way is not recommended.
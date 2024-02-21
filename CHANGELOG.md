# Version 0.1.3

+ Docker Compose was deleted and the main startup file was redone. **`BREAKING CHANGE`**

  Before that, Oleg did not want to run without Compose, and it was not entirely clear the problem,
  but the main file was redone and now it runs correctly without problems. And also the Dockerfile
  and startup logic has been completely redesigned, or rather, taken from Shinshi Avela ;)
+ Folder structure.

  Before that, it was a very strange decision to have data in the module, but now everything is
  fine.
+ python-dotenv has been removed and replaced with its own loader from Shinshi Avela.
+ ruff
+ README update (lmao)
+ `example.env` -> `.env.example`
+ `LICENSE.txt` -> `LICENSE`

# Version 0.1.2
+ Bot has been rewritten to a very similar base and structure as Shinshi, but without Dependency Injection due to complex implementation, so far.
+ Simplified getting and caching the right stuff, like language roles, channels and emoji to avoid using constats...
+ `about` slash command has been added.
+ Updated bot's design to Shinshi's new design. (really smart)

# Version 0.1.1
+ Absolute imports.
+ Environment variables example.
+ Add a LICENSE file and append license to each file, CHANGELOG and README.
+ Optimization.
+ 🎄 Add a task that changes the count of days until the new year! 
> so don't judge me harshly, especially CHANGELOG. (@stefanlight8)

# Version 0.1.0
There is no changelog, because this is first version.
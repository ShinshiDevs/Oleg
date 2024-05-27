import os
import re

DOTENV_REGEX = re.compile(r"^([A-Za-z_]+\w*)=([^#]+)(#.*)?$")


def load_dotenv(file_path: os.PathLike[str] | str = ".env") -> None:
    with open(file_path, "r", encoding="UTF-8") as file:
        for line in file:
            if match := DOTENV_REGEX.match(line):
                os.environ[match.group(1)] = match.group(2).strip().replace('"', "")

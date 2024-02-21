# Copyright (c) 2023-Present Shinshi Developers Team
# Apache-2.0 License from Shinshi Avela.
def parse_dotenv_file(file_path: str) -> dict:
    env_variables = {}
    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                key, value = line.split("=", 1)
                env_variables[key.strip()] = value.strip()
        return env_variables
    except Exception as exception:
        print(f"Error parsing .env file: {exception}")
        return {}

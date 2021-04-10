import os
from pathlib import Path

block_set_surge = ""
block_set_AGH = ""

if __name__ == '__main__':
    with open("block_set", "r") as f1:
        for line in f1.readlines():
            if line.startswith("#"):
                continue

            block_set_surge += f".{line}"

            block_set_AGH += f"||{line.strip()}^\n"

    # Surge rule set
    if not os.path.exists("block_set_surge"):
        Path("block_set_surge").touch()

    with open("block_set_surge", "w") as f1:
        f1.write(block_set_surge)

    # AdGuard Home
    if not os.path.exists("block_set_AGH"):
        Path("block_set_AGH").touch()

    with open("block_set_AGH", "w") as f1:
        f1.write(block_set_AGH)

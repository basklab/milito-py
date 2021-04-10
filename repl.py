import json
import os

import yaml

from decks.AncientBritish import ancient_british
from decks.common import CONFIG_PATH
from shared.dtos import DTO


def to_json(item, depth=None):
    if isinstance(item, DTO):
        return dict((k, to_json(v, depth)) for k, v in item.__dict__.items())
    elif isinstance(item, list):
        tmp = item[:depth] if depth is not None else item
        return [to_json(x, depth) for x in tmp]
    else:
        return item


def main():
    tmp = os.path.join(CONFIG_PATH, "decks", "AncientBritish.yaml")
    with open(tmp, 'r') as stream:
        print(yaml.safe_load(stream))


def main2():
    deck = ancient_british()

    dto = deck.to_dto()

    print(dto)

    print(json.dumps(to_json(dto, 3), indent=4))


if __name__ == "__main__":
    main()

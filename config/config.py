import sys
from pathlib import Path

import yaml

from clients.base import get_client_from_input

HERE = Path(__file__).parent
CONF_PATH: Path = HERE / "conf.yaml"


if CONF_PATH.is_file():
    with open(CONF_PATH, "r") as f:
        config = yaml.safe_load(f)

    try:
        # LLM
        key = config["llm_api"]["key"]
        model_family = config["llm_api"]["model_family"]
        client_type = get_client_from_input(model_family.lower())
        model_name = config["llm_api"]["model_name"]

    except KeyError as e:
        sys.exit(f"The parameter '{e}' was not found. Please check {CONF_PATH}.")

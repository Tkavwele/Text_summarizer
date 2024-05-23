import os
import yaml
from src.textSummarizer.logging import logger
from pathlib import Path
from typing import Any



def read_yaml_file(path_to_yaml: Path) -> dict:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

 
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return yaml.safe_load(yaml_file)    
    except Exception as e:
        raise e

def create_directories(path_to_dirs: list, verbose=True):
    """create list of directories

    Args:
        path_to_dirs (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")



def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

    

import os
from pathlib import Path
import logging
from time import asctime


logging.basicConfig(level=logging.INFO, format='[%(asctime)s: %(asctime)s]')

project_name = "coccidiosis-chicken-detection-cnn "

list_of_files = (

    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/coponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/confugration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "reasearch/trials.ipynb"



)

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)



    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating direcrtory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty fie¥le :{filepath}")


    else:
        logging.info(f"{filename} is already exist")
         

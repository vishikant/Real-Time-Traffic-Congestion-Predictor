# real_time_traffic_predictor/
# │
# ├── data/
# │   ├── historical/
# │   └── live/
# │
# ├── notebooks/
# ├── src/
# │   ├── data_collection.py
# │   ├── model_training.py
# │   ├── prediction.py
# │   └── dashboard.py
# │
# ├── model/
# │   └── lstm_traffic_model.h5
# │
# ├── streamlit_app.py
# └── requirements.txt



import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "Real_Time_Traffic_Congestion"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/data/live",
    f"src/{project_name}/data/historical",
    f"src/{project_name}/data_collection.py",
    f"src/{project_name}/model_training.py",
    f"src/{project_name}/prediction.py",
    f"src/{project_name}/dashboard.py",
    f"src/{project_name}/model/lstm_traffic_model.h5",
    "streamlit_app.py",
    "requirements.txt",



]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")
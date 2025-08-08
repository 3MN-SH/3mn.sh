import os
import re
import yaml
from dotenv import load_dotenv

load_dotenv()

ABS_IMPORT_DIR = os.getenv("BASE_DIR") + "/scripts/import/"
ABS_DATA_FILE = os.getenv("BASE_DIR") + "_data/portfolio.yml"
REL_IMAGE_DIR = "/assets/images/portfolio/"
ABS_IMAGE_DIR = os.getenv("BASE_DIR") + REL_IMAGE_DIR

pattern = r"(\d{4}-\d{2}-\d{2}) - (.+)"

for filename in os.listdir(ABS_IMPORT_DIR):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        if re.search(pattern, filename):
            date = re.findall(pattern, filename)[0][0]
            caption = re.findall(pattern, filename)[0][1]

            with open(ABS_DATA_FILE, "r") as j:
                data = yaml.load(j, yaml.FullLoader)
                data.append({'path': f'{REL_IMAGE_DIR}{filename}',
                            'caption': f'{caption}', 
                            'date': f'{date}'})
                
                with open(ABS_DATA_FILE, "w") as f:
                    yaml.dump(data, f, default_flow_style=False, sort_keys=False)
                    
            os.rename(ABS_IMPORT_DIR + "/" + filename, ABS_IMAGE_DIR + "/" + filename)
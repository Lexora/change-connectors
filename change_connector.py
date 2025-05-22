import requests
import time
import toml
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
secrets_path = BASE_DIR / "creds.toml"
secrets = toml.load(secrets_path)

# api_key = secrets["api_keys"]["api_key"]
# api_secret = secrets["api_keys"]["api_secret"]
b64_api_key_secret = secrets["api_keys"]["b64_api_key"]
BASE_URL = "https://api.fivetran.com/v1"
HEADERS = {"Authorization": f"Basic {b64_api_key_secret}"}

# *Step 1: Get all connectors*
response = requests.get(f"{BASE_URL}/connectors", headers=HEADERS)
connectors = response.json().get("data", [])

# *Step 2 & 3: Update each connector's schema setting*
connectors = [x for x in  connectors["items"] if "shopify" in x['service']]
# n = [x for x in  connectors["items"] if "shopify" in x['service']]

for connector in connectors:
    connector_id = connector["id"]
    patch_url = f"{BASE_URL}/connectors/{connector_id}/schemas"
    payload = {"schema_change_handling": "ALLOW_COLUMNS"}
    time.sleep(0.5)
    update_response = requests.patch(patch_url, headers=HEADERS, json=payload)    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")    
    if update_response.status_code == 200:
        print(f"[{timestamp}] Successfully updated connector {connector_id}")
    else:
        print(f"[{timestamp}] Failed to update connector {connector_id}", update_response.json())
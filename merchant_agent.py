import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

GUMROAD_TOKEN = os.getenv("GUMROAD_ACCESS_TOKEN")
API_URL = "https://api.gumroad.com/v2/products"

HEADERS = {
    "Authorization": f"Bearer {GUMROAD_TOKEN}"
}

def create_product(meta, folder_path):
    payload = {
        "name": meta["title"],
        "price": int(meta["price"]) * 100,
        "description": meta["description"],
        "custom_receipt": meta.get("receipt_message", ""),
        "tags": ",".join(meta.get("tags", [])),
        "is_recurring_billing": False
    }

    print("Creating product:", meta["title"])
    resp = requests.post(API_URL, data=payload, headers=HEADERS)
    product = resp.json()
    product_id = product["product"]["id"]

    upload_files(product_id, folder_path)
    return product_id

def upload_files(product_id, folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            continue
        file_path = os.path.join(folder_path, filename)
        print(f"Uploading: {filename}")
        files = {"file": open(file_path, "rb")}
        url = f"{API_URL}/{product_id}/files"
        requests.post(url, headers=HEADERS, files=files)

def load_metadata(folder_path):
    with open(os.path.join(folder_path, "metadata.json")) as f:
        return json.load(f)

if __name__ == "__main__":
    BASE_FOLDER = "products"
    for folder in os.listdir(BASE_FOLDER):
        path = os.path.join(BASE_FOLDER, folder)
        if os.path.isdir(path):
            meta = load_metadata(path)
            create_product(meta, path)

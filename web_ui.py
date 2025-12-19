from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import HTMLResponse
import uvicorn
import os
import json
from merchant_agent import create_product

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def form():
    return """
    <html>
        <body>
            <h2>Create a Gumroad Product</h2>
            <form action="/submit" enctype="multipart/form-data" method="post">
                Title: <input type="text" name="title"><br>
                Price (USD): <input type="number" name="price"><br>
                Tags (comma-separated): <input type="text" name="tags"><br>
                Description: <textarea name="description"></textarea><br>
                Receipt message: <textarea name="receipt_message"></textarea><br>
                <input type="submit" value="Create Product">
            </form>
        </body>
    </html>
    """

@app.post("/submit")
async def submit(
    title: str = Form(...),
    price: int = Form(...),
    tags: str = Form(...),
    description: str = Form(...),
    receipt_message: str = Form(...)
):
    meta = {
        "title": title,
        "price": price,
        "tags": tags.split(","),
        "description": description,
        "receipt_message": receipt_message
    }
    product_id = create_product(meta, folder_path="products/sample_product")
    return {"status": "created", "product_id": product_id}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

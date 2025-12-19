# MERCHANT Agent - Gumroad Product Builder

## What It Does
Automatically creates and uploads digital product listings to your Gumroad account using a local folder of assets.

## Setup
1. Create a `.env` file from `.env.example` and insert your Gumroad access token.
2. Organize your products like this:

```
products/
  resin_rescue/
    metadata.json
    Resin_Rescue_Guide.pdf
    Support_Cheat_Sheet.png
    bonus.zip
```

3. Run:
```bash
python merchant_agent.py
```

## Metadata File Format
```json
{
  "title": "Resin Rescue Blueprint",
  "price": 47,
  "description": "Fix failed 3D prints with this blueprint...",
  "tags": ["3d printing", "resin"],
  "receipt_message": "Thanks for purchasing — your guide is on the way!"
}
```

---

## 🚀 Render 1-Click Deploy

Click below to instantly deploy this agent to Render:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/YOUR_USERNAME/merchant-agent)

**Setup Instructions:**
- Add your `GUMROAD_ACCESS_TOKEN` and `OPENAI_API_KEY` as environment variables after deploy
- Start your agent via the built-in web form at `/`


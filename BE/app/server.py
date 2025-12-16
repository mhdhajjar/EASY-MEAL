from fastapi import FastAPI, UploadFile, File
from fastapi.responses import RedirectResponse
from langserve import add_routes
import base64 

from app.chain import chain

app = FastAPI(title="EASY MEAL API")


@app.get("/")
async def redirect_root_to_docs() -> RedirectResponse:
    return RedirectResponse("/docs")

# ---------- Image upload endpoint ----------

@app.post("/EASY MEAL")
async def analyze_fridge(image: UploadFile = File(...)):
    image_bytes = await image.read()
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    result = chain.invoke({
        "image_base64": image_base64
    })

    return result.model_dump()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    text: str


@app.post("/predict/")
def predict(item: Item):
    """
    Function for a POST request to /predict/
    Args:
        item (Item): Text for sentiment analysis.
    Returns:
        dict: Dictionary with predicted mood of the text.
    """
    return {"mood": "happy"}


@app.get("/model_info/")
def model_info():
    """
    Function for a GET request to /model_info/
    Returns:
        dict: Dictionary with information about the model.
    """
    return {"model": "Sentiment Analysis Model", "version": "1.0"}

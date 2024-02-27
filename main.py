from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from train import spam_detection
import uvicorn

# Create a FastAPI app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create a Pydantic model for the request payload
class TextRequest(BaseModel):
    text: str

# Define a route for spam detection API
@app.post('/detect_spam')
def detect_spam(request: TextRequest):
    print("inside the api")
    # Get the input text from the request
    input_text = request.text
    model=spam_detection()
    # Make a prediction using the trained model
    prediction = model.predict([input_text])[0]

    # Return the result as JSON
    result = {'is_spam': bool(prediction), 'confidence': float(model.predict_proba([input_text])[0][1])}
    return result

if __name__ == '__main__':
    # Run the FastAPI app using Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

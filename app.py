import fastapi
from contextlib import asynccontextmanager
from pydantic import BaseModel, Field
from sklearn.linear_model import LogisticRegression
import os


class PredictRequest(BaseModel):
    cecha1: float = Field(..., ge=0.0, le=1.0)
    cecha2: float = Field(..., ge=0.0, le=1.0)


class PredictResponse(BaseModel):
    prediction: int
    probability: float

@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    X = [
        [0.1, 0.2],
        [0.2, 0.1],
        [0.8, 0.9],
        [0.9, 0.8],
        [0.15, 0.25],
        [0.85, 0.75],
    ]
    y = [0, 0, 1, 1, 0, 1]

    model = LogisticRegression()
    model.fit(X, y)
    app.state.model = model
    yield
app = fastapi.FastAPI(lifespan=lifespan)

@app.get('/')
def home():
    return {'message': 'Hello World'}


@app.post(
    '/predict',
    response_model=PredictResponse,
)
def predict(payload: PredictRequest):
    features = [payload.cecha1, payload.cecha2]
    prediction = int(app.state.model.predict([features])[0])
    probability = float(app.state.model.predict_proba([features])[0][prediction])
    return PredictResponse(prediction=prediction, probability=probability)

@app.get('/info')
def info():
    model = app.state.model
    model_name = os.getenv("MODEL_NAME", "default")
    return {
        'model_type': type(model).__name__,
        'n_features': model.n_features_in_,
        'classes': model.classes_.tolist(),
        'model_name': model_name,
    }

@app.get('/health')
def health():
    return {'status': 'ok'}

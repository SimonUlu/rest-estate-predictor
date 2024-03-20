# rest-estate-predictor
Fast-Api Project to predict values of german real-estate

## Dev - folder
Jupyter notebooks and logic to create estate-predictor model

## App - folder
Rest api with middleware to get predictions

## Get Started - Locally

activate virtual environment:
source venv/bin/activate   

install all requiremenents listed in req.txt
pip install -r requirements.txt

start local dev server
python -m uvicorn app.main:app --reload

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

## Usage

### Dev - Folder 

#### Create Model Notebooks

These notebooks contain the code on how to create a new model for each estate type (e.g. apartment & house) 
Code also creates all json-files for folder *fields* that are needed to prepare the data for the actual prediction in the main app folder
As of right now (to be updated) all files need to be copied into the respective folders *estate_fields* in app-folder

#### Fields

As stated before only the fields needed in prediction for the respective models (e.g. prediction for houses and apartments)

### Main APP - Folder

#### API

##### Predicitions

Code to predict the value of estate which is send via http request
folder functionality has the logic to prepare the data to rigth format

##### Endpoints 

Api endpoint (maybe to be implemented with UI) for creating api-users that get saved into db-table "api_users"

##### ML-Models

Folder that contains the xgb models that were created within dev folder

#### Other stuff

##### main.py
initialisation of different api-endpoints (within fast-api framework is the first file that gets executed)

##### others
dependency stuff for using database connection that is set within the .env file



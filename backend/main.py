from fastapi import FastAPI, HTTPException, Query
app = FastAPI()
def calculate_status(counts, minimum):

    if counts >= minimum:
        return "Confirmed"
    else:
        return "Pending"
def calculate_missing(counts, minimum):

    if counts >= minimum:
        return 0
    else:
        return minimum - counts
    

@app.get("/")
def home():
    return {"message": "Bienvenido a CruiseOpsAI 🚢"}
@app.get("/coordinator")
def coordinator():
    return {
        "name": "Roberto",
        "position": "Cruise Coordinator",
        "countries": [
            "Italy",
            "France"
        ]
    }
@app.get("/ship")
def ship():
    return {
        "name": "Norwegian Epic",
        "capacity": 4200,
        "country": "Bahamas"
    }
@app.get("/health")
def health():
    return {
        "status": "OK",
        "application": "CruiseOpsAI"
    }
@app.get("/status")
def status(
    counts: int = Query(ge=0),
    minimum: int = Query(gt=0)
):
    

    if counts >= minimum:
        return {
            "status": "Confirmed",
            "counts": counts,
            "minimum": minimum,
            "missing": 0
        }

    return {
        "status": "Pending",
        "counts": counts,
        "minimum": minimum,
        "missing": minimum-counts
    }
operations = {
    1: {
        "ship": "Norwegian Epic",
        "port": "Livorno",
        "date": "2026-09-15",
        "counts": 18,
        "minimum": 25,
        "maximum": 45,
        "code": "Y6N0"
    },
    2: {
        "ship": "Norwegian Viva",
        "port": "Naples",
        "date": "2026-09-18",
        "counts": 30,
        "minimum": 25,
        "maximum": 45,
        "code": "V2A1"
    }
}


@app.get("/operation/{operation_id}")
def operation(operation_id: int):
    if operation_id not in operations:
        raise HTTPException(
            status_code=404,
            detail=f"Operation {operation_id} not found"
        )

    operation_data = operations[operation_id]

    counts = operation_data["counts"]
    minimum = operation_data["minimum"]
    maximum = operation_data["maximum"]

    if (
        counts < 0
        or minimum <= 0
        or maximum < minimum
        or counts > maximum
    ):
        raise HTTPException(
            status_code=500,
            detail=f"Invalid configuration for operation {operation_id}"
        )

    status = calculate_status(counts, minimum)
    missing = calculate_missing(counts, minimum)

    return {
        **operation_data,
        "status": status,
        "missing": missing
    }

   
    

   
from datetime import date

navigation_date = date(2026, 9, 15)
today = date.today()

days_to_navigation = (navigation_date - today).days


    
   
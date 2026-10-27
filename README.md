CruiseOpsAI

A Python REST API for managing sample cruise excursion operations.

Overview

CruiseOpsAI is a portfolio project developed to practice backend development using Python and FastAPI.

The API evaluates passenger counts against minimum excursion requirements and returns operational statuses.

Features

REST API built with FastAPI.

Sample cruise excursion records.

Excursion status calculation: Confirmed or Pending.

Passenger count validation.

HTTP error handling for nonexistent operations.

Automated tests using pytest.

Technologies

Python

FastAPI

Uvicorn

pytest

Git

API Endpoints

Method

Endpoint

Description

GET

/

Welcome message

GET

/coordinator

Sample coordinator information

GET

/ship

Sample ship information

GET

/health

Application health check

GET

/status?counts=18&minimum=25

Evaluates passenger counts

GET

/operation/1

Retrieves a sample excursion

GET

/operation/2

Retrieves another sample excursion

Getting Started

Requirements

Python 3.13 or a compatible version

pip

Install Dependencies

From the project root, activate the virtual environment:

.\.venv\Scripts\Activate.ps1

Install the required packages:

python -m pip install fastapi uvicorn pytest

Run the API

Navigate to the backend directory:

cd backend
python -m uvicorn main:app --reload

The API will be available at http://127.0.0.1:8000.

Interactive API documentation: http://127.0.0.1:8000/docs.

Run Tests

From the backend directory:

python -m pytest tests/test_main.py -v

The current test suite contains eight automated tests covering API responses, validation, and error handling.

Example

Request:

GET /status?counts=18&minimum=25

Example response:

{
  "status": "Pending",
  "counts": 18,
  "minimum": 25,
  "missing": 7
}

An excursion is marked Confirmed when passenger counts meet or exceed the minimum. Otherwise, its status is Pending.

Project Scope

This version uses sample data defined in the application code. It does not yet integrate with production databases, external cruise line systems, or live booking platforms.

Learning Objectives

Python backend development

REST API design

Query parameter validation

HTTP error handling

Automated testing with pytest

Version control with Git

Version

Version: 1.0.0

Status: Initial portfolio release.
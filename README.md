# demoapi-teams-agents

A basic UV project using FastAPI to expose an API method that lists example organisms.

## Features

- FastAPI-based REST API
- GET endpoint `/organisms` that returns a list of example organisms
- Automatic API documentation at `/docs`

## Requirements

- Python 3.12 or higher
- UV package manager

## Installation

1. Install UV if you haven't already:
```bash
pip install uv
```

2. Install dependencies:
```bash
uv sync
```

## Running the API

Start the FastAPI server:
```bash
uv run uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /organisms` - Returns a JSON list of example organisms
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation (ReDoc)

## Example Usage

```bash
curl http://localhost:8000/organisms
```

Response:
```json
{
  "organisms": [
    "Escherichia coli",
    "Saccharomyces cerevisiae",
    "Drosophila melanogaster",
    "Caenorhabditis elegans",
    "Mus musculus",
    "Homo sapiens"
  ]
}
```
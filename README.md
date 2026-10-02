# 🧮 Calculator FastAPI

A simple full-stack calculator built with **FastAPI** and **HTML, CSS, JavaScript**. The frontend sends calculations to a FastAPI backend as JSON and displays the result.

## Features

- Addition, subtraction, multiplication, division
- Decimal support, delete and clear buttons
- REST API with JSON requests and responses
- Division-by-zero error handling
- Auto-generated API docs (Swagger UI)

## Tech Stack

- **Backend:** Python, FastAPI, Uvicorn, Pydantic
- **Frontend:** HTML, CSS, JavaScript
- **Testing:** Postman

## Project Structure

```text
Calculator-Fastapi/
├── calculator.py   # FastAPI backend
├── index.html      # Frontend
├── .gitignore
└── README.md
```

## Installation

```bash
git clone https://github.com/shalahthaikkadan/Calculator-Fastapi.git
cd Calculator-Fastapi
python -m venv fastapi
fastapi\Scripts\activate        # Windows
pip install fastapi uvicorn
```

## Run

```bash
python -m uvicorn calculator:app --reload
```

- App: http://127.0.0.1:8000
- API docs: http://127.0.0.1:8000/docs

## API

### `POST /calculate`

Request:

```json
{ "x": 20, "y": 10, "opr": "+" }
```

Response:

```json
{ "result": 30 }
```

Supported operators: `+`, `-`, `*`, `/`

Error example (division by zero):

```json
{ "error": "Cannot divide by zero" }
```

## Future Improvements

- [ ] Calculation history
- [ ] Keyboard support
- [ ] Scientific functions
- [ ] Automated tests
- [ ] Deployment

## License

Created for learning and educational purposes.

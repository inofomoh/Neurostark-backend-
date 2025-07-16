
# Neurostark Film Backend

## Setup

```bash
pip install -r requirements.txt
python app.py
```

## API Endpoint

- POST `/generate`: Upload image + script + genre → returns video link
- GET `/download/<uid>`: Download generated film

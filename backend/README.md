# Simple Venmo

## How to run

You will need Poetry to run this app.

First, `cd` into `backend` and run `poetry shell` and `poetry install`

Then run `poetry run fastapi dev backend/main.py`. The backend should now be running!

Next in another terminal, `cd` into `frontend` and run `npm install`.

Lastly, run `npm run build` and then `npm start`, and the frontend should now be running at `http://localhost:3000`.

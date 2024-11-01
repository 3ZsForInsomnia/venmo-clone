# Simple Venmo

## How to run

You will need Poetry to run this app.

First, `cd` into `backend` and run `poetry shell` and `poetry install`

Then run `poetry run fastapi dev backend/main.py`. The backend should now be running!

Next in another terminal, `cd` into `frontend` and run `npm install`.

Lastly, run `npm run build` and then `npm start`, and the frontend should now be running at `http://localhost:3000`.

## What was not completed

The frontend is largely not complete due to time budgeting.

I mostly wanted to focus on the backend, which is mostly complete to allow a user to sign in or sign up, create new accounts, and create transactions.

The frontend is mostly just a login page, and a page to create a new account, but shows the main ideas of how I would organize and implement the rest. Namely, it is a NextJS application using HTTP services exposed through hooks. It also uses ShadCN and Tailwind for styling, as those are fantastic tools for modern professional UI development, as both are modern and support SSR + Server Components automatically.

Making such a small app actually use Server Components would be overkill, however NextJS still offers a nice, batteries included setup to develop within. Further, Server Components and SSR are great tools to make available in any modern React project.

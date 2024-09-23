from fastapi import FastAPI

app = FastAPI()


@app.get("/users/current")
async def root():
    return {"message": "Hello World!!!"}


@app.get("/users/{user_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/transactions/")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/transactions/{transaction_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/transaction_requests")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/transaction_requests/{transaction_request_id}")
async def read_item(item_id):
    return {"item_id": item_id}

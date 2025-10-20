from fastapi import FastAPI
from storage.router import router as storage_router

app = FastAPI(title="Azure Blob Storage API")


app.include_router(storage_router)




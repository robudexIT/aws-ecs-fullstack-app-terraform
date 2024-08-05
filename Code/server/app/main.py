from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import login, call_summary, call_details, metris,agents,cdrs, search_number, counts, tag


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins
    allow_credentials=True,
    allow_methods=["POST", "GET", "OPTIONS", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)

app.include_router(login.router)
app.include_router(call_summary.router)
app.include_router(call_details.router)
app.include_router(metris.router)
app.include_router(agents.router)
app.include_router(cdrs.router)
app.include_router(search_number.router)
app.include_router(counts.router)
app.include_router(tag.router)
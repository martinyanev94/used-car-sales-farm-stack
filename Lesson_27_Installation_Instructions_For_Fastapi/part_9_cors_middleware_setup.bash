pip install starlette
from starlette.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify the origins that are allowed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, or specify your domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

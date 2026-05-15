from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="LuminaOS API",
    description="Enterprise AI Meeting Intelligence Operating System",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "LuminaOS API"}

@app.websocket("/ws/stream/{meeting_id}")
async def websocket_endpoint(websocket: WebSocket, meeting_id: str):
    await websocket.accept()
    logger.info(f"WebSocket connected for meeting: {meeting_id}")
    try:
        while True:
            # Receive audio chunks from client
            data = await websocket.receive_bytes()
            # Push to Kafka or Redis Streams for processing
            # ... audio processing pipeline ...
            
            # Simulated response
            await websocket.send_json({"type": "status", "message": "Audio chunk received"})
    except WebSocketDisconnect:
        logger.info(f"WebSocket disconnected for meeting: {meeting_id}")

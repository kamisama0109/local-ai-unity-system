# Setup Guide - Local AI Unity System

## Prerequisites
- Python 3.8+
- Docker & Docker Compose
- Unity 2020.3 LTS or later
- GPU (NVIDIA CUDA 11.4+) - for Qwen LLM

## Backend Setup

### 1. Clone the Repository
```bash
git clone https://github.com/kamisama0109/local-ai-unity-system.git
cd local-ai-unity-system
```

### 2. Install Python Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 3. Run the FastAPI Server
```bash
python app.py
# Server starts at http://localhost:8000
```

## Docker Setup

### 1. Start Containers with Docker Compose
```bash
docker-compose up -d
```

This will start:
- **Qwen LLM** on port 8000 (GPU)
- **Phi-3 LLM** on port 8001 (CPU)

### 2. Verify Containers
```bash
docker-compose ps
```

### 3. Stop Containers
```bash
docker-compose down
```

## Unity Setup

### 1. Open Project in Unity
- Launch Unity Hub
- Click "Add" and select the project folder
- Open the project

### 2. Configure WebSocket Settings
- Navigate to `Assets/Settings/Config.json`
- Set the server URL: `ws://localhost:8000/ws`

### 3. Build for Mobile (Android/iOS)
```
File > Build Settings > Select Platform > Build
```

## Testing

### 1. Test WebSocket Connection
```bash
cd backend
python -m pytest tests/test_websocket.py
```

### 2. Test LLM Inference
```bash
python -m pytest tests/test_llm.py
```

## Troubleshooting

### Port Already in Use
```bash
# Find and kill process on port 8000
lsof -i :8000
kill -9 <PID>
```

### GPU Memory Issues
- Reduce batch size in `backend/config.json`
- Use CPU version (Phi-3) instead

### WebSocket Connection Failed
- Check if backend is running: `curl http://localhost:8000`
- Verify firewall settings
- Check network connectivity

## Next Steps
1. Review [ARCHITECTURE.md](../docs/ARCHITECTURE.md) for system design
2. Check [COMMUNICATION_FLOW.md](../docs/COMMUNICATION_FLOW.md) for API details
3. Start integrating with your Unity game
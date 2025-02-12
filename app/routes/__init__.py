import importlib
from fastapi import APIRouter
from pathlib import Path

mainRouter = APIRouter()

# Get all Python files inside the `routes` directory (excluding __init__.py)
for file in Path(__file__).parent.glob("*.py"):
    if file.stem != "__init__":  # Skip __init__.py
        module = importlib.import_module(f"{__name__}.{file.stem}")
        if hasattr(module, "router"):
            mainRouter.include_router(module.router)

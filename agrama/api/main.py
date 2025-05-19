"""
Agrama API - FastAPI application for Agrama
"""

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from agrama.api.routers import nodes, edges, search, summarise
from agrama.api.routers import mcp

# Create the FastAPI application
app = FastAPI(
    title="Agrama API",
    description="API for Agrama - A local micro-stack for knowledge "
    "management and retrieval",
    version="0.1.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create the main router
router = APIRouter()


@router.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to Agrama API"}


@router.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "ok"}


# Include the router in the application
app.include_router(router)

# Include other routers
app.include_router(nodes.router, prefix="/nodes", tags=["nodes"])
app.include_router(edges.router, prefix="/edges", tags=["edges"])
app.include_router(search.router, tags=["search"])
app.include_router(summarise.router, prefix="/summarise", tags=["summarise"])

# Include MCP router
app.include_router(mcp.router, prefix="/v1", tags=["mcp"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

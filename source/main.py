import uvicorn
import typer

from source.api.routes import app
from source.cli.commands import cli
from source.config import API_HOST, API_PORT

def start_api(host: str = API_HOST, port: int = API_PORT):
    """Start the FastAPI server"""
    uvicorn.run(app, host=host, port=port)

if __name__ == "__main__":
    # Add the API server command to the CLI
    cli.command(name="serve")(start_api)
    
    # Run the CLI
    cli()
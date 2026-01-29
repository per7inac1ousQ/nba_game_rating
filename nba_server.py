"""
Simple NBA MCP Server - Provides comprehensive NBA stats for games and players.
"""
import os
import sys
import logging
import random

# Configure logging to stderr
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', stream=sys.stderr)
logger = logging.getLogger(__name__)

mcp = FastMCP(
    name="NBA Stats Server",
    version="1.0",
    description="Provides comprehensive NBA stats for games and players.",
    author="Peter Andre",
)


@mcp.command("get_game_stats", "Get stats for a specific NBA game by game ID.")
def get_game_stats(game_id: str) -> dict:
    logger.info(f"Fetching stats for game ID: {game_id}")
    # Simulate fetching game stats
    game_stats = {
        "game_id": game_id,
        "teams": {
            "home": "Los Angeles Lakers",
            "away": "Boston Celtics"
        },
        "score": {
            "home": random.randint(80, 130),
            "away": random.randint(80, 130)
        },
        "top_performers": [
            {"player": "LeBron James", "points": random.randint(20, 40)},
            {"player": "Jayson Tatum", "points": random.randint(20, 40)}
        ]
    }
    return game_stats
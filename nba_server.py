"""
Simple NBA MCP Server - Provides comprehensive NBA stats for games and players.
"""
import os
import sys
import logging
import random
from fastmcp import FastMCP

# Configure logging to stderr
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', stream=sys.stderr)
logger = logging.getLogger(__name__)

mcp = FastMCP(
    name="NBA Stats Server",
    version="1.0",
)


@mcp.tool(name="get_game_stats", description="Get stats for a specific NBA game by game ID.")
async def get_game_stats(game_id: str) -> dict:
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


@mcp.tool(name="get_player_stats", description="Get stats for a specific NBA player by player ID.")
async def get_player_stats(player_id: str) -> dict:
    logger.info(f"Fetching stats for player ID: {player_id}")
    # Simulate fetching player stats
    player_stats = {
        "player_id": player_id,
        "name": "LeBron James",
        "position": "Forward",
        "team": "Los Angeles Lakers",
        "stats": {
            "points_per_game": random.randint(15, 35),
            "assists_per_game": random.randint(5, 15),
            "rebounds_per_game": random.randint(8, 18)
        }
    }
    return player_stats

if __name__ == "__main__":
    logger.info("Starting NBA Stats Server...")
    # mcp.run(transport="http", host="127.0.0.1", port=8000, path="/mcp")
    mcp.run(transport="stdio")
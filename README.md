# NBA GAME RATING

An application that reviews NBA games and rates them using a Model Context Protocol (MCP) server that provides comprehensive NBA stats functionality.

## Purpose

This MCP server provides a secure interface for AI assistants to perform various NBA stats calculation operations.

## Features

### Current Implementation
- **`get_game_stats`** - Get stats for a specific NBA game by game ID
- **`get_player_stats"`** - Get stats for a specific NBA player by player ID


## Prerequisites

- Docker Desktop with MCP Toolkit enabled
- Docker MCP CLI plugin (`docker mcp` command)

## Installation

See the step-by-step instructions provided with the files.

## Usage Examples

In Claude Desktop, you can ask:
- "Get stats for the game between Warriors and Raptors yesterday"
- "Get stats for Lebron James"

## Architecture
Claude Desktop / Agent → MCP Gateway → Dice MCP Server
↓
Random Generation
Engine

## Development


### Local Testing 

```bash
# Run server locally
python nba_server.py

# Test MCP protocol
echo '{"jsonrpc":"2.0","method":"tools/list","id":1}' | python nba_server.py

```

### Testing 
Test your server is up and running
`docker mcp server list`

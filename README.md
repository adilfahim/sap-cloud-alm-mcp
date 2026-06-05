# sap-cloud-alm-mcp
SAP Cloud ALM Sandbox MCP Server Refrence
# SAP Cloud ALM Sandbox MCP Server

A lightweight **Model Context Protocol (MCP)** server that exposes selected **SAP Cloud ALM Sandbox APIs** as MCP tools.

Using **FastMCP**, this server allows MCP-compatible clients such as:

* Claude Desktop
* MCP Inspector
* Cursor
* Syntax GenAI Studio
* Other MCP-compatible applications

to directly query SAP Cloud ALM Sandbox data through natural language interactions.

> **Note**
>
> This project is intended for learning, testing, and proof-of-concept purposes using the SAP API Business Hub Sandbox APIs. The same approach can be extended to productive SAP Cloud ALM environments by implementing the appropriate authentication and API configuration.

---

## Features

This MCP server exposes SAP Cloud ALM Sandbox APIs as MCP tools.

### Available Tools

| Tool                    | Description                              |
| ----------------------- | ---------------------------------------- |
| `get_alm_projects`      | List all SAP Cloud ALM projects          |
| `get_landscape_objects` | List all SAP Cloud ALM landscape objects |
| `get_status_events`     | Retrieve SAP Cloud ALM status events     |
| `get_alm_tasks`         | List all SAP Cloud ALM tasks             |
| `get_alm_deliverables`  | List all SAP Cloud ALM deliverables      |

---

## Architecture

```text
Claude Desktop / Cursor / MCP Inspector
                │
                ▼
         SAP Cloud ALM MCP Server
                │
                ▼
      SAP API Business Hub Sandbox
```

---

## Prerequisites

Before starting, ensure you have:

* Python 3.10 or higher
* FastMCP
* Claude Desktop (optional)
* SAP API Business Hub Sandbox API Key

---

## Authentication

## Authentication

This project uses an SAP API Business Hub Sandbox API Key.

### Obtain an API Key

1. Log in to SAP API Business Hub.
2. Open your profile.
3. Copy your Sandbox API Key.

### Configure Environment Variable

#### Linux / macOS

```bash
export SAP_API_KEY="YOUR_API_KEY"
```

#### Windows Command Prompt

```cmd
set SAP_API_KEY=YOUR_API_KEY
```

#### Windows PowerShell

```powershell
$env:SAP_API_KEY="YOUR_API_KEY"
```

The MCP server automatically reads the API key from the environment variable.

No code changes are required.

---

## Project Structure

Keep all files in a single directory.

```text
sap-cloud-alm-mcp/
│
├── server.py
├── requirements.txt
├── README.md
└── .venv/
```

---

# Installation

## Linux / macOS

### Create Virtual Environment

```bash
python3 -m venv .venv
```

### Activate Virtual Environment

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Windows

### Create Virtual Environment

```powershell
python -m venv .venv
```

### Activate Virtual Environment

```powershell
.venv\Scripts\activate
```

### Install Dependencies

```powershell
pip install -r requirements.txt
```

---

## requirements.txt

```text
httpx
fastmcp
uv
```

---

# Running the MCP Server

## Standard MCP (stdio)

Used by:

* Claude Desktop
* Cursor
* MCP Inspector

```bash
python server.py
```

If the server starts successfully, no errors should be displayed.

---

## HTTP Mode (Optional)

Useful for remote MCP clients such as Syntax GenAI Studio.

Example:

```bash
python server.py --http --host 0.0.0.0 --port 8000
```

> Note:
>
> The provided `server.py` currently runs using `stdio`. Additional FastMCP HTTP configuration may be required depending on the FastMCP version being used.

---

# Configure Claude Desktop

Open Claude Desktop configuration:

### Windows

```text
%APPDATA%\Claude\claude_desktop_config.json
```

### macOS

```text
~/Library/Application Support/Claude/claude_desktop_config.json
```

Add the MCP server configuration:

```json
{
  "mcpServers": {
    "sap-cloud-alm": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "httpx",
        "--with",
        "fastmcp",
        "C:\\path\\to\\server.py"
      ],
      "env": {
        "SAP_API_KEY": "YOUR_API_KEY"
      }
    }
  }
}

```

Replace:

```text
C:\path\to\server.py
```

with your actual file location.

Restart Claude Desktop after saving the configuration.

---

# Example Prompts

Once connected, you can ask Claude:

```text
Show all SAP Cloud ALM projects.
```

```text
List Cloud ALM landscape objects.
```

```text
Retrieve all Cloud ALM tasks.
```

```text
Show recent Cloud ALM status events.
```

```text
List all Cloud ALM deliverables.
```

---

# SAP Cloud ALM Sandbox APIs Used

The server currently consumes the following SAP API Business Hub Sandbox endpoints:

### Projects

```text
/SAPCALM/calm-projects/v1/projects
```

### Landscape Objects

```text
/SAPCALM/calm-landscape/v1/landscapeObjects
```

### Status Events

```text
/SAPCALM/bsm-service/v1/events
```

### Tasks

```text
/ SAPCALM/calm-tasks/v1/tasks
```

### Deliverables

```text
/ SAPCALM/calm-tasks/v1/deliverables
```

Base URL:

```text
https://sandbox.api.sap.com
```

---

# Security Disclaimer

This project is intended for educational and sandbox testing purposes.

For productive SAP Cloud ALM integrations:

* Do not hardcode credentials.
* Use OAuth authentication where applicable.
* Store secrets securely.
* Implement proper error handling and logging.
* Follow SAP security best practices.

---

# License

MIT License

Feel free to fork, enhance, and adapt this project for your SAP Cloud ALM automation and AI integration scenarios.

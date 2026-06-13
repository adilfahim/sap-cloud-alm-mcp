import os

import httpx
from fastmcp import FastMCP

mcp = FastMCP("SAP Cloud ALM")

API_KEY = os.getenv("SAP_API_KEY")

if not API_KEY:
    raise ValueError("SAP_API_KEY environment variable is not set")

headers: dict[str, str] = {
    "APIKey": API_KEY.strip(),
    "Accept": "application/json"
}

@mcp.tool
async def get_alm_projects():
    """Get all SAP Cloud ALM projects from the sandbox."""
    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.get(
            "https://sandbox.api.sap.com/SAPCALM/calm-projects/v1/projects",
            headers=headers
        )

    if response.status_code != 200:
        return {"error": "Failed to get Cloud ALM Projects", "status_code": response.status_code, "detail": response.text}

    return response.json()

@mcp.tool
async def get_landscape_objects():
    """Get all SAP Cloud ALM Landscape Objects from the sandbox."""
    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.get(
            "https://sandbox.api.sap.com/SAPCALM/calm-landscape/v1/landscapeObjects",
            headers=headers
        )

    if response.status_code != 200:
        return {"error": "Failed to get Cloud ALM Landscape Objects", "status_code": response.status_code, "detail": response.text}

    return response.json()

@mcp.tool
async def get_status_events():
    """Get all SAP Cloud ALM Status Events from the sandbox."""
    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.get(
            "https://sandbox.api.sap.com/SAPCALM/bsm-service/v1/events",
            headers=headers
        )

    if response.status_code != 200:
        return {"error": "Failed to get Cloud ALM Status Events", "status_code": response.status_code, "detail": response.text}

    return response.json()

@mcp.tool
async def get_alm_tasks():
    """Get all SAP Cloud ALM Tasks from the sandbox."""
    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.get(
            "https://sandbox.api.sap.com/SAPCALM/calm-tasks/v1/tasks",
            headers=headers
        )

    if response.status_code != 200:
        return {"error": "Failed to get Cloud ALM Tasks", "status_code": response.status_code, "detail": response.text}

    return response.json()

@mcp.tool
async def get_alm_deliverables():
    """Get all SAP Cloud ALM Deliverables from the sandbox."""
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.get(
            "https://sandbox.api.sap.com/SAPCALM/calm-tasks/v1/deliverables",
            headers=headers
        )

    if response.status_code != 200:
        return {"error": "Failed to get Cloud ALM Deliverables", "status_code": response.status_code, "detail": response.text}

    return response.json()

@mcp.tool
async def get_analytics_providers():
    """Get all SAP Cloud ALM Analytics from the sandbox."""
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.get(
            "https://sandbox.api.sap.com/SAPCALM/calm-analytics/v1/analytics/providers/data",
            headers=headers
        )

    if response.status_code != 200:
        return {"error": "Failed to get Cloud Analytics", "status_code": response.status_code, "detail": response.text}

    return response.json()

@mcp.tool
async def get_health_monitoring():
    """Get all SAP Cloud Health Monitoring from the sandbox."""
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.get(
            "https://sandbox.api.sap.com/SAPCALM/calm-analytics/v1/odata/v4/analytics/Metrics",
            headers=headers
        )

    if response.status_code != 200:
        return {"error": "Failed to get Cloud Health Monitoring", "status_code": response.status_code, "detail": response.text}

    return response.json()

if __name__ == "__main__":
    mcp.run(transport="stdio")

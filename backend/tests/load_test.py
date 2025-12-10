# Placeholder for load testing script

import asyncio
import httpx
import time

async def simulate_user(session_id, client):
    """Simulates a single user interaction."""
    headers = {"X-API-Key": os.environ.get("API_KEY", "your_default_api_key")} # Replace with actual API key if needed
    base_url = "http://localhost:8000/api/chat" # Replace with actual backend URL

    # Initial query
    payload = {
        "session_id": session_id,
        "query": "What is physical AI?",
        "selected_text": None
    }
    response = await client.post(base_url, json=payload, headers=headers)
    print(f"User {session_id} - Initial Query Status: {response.status_code}")
    # You might want to parse response.json() and use the returned session_id for subsequent calls

    # Follow-up query
    if response.status_code == 200:
        session_id_from_response = response.json().get("session_id", session_id)
        payload = {
            "session_id": session_id_from_response,
            "query": "Tell me more about its applications.",
            "selected_text": None
        }
        response = await client.post(base_url, json=payload, headers=headers)
        print(f"User {session_id} - Follow-up Query Status: {response.status_code}")

async def main():
    num_users = 100 # Simulate 100 concurrent users
    async with httpx.AsyncClient() as client:
        tasks = [simulate_user(f"user_{i}", client) for i in range(num_users)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    import os
    print("Starting load test simulation...")
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"Load test simulation finished in {end_time - start_time:.2f} seconds.")


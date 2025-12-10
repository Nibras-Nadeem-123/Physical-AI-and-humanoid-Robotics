# Placeholder for latency benchmarking script

import asyncio
import httpx
import time
import statistics
import os

async def measure_latency(query, session_id, client):
    """Measures latency for a single query."""
    headers = {"X-API-Key": os.environ.get("API_KEY", "your_default_api_key")} # Replace with actual API key if needed
    base_url = "http://localhost:8000/api/chat" # Replace with actual backend URL

    payload = {
        "session_id": session_id,
        "query": query,
        "selected_text": None
    }
    
    start_time = time.time()
    try:
        response = await client.post(base_url, json=payload, headers=headers, timeout=30.0) # 30 second timeout
        response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)
        end_time = time.time()
        return (end_time - start_time) * 1000 # return latency in milliseconds
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
        return None
    except httpx.RequestError as e:
        print(f"An error occurred while requesting {e.request.url!r}: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

async def main():
    num_runs = 50 # Number of times to run each query
    test_queries = [
        "What is Physical AI?",
        "Explain ROS 2 in brief.",
        "What are humanoid robots?"
    ]

    latencies = {query: [] for query in test_queries}

    async with httpx.AsyncClient() as client:
        print("Starting latency benchmarking...")
        for query in test_queries:
            print(f"\nBenchmarking query: '{query}'")
            for i in range(num_runs):
                session_id = f"benchmark_session_{query}_{i}"
                latency = await measure_latency(query, session_id, client)
                if latency is not None:
                    latencies[query].append(latency)
                    print(f"  Run {i+1}: {latency:.2f} ms")
                else:
                    print(f"  Run {i+1}: Failed")
                await asyncio.sleep(0.1) # Small delay to avoid overwhelming server

        print("\n--- Latency Benchmark Results ---")
        for query, query_latencies in latencies.items():
            if query_latencies:
                print(f"\nQuery: '{query}'")
                print(f"  Min: {min(query_latencies):.2f} ms")
                print(f"  Max: {max(query_latencies):.2f} ms")
                print(f"  Average: {statistics.mean(query_latencies):.2f} ms")
                print(f"  Median: {statistics.median(query_latencies):.2f} ms")
                if len(query_latencies) >= 2:
                    print(f"  Standard Deviation: {statistics.stdev(query_latencies):.2f} ms")
                print(f"  P95: {statistics.quantiles(query_latencies, n=100)[94]:.2f} ms")
            else:
                print(f"\nQuery: '{query}' - No successful runs.")

if __name__ == "__main__":
    import os
    asyncio.run(main())

import requests
import sys

def verify():
    base_url = "http://127.0.0.1:8000"
    results = []
    
    try:
        # 1. List clips
        resp = requests.get(f"{base_url}/play/")
        results.append(f"GET /play/: {resp.status_code}")
        if resp.status_code == 200:
            clips = resp.json()
            results.append(f"Found {len(clips)} clips")
            if len(clips) > 0:
                clip_id = clips[0]['id']
                
                # 2. Get stats
                resp = requests.get(f"{base_url}/play/{clip_id}/stats")
                results.append(f"GET /play/{clip_id}/stats: {resp.status_code}")
                results.append(f"Stats: {resp.text}")
                
                # 3. Stream (head)
                resp = requests.get(f"{base_url}/play/{clip_id}/stream", stream=True)
                results.append(f"GET /play/{clip_id}/stream: {resp.status_code}")
                results.append(f"Content-Type: {resp.headers.get('content-type')}")
                resp.close()
                
        # 4. Metrics
        resp = requests.get(f"{base_url}/metrics")
        results.append(f"GET /metrics: {resp.status_code}")
        if "http_requests_total" in resp.text:
            results.append("Metrics contain http_requests_total")
            
    except Exception as e:
        results.append(f"Error: {e}")
        
    with open("verification_results.txt", "w") as f:
        f.write("\n".join(results))

if __name__ == "__main__":
    verify()

import subprocess
import time

# Note
# The unittest for this kata *must mock* the ping to avoid actual network calls.



def ping_host(hostname: str, count: int = 5):
    """
    Pings a host and returns connection statistics.
    
    Args:
        hostname: Host to ping (e.g., 'google.com')
        count: Number of ping attempts
        
    Returns:
        Dictionary with:
        - 'host': hostname
        - 'avg_response_time_ms': average response time in milliseconds
        - 'success': True if any packets received
    """
    # TODO: Use subprocess.run() to execute ping command
    # Linux/Mac: ping -c {count} {hostname}
    # Parse output to extract the average latency in milliseconds

    cmd = ["ping", "-c", str(count), hostname]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        output = result.stdout
        # Example output parsing (Linux):
        # rtt min/avg/max/mdev = 14.123/15.456/16.789/0.123 ms
        for line in output.splitlines():
            if "rtt min/avg/max/mdev" in line:
                stats = line.split('=')[1].strip().split('/')[1]
                avg_response_time_ms = float(stats)
                return {
                    'host': hostname,
                    'avg_response_time_ms': avg_response_time_ms,
                    'success': True
                }
        return {
            'host': hostname,
            'avg_response_time_ms': None,
            'success': False
        }
    except Exception:
        return {
            'host': hostname,
            'avg_response_time_ms': None,
            'success': False
        }




if __name__ == '__main__':
    # Test the functions
    ping_result = ping_host("8.8.8.8", 3)
    print(f"Ping result: {ping_result}")
    ping_result = ping_host("google.com", 3)
    print(f"Ping result: {ping_result}")

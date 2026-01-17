request_count = {}
MAX_REQUESTS = 5

def check_rate_limit(ip):
    if ip not in request_count:
        request_count[ip] = 1
    else:
        request_count[ip] += 1

    return request_count[ip] > MAX_REQUESTS

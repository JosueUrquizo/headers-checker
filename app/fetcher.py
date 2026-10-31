import httpx
from app.security import UnsafeURLError, validate_url

MAX_REDIRECTS = 3
TIMEOUT_SECONDS = 5.0


def fetch_headers(url: str) -> dict[str, str]:
    current = url
    for _ in range(MAX_REDIRECTS + 1):
        validate_url(current)
        response = httpx.get(
            current, follow_redirects=False, timeout=TIMEOUT_SECONDS
        )
        if response.is_redirect:
            location = response.headers["location"]
            current = str(httpx.URL(current).join(location))
            continue
        return dict(response.headers)
    raise UnsafeURLError("Demasiadas redirecciones.")

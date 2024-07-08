from fastapi.testclient import TestClient
from starlette import status

from backend.api.main import api

client = TestClient(api)


def test_health() -> None:
    r = client.get("/health")
    assert r.text.strip('"').startswith("OK")
    assert r.status_code == status.HTTP_200_OK

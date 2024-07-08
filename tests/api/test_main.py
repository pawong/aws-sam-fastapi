from fastapi.testclient import TestClient
from starlette import status

from backend.api.main import api

client = TestClient(api)


def test_root() -> None:
    r = client.get("/")
    assert r.json() == {"Hello": "World"}
    assert r.status_code == status.HTTP_200_OK

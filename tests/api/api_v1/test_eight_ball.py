from fastapi.testclient import TestClient
from starlette import status

from backend.api.api_v1.eight_ball import answers
from backend.api.main import api

client = TestClient(api)


def test_get_answer_only() -> None:
    r = client.get("/8ball")
    assert r.text.strip('"') in answers
    assert r.status_code == status.HTTP_200_OK


def test_get_answer() -> None:
    r = client.post("/8ball", data='{"question":"Will I die today?"}')
    assert r.json()["question"] == "Will I die today?"
    assert r.json()["answer"] in answers
    assert r.status_code == status.HTTP_200_OK

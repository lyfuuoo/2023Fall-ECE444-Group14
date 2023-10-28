"""mainPage_test.py: testing main page functionality."""
__author__      = "Jerry Cui"

from project.mainPage import app

def test_index():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b"Hello, World!"


def test_displayMainPageWithEmptyEvent():
    pageInfo = []
    tester = app.test_client()
    response = tester.post("/mainPage", data=dict(pageInfo), content_type="html/text")

    assert response.status_code == 200


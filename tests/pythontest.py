
def test_request_example(client):
    """This makes the index page"""
    response = client.get("/python.html")
    assert response.status_code == 200
    assert b"Python/Flask" in response.data
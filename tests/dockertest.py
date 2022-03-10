def test_request_example(client):
    """This makes the index page"""
    response = client.get("/docker.html")
    assert response.status_code == 200
    assert b"Docker" in response.data
from fastapi.testclient import TestClient
from main.main import app  # Ensure your FastAPI main app is correctly imported

client = TestClient(app)

# def test_signup():
#     response = client.post("/signup", json={"email": "user@example.com", "password": "password123"})
#     assert response.status_code == 200
#     token = response.json().get("access_token")
#     print("Signup token:", token)
#     assert "access_token" in response.json()

def test_signup():
    response = client.post("/signup", json={"email": "user2@example.com", "password": "Password@12345"})
    print("Response status:", response.status_code)
    print("Response body:", response.json())  # This will show the error details if any
    assert response.status_code == 200, "Expected status code 200 but got {}".format(response.status_code)

def test_login():
    response = client.post("/login", json={"email": "user2@example.com", "password": "Password@123"})
    assert response.status_code == 200
    assert "access_token" in response.json()

if __name__ == "__main__":
    test_signup()
    test_login()
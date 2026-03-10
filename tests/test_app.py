import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Test GET /activities

def test_get_activities():
    # Arrange
    # ...nothing to arrange for this endpoint...
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# Test POST /activities/{activity_name}/signup

def test_signup_for_activity_success():
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"
    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})
    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for {activity}"


def test_signup_for_activity_not_found():
    # Arrange
    activity = "Nonexistent Club"
    email = "student@mergington.edu"
    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"

# Test POST /activities/{activity_name}/unregister

def test_unregister_for_activity_success():
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"
    # Act
    response = client.post(f"/activities/{activity}/unregister", params={"email": email})
    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Removed {email} from {activity}"


def test_unregister_for_activity_not_found():
    # Arrange
    activity = "Nonexistent Club"
    email = "student@mergington.edu"
    # Act
    response = client.post(f"/activities/{activity}/unregister", params={"email": email})
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_for_activity_participant_not_found():
    # Arrange
    activity = "Chess Club"
    email = "ghost@mergington.edu"
    # Act
    response = client.post(f"/activities/{activity}/unregister", params={"email": email})
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"

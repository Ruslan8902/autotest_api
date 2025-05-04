import httpx

# Данные для входа в систему
login_payload = {
    "email": "custom_user@example.com",
    "password": "12345"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print(login_response.status_code)
print(login_response.json())


# Выполняем запрос для получения данных аутентифицированного пользователя
accessToken = login_response_data["token"]["accessToken"]
headers = {"Authorization": f"Bearer {accessToken}"}
response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print(response.status_code)
print(response.json())

from typing import TypedDict
import allure

from httpx import Response
from tools.routes import APIRoutes

from clients.api_client import APIClient
from clients.authentication.authentication_schema import LoginRequestSchema, RefreshRequestSchema, LoginResponseSchema
from clients.public_http_builder import get_public_http_client
from clients.api_coverage import tracker

class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """

    @allure.step("Authenticate user")
    @tracker.track_coverage_httpx(f"{APIRoutes.AUTHENTICATION}/login")
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f"{APIRoutes.AUTHENTICATION}/login", json=request.model_dump(by_alias=True))

    @allure.step("Refresh authentication token")
    @tracker.track_coverage_httpx(f"{APIRoutes.AUTHENTICATION}/refresh")
    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f"{APIRoutes.AUTHENTICATION}/refresh", json=request.model_dump(by_alias=True))

    # Добавили метод login
    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)  # Отправляем запрос на аутентификацию
        return LoginResponseSchema.model_validate_json(response.text) # Извлекаем JSON из ответа


def get_authentication_client() -> AuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())
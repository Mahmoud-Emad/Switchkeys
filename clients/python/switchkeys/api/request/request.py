import json
from typing import Any, Dict
import requests
from switchkeys.api.response.response import SwitchKeysResponse
from enum import Enum


class SwitchKeysRequestMethod(Enum):
    POST = "POST"
    GET = "GET"
    PUT = "PUT"
    DELETE = "DELETE"


class SwitchKeysRequest:
    """
    Make an HTTP request to the specified URL using the provided method.

    Args:
        url (str): The URL to make the request to.
        method (SwitchKeysRequestMethod): The HTTP method to use for the request.
        headers (Dict[str, str]): Additional headers for the request.

    Returns:
        SwitchKeysResponse: An object containing the response from the request.

    Raises:
        ValueError: If an invalid method is provided.
    """

    @staticmethod
    def call(
        url: str,
        method: SwitchKeysRequestMethod,
        data: Dict[str, Any] = {},
        token: str | None = None,
    ) -> SwitchKeysResponse:
        try:
            headers = {}
            if token:
                headers["Authorization"] = f"Bearer {token}"

            if method == SwitchKeysRequestMethod.GET:
                response = requests.get(url)
            elif method == SwitchKeysRequestMethod.POST:
                response = requests.post(url, json=data, headers=headers)
            elif method == SwitchKeysRequestMethod.PUT:
                response = requests.put(url, json=data, headers=headers)
            elif method == SwitchKeysRequestMethod.DELETE:
                response = requests.delete(url, headers=headers)
            else:
                raise ValueError("Invalid method provided.")

            response_content = response.content.decode()

            # Check if response content is not valid JSON.
            if response_content.startswith("<!DOCTYPE html>"):
                print("response_content", response_content)
                return SwitchKeysResponse(
                    status_code=response.status_code,
                    error_message="Response content is not valid json.",
                )

            # Check if response content is empty
            if not response_content.strip():
                return SwitchKeysResponse(
                    status_code=response.status_code,
                    error_message="Empty response content",
                )

            response_content = json.loads(response_content)

            if response.status_code >= 200 and response.status_code < 400:
                return SwitchKeysResponse(
                    status_code=response.status_code,
                    message=response_content.get("message"),
                    data=response_content.get("results"),
                )
            elif response.status_code >= 400:
                if response_content.get("detail") is None:
                    error_message = response_content.get("message")
                else:
                    error_message = response_content.get("detail")

                error = response_content.get("error")

                return SwitchKeysResponse(
                    status_code=response.status_code,
                    error_message=error_message,
                    error=error
                )
            else:
                return SwitchKeysResponse(
                    status_code=response.status_code,
                    error_message=response_content.get("detail"),
                )
        except requests.exceptions.RequestException as e:
            return SwitchKeysResponse(
                status_code=500,
                error_message=str(e),
                data=None,
                message=str(e),
            )

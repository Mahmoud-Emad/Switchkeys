import json
from typing import Any, Dict
import requests
from switchkey.api.response import SwitchKeyResponse
from enum import Enum


class SwitchKeyRequestMethod(Enum):
    POST = "POST"
    GET = "GET"
    PUT = "PUT"
    DELETE = "DELETE"


class SwitchKeyRequest:
    """
    Make an HTTP request to the specified URL using the provided method.

    Args:
        url (str): The URL to make the request to.
        method (SwitchKeyRequestMethod): The HTTP method to use for the request.

    Returns:
        SwitchKeyResponse: An object containing the response from the request.

    Raises:
        ValueError: If an invalid method is provided.
    """

    @staticmethod
    def call(
        url: str,
        method: SwitchKeyRequestMethod,
        data: Dict[str, Any] = {}
    ) -> SwitchKeyResponse:
        try:
            if method == SwitchKeyRequestMethod.GET:
                response = requests.get(url)
            elif method == SwitchKeyRequestMethod.POST:
                response = requests.post(url, json=data)
            elif method == SwitchKeyRequestMethod.PUT:
                response = requests.put(url, json=data)
            elif method == SwitchKeyRequestMethod.DELETE:
                response = requests.delete(url)
            else:
                raise ValueError("Invalid method provided.")

            response_content = response.content.decode()
            
            # Check if response content is not valid JSON.
            if response_content.startswith("<!DOCTYPE html>"):
               return SwitchKeyResponse(
                    status_code=response.status_code,
                    error_message="Response content is not valid json.",
                )

            # Check if response content is empty
            if not response_content.strip():
                return SwitchKeyResponse(
                    status_code=response.status_code,
                    error_message="Empty response content",
                )

            response_content = json.loads(response_content)

            if response.status_code >= 200 and response.status_code < 400:
                return SwitchKeyResponse(
                    status_code=response.status_code,
                    message=response_content.get("message"),
                    data=response_content.get("results"),
                )
            elif response.status_code >= 400:
                if response_content.get("detail") is None:
                    error_message = response_content.get("message")
                else:
                    error_message = response_content.get("detail")
                return SwitchKeyResponse(
                    status_code=response.status_code,
                    error_message=error_message,
                )
            else:
                return SwitchKeyResponse(
                    status_code=response.status_code,
                    error_message=response_content.get("detail"),
                )
        except requests.exceptions.RequestException as e:
            return SwitchKeyResponse(
                status_code=500,
                error_message=str(e),
                data=None,
                message=str(e),
            )

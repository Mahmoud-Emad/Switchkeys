import json
import requests
from switchkey.api.response import SwitchKeyResponse
from enum import Enum


class SwitchKeyRequestMethod(Enum):
    POST = "POST"
    GET = "GET"
    PUT = "PUT"
    DELETE = "DELETE"


class SwitchKeyRequest:
    @staticmethod
    def call(
        url: str,
        method: SwitchKeyRequestMethod,
    ) -> SwitchKeyResponse:
        try:
            if method == SwitchKeyRequestMethod.GET:
                response = requests.get(url)
            elif method == SwitchKeyRequestMethod.POST:
                response = requests.post(url)
            elif method == SwitchKeyRequestMethod.PUT:
                response = requests.put(url)
            elif method == SwitchKeyRequestMethod.DELETE:
                response = requests.delete(url)
            else:
                raise ValueError("Invalid method provided.")

            response_content = response.content.decode()
            response_content = json.loads(response_content)

            if response.status_code >= 200 and response.status_code < 400:
                # print("response_content", response_content)
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
                status_code=500, error_message=str(e), data_type=None
            )

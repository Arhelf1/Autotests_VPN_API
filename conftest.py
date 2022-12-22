import pytest
import requests

@pytest.fixture(scope="session")
def base_env(request, allure_env):
    env = request.config.getoption("--env")


class Application:
    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path, data, headers=None, cookies=None, ):
        return requests.post(url=self.base_address + path, json=data, headers=headers, cookies=cookies)

    # def get(self, path="/", params=None, headers=None):
    #     return requests.request("GET", url=self.base_address+path, params=params, headers=headers)


@pytest.fixture
def vpn_api():
    return Application(base_address="https://site.test.infra.gnuvpn.com/api/v1/")

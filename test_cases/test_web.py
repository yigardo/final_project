
from workflows.web_flows import WebFlows
import pytest


@pytest.mark.usefixtures("init_web_driver")
class Test_Web:
    def test_verify_login(self):
        WebFlows.login_flow("admin", "admin")

from unittest.mock import Mock, patch

from itential.core import Itential


@patch("itential.core.requests.post")
def test_authentication(mock_post):
    client = Itential()
    # print(f"{mock_post=}")

    # print(f"{client.session.cookies=}")
    client._authenticate_call()
    # print(f"{client.session.cookies=}")


if __name__ == '__main__':
    test_authentication()

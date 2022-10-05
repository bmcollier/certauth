import requests


def get_payload():
    response = requests.get("http://127.0.0.1:8000")
    print(f"The endpoint response is: {response.text}")

def get_payload_secure():
    #response = requests.get("https://127.0.0.1:8000")
    #response = requests.get("https://127.0.0.1:8000", verify="ca_public_key.pem")
    response = requests.get("https://my-server.com:8000", verify="ca_public_key.pem")
    print(f"The endpoint response is {response.text}")


if __name__ == "__main__":
    get_payload()


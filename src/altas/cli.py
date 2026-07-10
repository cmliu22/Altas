from altas.application import ChatApplication
from altas.providers.mock import MockProvider


def main():

    app = ChatApplication(
        provider=MockProvider()
    )

    message = input("> ")

    response = app.chat(message)

    print(response)


if __name__ == "__main__":
    main()
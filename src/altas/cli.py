from altas.application import ChatApplication
from altas.config import get_settings
from altas.providers.mock import MockProvider


def main():

    settings = get_settings()

    print(f"Using provider: {settings.provider}")

    # Provider selection will be introduced in the provider factory step.
    app = ChatApplication(
        provider=MockProvider()
    )

    message = input("> ")

    response = app.chat(message)

    print(response)


if __name__ == "__main__":
    main()
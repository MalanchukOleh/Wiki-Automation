import pytest

from src.utils.globals.appium_service import appium_service

if __name__ == "__main__":
    appium_service.start()
    pytest.main()
    appium_service.stop()

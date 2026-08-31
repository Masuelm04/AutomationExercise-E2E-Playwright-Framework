import os

BASE_URL = "https://www.automationexercise.com"
DEFAULT_TIMEOUT = 20000
HEADLESS = os.getenv(
    "HEADLESS",
    "false"
).lower() == "true"
REPORTS_DIR = "reports"
TEST_RESULTS_DIR = "test-results"
SCREENSHOTS_DIR = f"{TEST_RESULTS_DIR}/screenshots"
TRACES_DIR = f"{TEST_RESULTS_DIR}/traces"
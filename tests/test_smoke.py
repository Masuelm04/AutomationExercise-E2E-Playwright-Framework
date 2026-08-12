from config.settings import BASE_URL

def test_open_automation_exercise(page):

    page.goto(BASE_URL)

    assert "Automation Exercise" in page.title()
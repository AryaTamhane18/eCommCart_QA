import os
from pathlib import Path
import allure
from playwright.sync_api import sync_playwright
from datetime import datetime


def before_all(context):
    print("Setting up the environment before all tests.")
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True, args=['--start-maximized'], slow_mo=200)

    base_reports_dir = Path("Temp_reports")
    context.allure_reports_dir = base_reports_dir / "allure_reports"
    context.allure_reports_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime('%d-%b-%y-%H%M%S')
    context.tmp_dir = base_reports_dir / f"tmp_{timestamp}"
    context.video_dir = context.tmp_dir / "videos"
    context.screenshot_dir = context.tmp_dir / "screenshots"
    context.video_dir.mkdir(parents=True, exist_ok=True)
    context.screenshot_dir.mkdir(parents=True, exist_ok=True)

    context.browser_context = context.browser.new_context(no_viewport=True, ignore_https_errors=True,
                                                          record_video_dir=str(context.video_dir))


def before_scenario(context, scenario):
    print("Setting up the environment before each scenario.")
    context.page = context.browser_context.new_page()
    context.page.goto("https://www.saucedemo.com/")


def after_scenario(context, scenario):
    print("closing the page for the scenario...")
    screenshot_path = context.screenshot_dir / f"{scenario.name.replace(' ','_')}.png"
    context.page.screenshot(path=str(screenshot_path), full_page=True)

    with open(screenshot_path, "rb") as f:
        allure.attach(f.read(), name=scenario.name, attachment_type=allure.attachment_type.PNG)

    video_path = None
    if scenario.status == 'failed' and context.page.video:
        video_path = context.page.video.path()

    context.page.close()

    if video_path and os.path.exists(video_path):
        with open(video_path, "rb") as f:
            allure.attach(f.read(), name=scenario.name, attachment_type=allure.attachment_type.WEBM)


def after_all(context):
    print("Tearing down the environment after all tests.")
    context.browser_context.close()
    context.browser.close()
    context.playwright.stop()

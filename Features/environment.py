import os
from pathlib import Path
from utils.logger import setup_file_logger, log
import allure
from playwright.sync_api import sync_playwright
from datetime import datetime


def before_all(context):
    log.info("Setting up the environment before all tests.")
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True, args=['--start-maximized'], slow_mo=200)

    base_reports_dir = Path("Temp_reports")
    context.allure_reports_dir = base_reports_dir / "allure_reports"
    context.allure_reports_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime('%d-%b-%y-%H%M%S')
    context.tmp_dir = base_reports_dir / f"tmp_{timestamp}"
    context.video_dir = context.tmp_dir / "videos"
    context.screenshot_dir = context.tmp_dir / "screenshots"
    context.logs_dir = context.tmp_dir / "logs"
    context.video_dir.mkdir(parents=True, exist_ok=True)
    context.screenshot_dir.mkdir(parents=True, exist_ok=True)
    context.logs_dir.mkdir(parents=True, exist_ok=True)

    context.browser_context = context.browser.new_context(no_viewport=True, ignore_https_errors=True,
                                                          record_video_dir=str(context.video_dir))


def before_scenario(context, scenario):
    log.info("Setting up the environment before each scenario.")
    context.page = context.browser_context.new_page()
    context.page.goto("https://www.saucedemo.com/")

    context.log_file_path = setup_file_logger(scenario.name, str(context.logs_dir))
    log.info(f"Starting scenario: {scenario.name}")


def after_scenario(context, scenario):
    log.info("closing the page for the scenario...")
    screenshot_path = context.screenshot_dir / f"{scenario.name.replace(' ','_')}.png"
    context.page.screenshot(path=str(screenshot_path), full_page=True)

    with open(screenshot_path, "rb") as f:
        allure.attach(f.read(), name=scenario.name, attachment_type=allure.attachment_type.PNG)

    video_path = None
    if scenario.status == 'failed' and context.page.video:
        video_path = context.page.video.path()

    context.page.close()

    if video_path and os.path.exists(video_path):
        saved_video_path = context.video_dir / f"{scenario.name.replace(' ', '_')}.webm"
        context.page.video.save_as(str(saved_video_path))
        with open(video_path, "rb") as f:
            allure.attach(f.read(), name=scenario.name, attachment_type=allure.attachment_type.WEBM)

    if hasattr(context, "log_file_path") and os.path.exists(context.log_file_path):
        with open(context.log_file_path, "rb") as f:
            allure.attach(f.read(), name=f"Logs - {scenario.name}", attachment_type=allure.attachment_type.TEXT)


def after_all(context):
    log.info("Tearing down the environment after all tests.")
    context.browser_context.close()
    context.browser.close()
    context.playwright.stop()

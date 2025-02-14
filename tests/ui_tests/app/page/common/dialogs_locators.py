# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Dialog locators"""

from selenium.webdriver.common.by import By

from tests.ui_tests.app.helpers.locator import Locator


class DeleteDialog:
    """Delete Dialog class"""

    body = Locator(By.CSS_SELECTOR, "mat-dialog-container", "Dialog with choices")
    yes = Locator(By.XPATH, "//button//span[contains(text(), 'Yes')]", "Yes button in delete dialog")


class ActionDialog:
    """Action Dialog class"""

    body = Locator(By.CSS_SELECTOR, "mat-dialog-container", "Dialog with choices")
    text = Locator(By.CSS_SELECTOR, "app-dialog mat-dialog-content", "Dialog content")
    next_btn = Locator(By.CSS_SELECTOR, ".mat-stepper-next", "Next button in action dialog")
    run = Locator(By.CSS_SELECTOR, "app-dialog button[color='accent']", "Run button in action dialog")

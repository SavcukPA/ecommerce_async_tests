import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.host = "https://demoqa.com/"

    @allure.step("Open a browser")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Open self_endpoint a browser")
    def open_self(
        self,
    ):
        self.driver.get(f"{self.host}{self.endpoint}")

    @allure.step("Find a visible element")
    def element_is_visible(self, locator: tuple[str, str], timeout=20) -> WebElement:
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Find visible elements")
    def elements_are_visible(
        self, locator: tuple[str, str], timeout=20
    ) -> list[WebElement]:
        return wait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    @allure.step("Find a present element")
    def element_is_present(self, locator: tuple[str, str], timeout=20) -> WebElement:
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Find present elements")
    def elements_are_present(
        self, locator: tuple[str, str], timeout=20
    ) -> list[WebElement]:
        return wait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    @allure.step("Find a not visible element")
    def element_is_not_visible(self, locator: tuple[str, str], timeout=20):
        return wait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Find clickable elements")
    def element_is_clickable(self, locator: tuple[str, str], timeout=20):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Go to specified element")
    def go_to_element(self, element: WebElement):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Double click")
    def action_double_click(self, element: WebElement):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    @allure.step("Right click")
    def action_right_click(self, element: WebElement):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    @allure.step("Drag and drop by offset")
    def action_drag_and_drop_by_offset(self, element: WebElement, x_coords, y_coords):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.perform()

    @allure.step("Drag and drop element to element")
    def action_drag_and_drop_to_element(self, source: WebElement, target: WebElement):
        action = ActionChains(self.driver)
        action.drag_and_drop(source=source, target=target)
        action.perform()

    @allure.step("Move cursor to element")
    def action_move_to_element(self, element: WebElement):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

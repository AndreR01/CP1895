class Lightbulb:
    def __init__(self, wattage: int, is_led:bool, brand_name: str, brightness: int, is_on: bool = False):
        self.wattage = wattage
        self.is_led = is_led
        self.brand_name = brand_name
        self.is_on = is_on
        self.brightness = brightness

    def turn_on(is_on):
        Lightbulb.is_on = True
        return is_on

myLightbulb = Lightbulb(10, True, "Phillip", 8, False)

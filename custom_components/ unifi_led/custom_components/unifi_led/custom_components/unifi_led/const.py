"""Constants for the UniFi LED integration."""

DOMAIN = "unifi_led"

VERSION = "1.0.0"


# Configuration keys

CONF_HOST = "host"

CONF_USERNAME = "username"

CONF_PRIVATE_KEY = "private_key"


# Default SSH configuration

DEFAULT_SSH_PORT = 22


# Supported platforms

PLATFORMS = [
    "button",
    "sensor",
]


# Services

SERVICE_SET_COLOR = "set_color"

SERVICE_SET_RGB = "set_rgb"

SERVICE_TURN_ON = "turn_on"

SERVICE_TURN_OFF = "turn_off"


# Supported LED colors
#
# RGB values discovered and tested
# on UniFi E7 hardware.

COLOR_MAP = {

    "blue": "1,23,103",

    "green": "0,255,0",

    "red": "255,0,0",

    "white": "255,255,255",

}


# LED state names

LED_ON = "on"

LED_OFF = "off"

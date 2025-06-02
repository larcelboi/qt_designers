from enum import Enum

class DeviceType(Enum):
    LIGHT = "Light"
    SENSOR = "Sensor"
    CAMERA = "Camera"

class DistrictType(Enum):
    RESIDENTIAL = "Residential"
    COMMERCIAL = "Commercial"
    INDUSTRIAL = "Industrial"

class TrafficLightMode(Enum):
    NORMAL = "Normal"
    BLINKING = "Blinking"

from smartdevice import SmartDevice
from enum_device_type import DeviceType,DistrictType,TrafficLightMode

class Camera(SmartDevice):
    def __init__(self,name : str,energy_usage:int,status:bool,malfunctioning:bool,recording:bool):
        super().__init__(name,energy_usage,status,malfunctioning)
        self.recording = recording

    @property
    def recording(self):
        return self._recording
    @recording.setter
    def recording(self,nouv_recording):
        if isinstance(nouv_recording,bool):
            self._recording = nouv_recording
        else:
            raise TypeError('recording must be a bool')

    def toggle_recording(self):
        if self.recording:
            self.recording = False
        else:
            self.recording = True

    def __str__(self):
        return super().__str__() + f"Camera: {"IS recording"if self.recording else "is NOT recording"}"

class Sensor (SmartDevice):
    def __init__(self,name : str,energy_usage:int,status:bool,malfunctioning:bool,sensitivity:int):
        super().__init__(name,energy_usage,status,malfunctioning)

        self.sensitivity = sensitivity

    @property
    def sensitivity(self):
        return self._sensitivity

    @sensitivity.setter
    def sensitivity(self, nouv_sensitivity):
        if isinstance(nouv_sensitivity, int) and nouv_sensitivity in range(0,101):
            self._sensitivity = nouv_sensitivity
        else:
            raise ValueError("Sensitivity must be between 0 and 100")

    def __str__(self):
        return super().__str__() + f"Camera: {self.sensitivity}"

class TrafficLight (SmartDevice):
    def __init__(self,name : str,energy_usage:int,status:bool,malfunctioning:bool,mode:TrafficLightMode):
        super().__init__(name,energy_usage,status,malfunctioning)
        self.mode = mode

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, nouv_mode):
        if isinstance(nouv_mode, TrafficLightMode):
            self._mode = nouv_mode
        else:
            raise ValueError("Sensitivity must be between 0 and 100")

    def change_mode(self):
        if self.mode == TrafficLightMode.NORMAL:
            self.mode = TrafficLightMode.BLINKING
        elif self.mode == TrafficLightMode.BLINKING:
            self.mode = TrafficLightMode.NORMAL

    def __str__(self):
        return super().__str__() + "Mode: " + str(self.mode.value)
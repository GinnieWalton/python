class Television:
    """Default settings for class variables"""
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self):
        self.__status = False #Tv is off as default
        self.__muted = False #Tv is not muted as default
        self.__volume = Television.MIN_VOLUME #default volume is at 0
        self.__channel = Television.MIN_CHANNEL #default channel is at 0

    def power(self):
        self.__status = not self.__status #toggles power on and off
    def mute(self):
        self.__muted = not self.__muted #toggles mute on and off
    def channel_up(self):
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1) #iterates up through channels
    def channel_down(self):
        if self.__status:
            self.__channel = (self.__channel - 1) % (Television.MAX_CHANNEL + 1) #iterates down through channels
    def volume_up(self):
        if self.__status and not self.__muted:
            if self.__volume < Television.MAX_VOLUME: #turns volume up
                self.__volume += 1
    def volume_down(self):
        if self.__status and not self.__muted:
            if self.__volume > Television.MIN_VOLUME: #turns volume down
                self.__volume -= 1

    def __str__(self):
        """Prints out the current status of the variables"""
        status = "True" if self.__status else "False"
        volume = "Muted" if self.__muted else self.__volume
        return f"Power = {status}, Channel = {self.__channel}, Volume = {volume}"
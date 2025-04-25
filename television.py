class Television:
    """
    A class representing a simple Television with power, mute, channel, and volume control.
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initializes a new Television instance with power off, volume at minimum, and channel at minimum.
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL


    def power(self) -> None:
        """
        Toggles the power status of the television (on/off).
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggles the muted status of the television.
        Only works if the television is powered on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increments the channel by 1.
        Wraps around to MIN_CHANNEL if MAX_CHANNEL is exceeded.
        Only works if the television is powered on.
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else: 
                self.__channel += 1 
    
    def channel_down(self) -> None:
        """
        Decrements the channel by 1.
        Wraps around to MAX_CHANNEL if MIN_CHANNEL is passed.
        Only works if the television is powered on.
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increases the volume by 1.
        Unmutes the television if it was muted.
        Only works if the television is powered on and volume is below MAX_VOLUME.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume != self.MAX_VOLUME:
                self.__volume += 1
    
    def volume_down(self) -> None:
        """
        Decreases the volume by 1.
        Unmutes the television if it was muted.
        Only works if the television is powered on and volume is above MIN_VOLUME.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume != self.MIN_VOLUME:
                self.__volume -=1

    def __str__(self) -> str:
        """
        Returns the string representation of the television status,
        showing power status, current channel, and current volume (0 if muted).
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {0 if self.__muted else self.__volume}' 
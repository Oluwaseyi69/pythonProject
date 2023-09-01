class Television:
    def __init__(self):
        self.channel = 0
        self.volume_level = 0
        self.isOn = False

    def turn_on(self):
        self.isOn = True

    def turn_off(self):
        return self.isOn

    def get_channel(self):

            return self.channel


    def set_channel(self, channel):
        if self.channel < 0:
            raise ValueError ("Negative value cannot be set")
        self.channel = channel

    def set_volume(self, volume_level):
        if self.volume_level < 0:
            raise ValueError ("Negative value cannot be set")
        self.volume_level = volume_level

    def get_volume(self):
        return self.volume_level


    def channel_up(self):
        if self.isOn and self.channel < 100:
            self.channel += 1

    def channel_down(self):
        if self.isOn and self.channel < 100:
            self.channel -= 1

    def volume_up(self):
        if self.isOn and self.volume_level < 100:
            self.volume_level += 1

    def volume_down(self):
        if self.isOn and self.volume_level < 100:
            self.volume_level -= 1
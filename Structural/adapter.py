class Volt:
    def __init__(self, volt):
        self.volt = volt

    def get_volt(self):
        return self.volt

    def set_volt(self, volt):
        self.volt = volt


class Socket:
    def get_volt(self):
        return Volt(120)


class SocketClassAdapterImpl(Socket):
    def get_120volt(self):
        return self.get_volt()

    def get_12volt(self):
        v = self.get_volt()
        return self.convert_volt(v, 10)

    def get_3volt(self):
        v = self.get_volt()
        return self.convert_volt(v, 40)

    def convert_volt(self, v, i):
        return Volt(v.get_volt() / i)


def get_volt(sock_adapter, i):
    if i == 3:
        return sock_adapter.get_3volt()
    elif i == 12:
        return sock_adapter.get_12volt()
    elif i == 120:
        return sock_adapter.get_120volt()

    return sock_adapter.get_120volt()


if __name__ == '__main__':
    sock_adapter = SocketClassAdapterImpl()

    v3 = get_volt(sock_adapter, 3)
    v12 = get_volt(sock_adapter, 12)
    v120 = get_volt(sock_adapter, 120)

    print("v3 volts using Class Adapter=" + str(v3.get_volt()))
    print("v12 volts using Class Adapter=" + str(v12.get_volt()))
    print("v120 volts using Class Adapter=" + str(v120.get_volt()))

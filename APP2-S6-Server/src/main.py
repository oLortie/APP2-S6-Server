import socket

HOST_OLIVIER = "192.168.0.26"
HOST_PAUL = "10.0.0.141"
HOST = HOST_PAUL
PORT = 8888

#########################################
# !! Mapping !!
# Light: 2 bytes (0 à ~2500)
# Température: 2 bytes + 40 Celcius pour une étendue postive * 10 pour les dizièmes (-40 à 85 Celcius)
# Pression: 3 bytes en Pascal (300 à 1200 hPa)
# Direction du vent: 2 bytes * 10 pour les dizièmes (0 à 360 Degrés)
# Force du vent: 2 bytes (0 à ?? km/h)
# Pluie: 2 bytes (0 à ?? mm)
#########################################


if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                light = (data[0] << 8) | data[1]
                temperature = ((data[2] << 8) | data[3]) / 10 - 40
                pressure = ((data[4] << 16) | (data[5] << 8)) | data[6]
                windDirection = ((data[7] << 8) | data[8]) / 10
                windSpeed = (data[9] << 8) | data[10]
                rain = (data[11] << 8) | data[12]

                print("========= New Data =========")
                print("Light: {:.0f}".format(light))
                print("Temperature: {:.1f}".format(temperature))
                print("Pressure: {:.0f}".format(pressure))
                print("Wind Direction: {:.1f}".format(windDirection))
                print("Wind Speed: {:.0f}".format(windSpeed))
                print("Rain: {:.0f}".format(rain))

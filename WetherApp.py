import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class WetherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.City_Label = QLabel("Enter city name: ", self)
        self.City_Imput = QLineEdit(self)
        self.GetWether_Buton = QPushButton("Get Weather", self)
        self.Temperature_Label = QLabel(self)
        self.Emogie_Label = QLabel(self)
        self.Description_Label = QLabel(self)
        self.Layout()
        
        self.GetWether_Buton.clicked.connect(self.get_Wether)
        
    def Layout(self):
        self.setWindowTitle("Wether App")
        
        vBox = QVBoxLayout()
        vBox.addWidget(self.City_Label)
        vBox.addWidget(self.City_Imput)
        vBox.addWidget(self.GetWether_Buton)
        vBox.addWidget(self.Temperature_Label)
        vBox.addWidget(self.Emogie_Label)
        vBox.addWidget(self.Description_Label)
        
        self.setLayout(vBox)
        self.City_Label.setAlignment(Qt.AlignCenter)
        self.Temperature_Label.setAlignment(Qt.AlignCenter)
        self.Emogie_Label.setAlignment(Qt.AlignCenter)
        self.Description_Label.setAlignment(Qt.AlignCenter)
        
        self.City_Label.setObjectName("City_Label")
        self.City_Imput.setObjectName("City_Imput")
        self.GetWether_Buton.setObjectName("GetWether_Buton")
        self.Temperature_Label.setObjectName("Temperature_Label")
        self.Emogie_Label.setObjectName("Emogie_Label")
        self.Description_Label.setObjectName("Description_Label")
        
        self.setStyleSheet(""" 
                           QLabel, QPushButton{
                               font-family: calibri;
                           }
                           QLabel#City_Label{
                               font-size: 40px;
                               font-style: italic;
                           }
                           QLineEdit{
                               font-size: 40px;
                           }
                           QPushButton{
                               font-size: 30px;
                               font-weight: bold;
                           }
                           QLabel#Temperature_Label{
                               font-size: 75px;
                           }
                           QLabel#Emogie_Label{
                               font-size: 100px;
                               font-family: Segoe UI emoji;
                           }
                           QLabel#Description_Label{
                               font-size: 30px;
                           }
                           """)
        
    def get_Wether(self):
        api_key = "2a45a777e9b116fdb83219b342053f3f"
        city = self.City_Imput.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        
        try:
            responce = requests.get(url)
            responce.raise_for_status()
            
            data = responce.json()
            if data["cod"] == 200:
                self.display_Wether(data)
        
        except requests.exceptions.HTTPError:
            self.Temperature_Label.setText("There is no such city! \n Pleace check your imput")
        except requests.exceptions.RequestException:
            pass
                
    def display_Wether(self, data):
        print(data)
        nebo = data["weather"][0]["description"]
        self.Temperature_Label.setText(f"Temp: {round(int(data["main"]["temp"])-273.15, 2)} °C")
        self.Description_Label.setText(nebo)
        self.Emogie_Label.setText(self.get_Wether_emogie(data["weather"][0]["id"]))
        print(data["weather"][0]["id"])
        
    @staticmethod
    def get_Wether_emogie(Wether_id):
        if 200 >= Wether_id <= 232:
            return "⛈️"
        elif 300 >= Wether_id <= 321:
            return "🌦️"
        elif 500 >= Wether_id <= 531:
            return "🌧️"
        elif 600 >= Wether_id <= 622:
            return "🌨️"
        elif 701 >= Wether_id <= 771:
            return "🌫️"
        elif Wether_id ==781:
            return "🌪️"
        elif Wether_id == 800:
            return "☀️"
        else:
            return "⛅"
        
        
        
              
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WetherApp()
    window.show()
    sys.exit(app.exec_())
    
    
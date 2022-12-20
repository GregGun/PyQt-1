from PyQt6.QtWidgets import QWidget, QApplication, QLabel
import sys

# Eine Instanz von der Klasse QApplication erzeugen
app = QApplication(sys.argv)

# Fensterelement erzeugen und konfigurieren
window = QWidget()
window.setWindowTitle("Meine erste PyQt App!")
window.setGeometry(200, 200, 600, 300)

# Text einfügen
txt1 = QLabel("Hallo Welt!", parent=window)
txt1.move(250, 130)

txt2 = QLabel("Hallo Gregor!", parent=window)
txt2.move(250, 180)

window.show()
sys.exit(app.exec())
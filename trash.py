import os
import sys

from PyQt5 import QtCore, QtMultimedia

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


def main():
    filename = os.path.join(CURRENT_DIR, "fir.wav")

    app = QtCore.QCoreApplication(sys.argv)

    QtMultimedia.QSound.play(filename)


    # end in 5 seconds:
    QtCore.QTimer.singleShot(10000, app.quit)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
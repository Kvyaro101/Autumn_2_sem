'''Main functional file of the errors ui'''
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from calc_subpack import mean_value_loc, Variance_loc, errors_itself

value_data = []

class Error_calc(QtWidgets.QMainWindow):
    '''Provide work of the UI'''
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        '''Setup of the window appearance'''
        self.setWindowTitle('Measurment Errors')
        self.setWindowIcon(QIcon('window_icon.jpg'))
        self.ui.lineEdit.setPlaceholderText('Value')
        self.ui.lineEdit_2.setPlaceholderText('Here will be shown data')
        self.ui.lineEdit_6.setPlaceholderText('System Error')
        self.ui.lineEdit_3.setPlaceholderText('Await') #Mean Value
        self.ui.lineEdit_4.setPlaceholderText('Await') #Variance
        self.ui.lineEdit_5.setPlaceholderText('Await') #Random Error
        self.ui.lineEdit_7.setPlaceholderText('Await') #Error (sys+ran)
        self.ui.lineEdit_8.setPlaceholderText('Await') #Square Variance
        self.ui.lineEdit_9.setPlaceholderText('Await') #Relative Error
        self.ui.pushButton.clicked.connect(self.data_add)
        self.ui.pushButton_2.clicked.connect(self.calculate)

    def data_add(self):
        '''Method to add data to its list'''
        if self.ui.lineEdit.text() == '':
            pass
        else:
            value_data.append(float(self.ui.lineEdit.text()))
            self.ui.lineEdit.setText(str())
            self.ui.lineEdit_2.setText(str(value_data))

    def calculate(self):
        '''Method that initiate analysis of an input data'''
        studt_cf = float(self.ui.doubleSpinBox.text().replace(',','.'))
        syst_err = float(self.ui.lineEdit_6.text())
        self.ui.lineEdit_3.setText(str(mean_value_loc.find_mean(value_data))[:8])
        self.ui.lineEdit_4.setText(str(Variance_loc.find_variance(value_data))[:8])
        self.ui.lineEdit_5.setText(str(errors_itself.ran_err(studt_cf,value_data))[:8])
        self.ui.lineEdit_7.setText(str(errors_itself.tot_error(studt_cf,value_data,syst_err))[:8])
        self.ui.lineEdit_8.setText(str(Variance_loc.find_variance(value_data)**2)[:8])
        self.ui.lineEdit_9.setText(str(errors_itself.rel_error(studt_cf,value_data,syst_err))[:8])

app = QtWidgets.QApplication([])
application = Error_calc()
application.show()

sys.exit(app.exec())

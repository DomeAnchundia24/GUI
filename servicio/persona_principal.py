from PySide6 import QtGui
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox

from Dato.estudiante_dao import Estudiantedao
from Dominio.Docente import Docente
from Dominio.Estudiante import Estudiante
from UI.vtn_principal import Ui_vtn_principal


class PersonaPrincipal(QMainWindow):
  def __init__(self):
    super(PersonaPrincipal, self).__init__()
    self.ui = Ui_vtn_principal()
    self.ui.setupUi(self)
    self.ui.statusbar.showMessage('Bienvenido', 2000)
    self.ui.pBtton_Grabar.clicked.connect(self.Grabar)
    self.ui.pBtton_buscar_cedula.clicked.connect(self.buscar_x_cedula)
    self.ui.line_cedula.setValidator(QtGui.QIntValidator())

    correo_exp = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    validator = QRegularExpressionValidator(correo_exp, self)
    self.ui.line_email.setValidator(validator)

  def Grabar(self):
      tipo_persona = self.ui.cb_tipo_persona.currentText()
      if self.ui.line_nombre.text() == '' or self.ui.line_apellido.text() == ''\
              or len(self.ui.line_cedula.text()) < 10 or self.ui.line_email.text() == '':
         print('Completar Datos')
         QMessageBox.warning(self, 'Advertencia', 'Falta de llenar los datos obligatorios.')
      else:
        persona = None
        if tipo_persona == 'Docente':
          persona = Docente()
          persona.nombre = self.ui.line_nombre.text()
          persona.apellido = self.ui.line_apellido.text()
          persona.cedula = self.ui.line_cedula.text()
          persona.email = self.ui.line_email.text()
        else:
          persona = Estudiante()
          persona.nombre = self.ui.line_nombre.text()
          persona.apellido = self.ui.line_apellido.text()
          persona.cedula = self.ui.line_cedula.text()
          persona.email = self.ui.line_email.text()

          #insertar en la base de datos al estudiante
          respuesta = None
          Estudiantedao.insertar_estudiante(persona)
          try:
            respuesta =Estudiantedao.insertar_estudiante(persona)
          except Exception as e:
            print(e)

        #archivo = None
        #try:
          #  archivo = open('archivo.txt', mode='a')
          # archivo.write(persona.__str__())
        # archivo.write('\n')
        #except Exception as e:
        # print('No se pudo grabar.')
        #finally:
          # if archivo:
        # archivo.close()
      if respuesta['exito']:
        self.ui.line_nombre.setText('')
        self.ui.line_apellido.setText('')
        self.ui.line_cedula.setText('')
        self.ui.line_email.setText('')
        self.ui.statusbar.showMessage('Grabado con éxito, felicidades.', 2000)
      else:
        QMessageBox.critical(self, 'Error', respuesta['mensaje'])

  def buscar_x_cedula(self):
      cedula = self.ui.line_cedula.text()
      e = Estudiante(cedula=cedula)
      e = Estudiantedao.selecionar_por_cedula(e)
      print(e)
      self.ui.line_nombre.setText(e.nombre)
      self.ui.line_apellido.setText(e.apellido)
      self.ui.line_email.setText(e.email)
      self.ui.cb_tipo_persona.setCurrentText('Estudiante')

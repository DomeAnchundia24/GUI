from PySide6.QtWidgets import QMainWindow

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


  def Grabar(self):
    tipo_persona = self.ui.cb_tipo_persona.currentText()
    persona = None
    if tipo_persona == 'Docente':
      persona = Docente()
      persona.nombre = self.ui.line_nombre.text()
      persona.apellido = self.ui.line_apellido.text()
    else:
      persona = Estudiante()
      persona.nombre = self.ui.line_nombre.text()
      persona.apellido = self.ui.line_apellido.text()

    archivo = None
    try:
      archivo = open('archivo.txt', mode='a')
      archivo.write(persona.__str__())
      archivo.write('\n')
    except Exception as e:
      print('No se pudo grabar.')
    finally:
      if archivo:
        archivo.close()
    self.ui.line_nombre.setText('')
    self.ui.line_apellido.setText('')
    self.ui.statusbar.showMessage('Grabado con éxito, felicidades.', 2000)
    
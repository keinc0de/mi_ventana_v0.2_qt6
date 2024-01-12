#PyQt6 6.6.1 e24
import ctypes
from PyQt6 import QtCore, QtGui, QtWidgets


class _Ui_MiVentana(object):
    def setupUi(self, MiVentana):
        self._carga_iconos()
        MiVentana.setObjectName("MiVentana")
        MiVentana.resize(605, 344)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(MiVentana)
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.vly_principal = QtWidgets.QVBoxLayout()
        self.vly_principal.setSpacing(2)
        self.vly_principal.setObjectName("vly_principal")
        self.fm_top = QtWidgets.QFrame(parent=MiVentana)
        self.fm_top.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fm_top.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fm_top.setObjectName("fm_top")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fm_top)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_icono = QtWidgets.QPushButton(parent=self.fm_top)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        self.bt_icono.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(self.pix('T'), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_icono.setIcon(icon)
        self.bt_icono.setFlat(False)
        self.bt_icono.setObjectName("bt_icono")
        self.horizontalLayout.addWidget(self.bt_icono)
        self.fmi = QtWidgets.QFrame(parent=self.fm_top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fmi.sizePolicy().hasHeightForWidth())
        self.fmi.setSizePolicy(sizePolicy)
        self.fmi.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fmi.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fmi.setObjectName("fmi")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fmi)
        self.verticalLayout_5.setContentsMargins(2, 0, 2, 0)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.hly_top_izquierfa = QtWidgets.QHBoxLayout()
        self.hly_top_izquierfa.setObjectName("hly_top_izquierfa")
        self.verticalLayout_5.addLayout(self.hly_top_izquierfa)
        self.horizontalLayout.addWidget(self.fmi)
        self.lb_titulo = QtWidgets.QLabel(parent=self.fm_top)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        font.setBold(False)
        self.lb_titulo.setFont(font)
        self.lb_titulo.setObjectName("lb_titulo")
        self.horizontalLayout.addWidget(self.lb_titulo)
        self.lb_nota = QtWidgets.QLabel(parent=self.fm_top)
        self.lb_nota.setText("")
        self.lb_nota.setObjectName("lb_nota")
        self.horizontalLayout.addWidget(self.lb_nota)
        self.fmd = QtWidgets.QFrame(parent=self.fm_top)
        self.fmd.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fmd.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fmd.setObjectName("fmd")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fmd)
        self.verticalLayout_4.setContentsMargins(2, 0, 2, 0)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.hly_top_derecha = QtWidgets.QHBoxLayout()
        self.hly_top_derecha.setObjectName("hly_top_derecha")
        self.verticalLayout_4.addLayout(self.hly_top_derecha)
        self.horizontalLayout.addWidget(self.fmd)
        self.fm_bts = QtWidgets.QFrame(parent=self.fm_top)
        self.fm_bts.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fm_bts.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fm_bts.setObjectName("fm_bts")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.fm_bts)
        self.horizontalLayout_3.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bt_lock = QtWidgets.QPushButton(parent=self.fm_bts)
        self.bt_lock.setMinimumSize(QtCore.QSize(25, 18))
        self.bt_lock.setMaximumSize(QtCore.QSize(25, 18))
        self.bt_lock.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(self.pix('unlock'), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon1.addPixmap(self.pix('lock'), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.bt_lock.setIcon(icon1)
        self.bt_lock.setCheckable(True)
        self.bt_lock.setChecked(False)
        self.bt_lock.setFlat(False)
        self.bt_lock.setObjectName("bt_lock")
        self.horizontalLayout_2.addWidget(self.bt_lock)
        self.bt_min = QtWidgets.QPushButton(parent=self.fm_bts)
        self.bt_min.setMinimumSize(QtCore.QSize(25, 18))
        self.bt_min.setMaximumSize(QtCore.QSize(30, 18))
        self.bt_min.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(self.pix('min'), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_min.setIcon(icon2)
        self.bt_min.setIconSize(QtCore.QSize(14, 14))
        self.bt_min.setFlat(False)
        self.bt_min.setObjectName("bt_min")
        self.horizontalLayout_2.addWidget(self.bt_min)
        self.bt_mm = QtWidgets.QPushButton(parent=self.fm_bts)
        self.bt_mm.setMinimumSize(QtCore.QSize(25, 18))
        self.bt_mm.setMaximumSize(QtCore.QSize(30, 18))
        self.bt_mm.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(self.pix('vf'), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_mm.setIcon(icon3)
        self.bt_mm.setIconSize(QtCore.QSize(16, 16))
        self.bt_mm.setFlat(False)
        self.bt_mm.setObjectName("bt_mm")
        self.horizontalLayout_2.addWidget(self.bt_mm)
        self.bt_x = QtWidgets.QPushButton(parent=self.fm_bts)
        self.bt_x.setMinimumSize(QtCore.QSize(25, 18))
        self.bt_x.setMaximumSize(QtCore.QSize(30, 18))
        self.bt_x.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(self.pix('x'), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_x.setIcon(icon4)
        self.bt_x.setIconSize(QtCore.QSize(14, 14))
        self.bt_x.setFlat(False)
        self.bt_x.setObjectName("bt_x")
        self.horizontalLayout_2.addWidget(self.bt_x)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addWidget(self.fm_bts)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 10)
        self.horizontalLayout.setStretch(5, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.vly_principal.addWidget(self.fm_top)
        self.fm_contenido = QtWidgets.QFrame(parent=MiVentana)
        self.fm_contenido.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fm_contenido.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fm_contenido.setObjectName("fm_contenido")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.fm_contenido)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.vly_contenido = QtWidgets.QVBoxLayout()
        self.vly_contenido.setObjectName("vly_contenido")
        self.verticalLayout_6.addLayout(self.vly_contenido)
        self.vly_principal.addWidget(self.fm_contenido)
        self.vly_principal.setStretch(0, 1)
        self.vly_principal.setStretch(1, 20)
        self.verticalLayout_3.addLayout(self.vly_principal)

        self.horizontalLayout.setSpacing(0)

    def _carga_iconos(self):
        self.icos = {
            'x':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAdklEQVR4nGNgGGzgJRSTKgdR8
            PjF2f+PX5z9j0UhTjkmJAViMEEo+yURcnADMABMIbJmbIARzZl4FTMwMDDIShi/YmBgEMfmAnGoJNGa0
            Q0gCyAbQNAL6AGIbABWzdi8RHQswPxLKFyQAVkJCcMQPAoIJuWBAQBw1lo0OCl92gAAAABJRU5ErkJggg==''',
            'vf':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAtklEQVR4nJ2TvQ7CIBSFv5p2
            dWxJLG59AuKj+xSGN3CjJtSxaxPjYFEGLrachIF7OSf351AhYwQaITcDA0AlPJict21GHK3MA+hTAqPz
            9pQjRyL3QyIulZ3CsY4u0w7iF6GCyXnb/utbEggDu2plnqUVoJW5AF2xQClSAssO/pwS6LfMYjXSUAv5
            TisjWXkBXsAZohactzc+XginCfFovR3QBzL8/kLW+2tLyQ3FfyHnxN3r3Yw3Iak0XUaduYIAAAAASUVO
            RK5CYII=''',
            'vc':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAA4klEQVR4nGNkwAFMTU0/4ZJj
            YGBgOH36NB8DAwMDIy7N6zbP4MVnQJBvxufTp0/zYRgA08zCzHHJzytBEZvmTdsW3P/z94dekG/GZ6y2
            P35x9j8+LyCrYUEWZGBgYODj42MtyG5j4OPjY4WJwfyLDbAgOxtNjgOKGYJ8Mz7hMoSJmABbt3kGLy4v
            MeHTSAyg2AAWwkogADlQYdFIkgECAgIcC5Z2cTAwMDDA0sDp06f5iDbgw4cPP4J8M37D+LBYIdqAT58+
            /cYWlUynT5/mw5okkQDMudjk4HkBX9LFlxIpBgBLJWpdBnxuoAAAAABJRU5ErkJggg==''',
            'min':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAc0lEQVR4nO2QIQ6AMAxF/xo
            UXGBmdqmf5PyToJtZDBcA2WFYQkggwyH2VNP8/9IUaDT+gCmD934jIvMWLqhqTikNANABADPvIjIv6zT
            WCJwN8ez0VJa15XuWyknOhlgrcDZEVc3A5QfMvNcKAEBE+i/5Rw5cSCjBRfdVQwAAAABJRU5ErkJggg==''',
            'lock':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAmElEQVR4nLWTMQ6AIBAE94
            w9rY2v8BnyXHmGr7Cx9QVrwxkkHBISp4O7XWAvgKRDByQdSSfphohccbkZOp/3SqFpO859LannaQlqou
            QGKg5RAAA4zl3ra24yGFdVsQfg1aiEadDK+FG3wnxIMzDDy0lzqD5hnpYQm02qBkn6fQa19JsMWvh3jC
            1TEeD1OT7nHvGPpvc768E3wrY+kahZHnIAAAAASUVORK5CYII=''',
            'unlock':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAj0lEQVR4nKWT0Q2AIAxE
            T+MQ/jAFY8C4MoZT8EOcwh9qSOmZRu8P6D1IryywdZD9rDcWy1zbmSx32GPREA0Qc+kGAEBtp5wnDVnJ
            U8WcAWQBWbIAF602tKl1DnuUBk4N8wDcRgZg8VGNKdD4tMYkaApS2IupXgFD/t8Ab/m7AB79Blhz8MiT
            yvSZnBc/w3YDbPQiR/InLn4AAAAASUVORK5CYII=''',
            'T':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAA00lEQVR4nN2ToQrCUBiFvztmM
            C3uQSaIySIYBMOCRcuMSxabb2AxCRYFNdtsliUR3DtYF00LC79BhevmpsPm137uOYd7OfdXACJiA02gA
            lQpJgYSIFBKRebD3Bp6/mi/O9U+mAHouPXzcjWviMhBiUhv6Pnjb82pkKkSkb5tOdsy5ifRNRyYpN4cX
            cNjkcm2nIY2Vo08kS5MzzqZgDxh3tnbG5ThnwP0OouqNbn/7QxFbWjEBpC0u7XLF+IXOm79DCQGEKw3i
            0mZkMcezIBAwW/rfAOZJE71pbW/kwAAAABJRU5ErkJggg==''',
            'vacio16':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAEklEQVR4nGNgGAWjYBS
            MAggAAAQQAAFVN1rQAAAAAElFTkSuQmCC''',
            'cuadro i':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAeklEQVR4nO2TsQ2AIB
            BFH8YhaJjC0lgZK9nL3glMXAEWMLZMQcMYNiZKogF6Xn337xf3BA+GMjSAABin/tj2dSjZVrKzgBaA8c
            HNicEIH9wJLEp2ti2p+wo1PjgAmuzOP9SAGgCQ+4mRaPcrz3DLRMKHL94yfV7JQANc8+ceLyYfvbQAAA
            AASUVORK5CYII=''',
            'cuadro d':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAaUlEQVR4nGNkQIAtDK
            QBHwYGBgZGmObHL856k6JbVsJ4KwMDgw8jkuZKWQljG3SF+AyWlTDeyoLEsYE5CwkQ9BYT0W4eNWDUAD
            wAnhIfvzh7RFbCmNQMRX5mSojNO7x391E7RiQxsrIzAHfCHfDR5RURAAAAAElFTkSuQmCC''',
            'cuadro top':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAdElEQVR4nGNkQIAt
            DKQBHwYGBgZGmObHL856k6I7ITbv8N7dR+0YydEMA7ISxluZyNGIDEYNYGBggTFkJYy3kqIRFnMsaOI+
            ROqHJ7qBDwPqBeLjF2ePyEoYE5WhHr84e4SBgcGbgYGCzASNNR9GJDGysjMAV7Ug9ZWZ4x4AAAAASUVORK5CYII=''',
            'cuadro bot':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAcElEQVR4nGNkQIAt
            DKQBHwYGBgZGmObHL856k6JbVsJ4KwMDgw8jkuZKWQljG2I0P35x9ggDA0M71BCGLY9fnP3PQJoX4HqY
            SHE2NjDwBrCg8UmNSoQBpEYjDAx8GAwTA3wSYvMOk6oROTPBAFnZGQCo6iILBS3I0wAAAABJRU5ErkJggg==''',
            'folder':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAiUlEQVR4nGNgoBAwQunF
            DAwMgljk30PFffAZsPjxi7MxeCzZKithzIDLEBaYzbISxluxKXj84qw3AwPDZAYGhi1YpH0YGRgYtkAV
            kQxkJYy3MpGjkYGB4RWMQa4BYlD6PbkGwIAgpQaQ7YVhZAA8FuaQaYAgEwMkw6SQawgsN8LSOSz34QPI
            anwAXqYaALRP9w0AAAAASUVORK5CYII=''',
            'cuadro c':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAA1ElEQVR4nM2TsQrCMB
            RFT7UgCt0jkrW75CcE+y1+jL/h2n5G6N41iHETBF0dfNW02BKdvEvC456bkJeX8FbJdyoAkhZ23jZAFg
            lftTI5UCQBnGtlomjnLUCjlclTqWUCFzEBWpnSeZsBpEH9LmsNzGQ/7bE3YB14OwEZUDtvj8B24PCdVq
            YGzsAFYNIzLEZggL14XuoHfK3/C7gB1Yi/Es9LYReuwEZeuRkIWPFs4+FTwFzW9cgNQu+lE+C8RSsTNV
            DylYHuMJ1i4FZamSUyTK1+GucH2d02d/lbtfAAAAAASUVORK5CYII='''
        }
        return self.icos
    
    def pix(self, key):
        data = self.icos.get(key)
        px = QtGui.QPixmap()
        px.loadFromData(QtCore.QByteArray.fromBase64(str(data).encode("utf-8")))
        return px
    
class Operaciones:
    def __init__(self, ventana):
        self.ventana = ventana

    def obten_resolusion_pantalla(self):
        md = ctypes.windll.user32
        md.SetProcessDPIAware()
        return md.GetSystemMetrics(0), md.GetSystemMetrics(1)
    
    def mover(self, w, h, ub='no', barras=0, modx=0, mody=0):
        wp, hp = self.obten_resolusion_pantalla()
        if barras!=0:
            hp += barras
        if ub=='no':
            x, y = 0+modx, 0+mody
        elif ub=='ne':
            x, y = (wp-modx)-w, 0+mody
        elif ub=='so':
            x, y = 0+modx, (hp-mody)-h
        elif ub=='se':
            x, y = (wp-modx)-w, (hp-mody)-h
        elif ub=='ctop':
            x, y = wp//2-w//2, 0+mody
        elif ub=='cbot':
            x, y = wp//2-w//2, (hp-mody)-h
        elif ub=='c':
            x, y = wp//2-w//2, hp//2-h//2
        # PARA TKINTER
        # self.ventana.geometry(f"+{x}+{y}")
        # PARA QT
        self.ventana.move(x, y)


class Arriba(Operaciones):
    def __init__(self, ventana, w, h, barras=0, modx=0 ,mody=0):
        super().__init__(ventana=ventana)
        self.dc = {'w':w, 'h':h, 'barras':barras, 'modx':modx, 'mody':mody}

    def izquierda(self):
        self.mover(ub='no', **self.dc)

    def derecha(self):
        self.mover(ub='ne', **self.dc)

    def centrar(self):
        self.mover(ub='ctop', **self.dc)


class Abajo(Arriba):
    def __init__(self, ventana, w, h, barras, modx=0 ,mody=0):
        super().__init__(ventana, w, h, barras, modx ,mody)

    def izquierda(self):
        self.mover(ub='so', **self.dc)

    def derecha(self):
        self.mover(ub='se', **self.dc)

    def centrar(self):
        self.mover(ub='cbot', **self.dc)


class PosicionVentana:
    def __init__(self, ventana, w, h, barras=-60, modx=0, mody=0):
        self.ventana = ventana
        self.d = {
            'w':w, 'h':h,
            'barras':barras,
            'modx':modx, 'mody':mody
        }
        self.arriba = Arriba(ventana=self.ventana, **self.d)
        self.abajo = Abajo(ventana=self.ventana, **self.d)
        self.__op = Operaciones(self.ventana)

    def centrar(self):
        # coo = Operaciones(self.ventana)
        self.__op.mover(ub='c', **self.d)

    def obten_resolusion_pantalla(self):
        return self.__op.obten_resolusion_pantalla()

class MiVentana(QtWidgets.QWidget, _Ui_MiVentana):
    def __init__(self, **kwargs):
        super(MiVentana, self).__init__(**kwargs)
        self.setupUi(self)

        self._cse = []
        self._tam_cse = 16
        for x in range(4):
            gp = QtWidgets.QSizeGrip(self)
            gp.resize(self._tam_cse, self._tam_cse)
            ico = str(self.icos.get('vacio16')).encode("utf-8")
            gp.setStyleSheet(f'background:transparent;image:data("{ico}");')
            self._cse.append(gp)

        gm = self.geometry()
        self.posv = PosicionVentana(self, gm.width(), gm.height())
        self.MOD_TITULO = 11
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

        self.bt_x.clicked.connect(self._cerrar)
        self.bt_mm.clicked.connect(self._maximiza_minimiza)
        self.bt_min.clicked.connect(self.showMinimized)
        self.bt_lock.clicked.connect(self._on_top)
        self.__config_uno()
        self.ancho_alto(450, 250)

    def resizeEvent(self, e):
        rc = self.rect()
        self._cse[1].move(rc.right()-self._tam_cse, 0)
        self._cse[2].move(rc.right()-self._tam_cse, rc.bottom()-self._tam_cse)
        self._cse[3].move(0, rc.bottom()-self._tam_cse)

    def asigna_icono_a_boton(self, btn, icono, w=16, h=16):
        btn.setIcon(QtGui.QIcon(icono))
        btn.setIconSize(QtCore.QSize(w, h))

    def asigna_icono_al_programa(self, icono, **kwargs):
        self.asigna_icono_a_boton(self.bt_icono, icono, **kwargs)
        self.setWindowIcon(QtGui.QIcon(icono))

    def asigna_nombre_al_programa(self, nombre, fg="#F0EAD6", bg="#1D2440"):
        self.bt_icono.setStyleSheet(f"color:{fg}; background-color:{bg}")
        self.bt_icono.setText(nombre)
        self.bt_icono.setFixedWidth(len(nombre)*self.MOD_TITULO)

    def _cerrar(self):
        self.close()

    def _maximiza_minimiza(self):
        if self.isMaximized():
            self.showNormal()
            mg, ico = 0, self.pix('vf')
        else:
            self.showMaximized()
            mg, ico = 0, self.pix('vc')
        self.asigna_icono_a_boton(self.bt_mm, ico)
        self.setContentsMargins(0,mg,0,0)

    def asigna_color_barra(self, fg='#F0EAD6', bg='rgba(0,0,0,0)'):
        self.fm_top.setStyleSheet(f'background-color:{bg};color:{fg}')

    def _on_top(self):
        b = self.bt_lock.isChecked()
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint, b)
        self.showNormal()

    def mousePressEvent(self, e):
        if e.button()==QtCore.Qt.MouseButton.RightButton:
            self.cur_pos = e.globalPosition().toPoint()

    def mouseMoveEvent(self, e):
        if self.isMaximized():
            return
        try:
            if e.buttons()==QtCore.Qt.MouseButton.RightButton:
                self.np = QtCore.QPoint(e.globalPosition().toPoint() - self.cur_pos)
                x, y = self.cur_pos.x(), self.cur_pos.y()
                self.move(x+self.np.x(), y+self.np.y())
                self.cur_pos = e.globalPosition().toPoint()
        except Exception as err:
            print(err)

    def agrega_menu(self):
        self.menu_bt = QtWidgets.QMenu(self)
        self.menu_bt.addAction('&UNO', self.accion1)
        self.bt_icono.setMenu(self.menu_bt)

    def accion1(self):
        self.ajusta_derecha()

    def ajusta_derecha(self, proporcion=2/5):
        wp, hp = self.posv.obten_resolusion_pantalla()
        self.setGeometry(0,0, int(wp*proporcion), int(hp))

    def ajusta_izquierda(self, proporcion=2/5):
        wp, hp = self.posv.obten_resolusion_pantalla()
        gm = self.geometry()
        w, h = gm.width(), gm.height()
        self.setGeometry(wp-w,0, int(wp*proporcion), int(hp))

    def __config_uno(self):
        bg1 = '#1C1B24'
        self.asigna_nombre_al_programa('MI VENTANA 2',bg=bg1)
        self.asigna_color_barra(bg=bg1)
        self.setStyleSheet(f'background-color:{bg1};')
        self.asigna_icono_al_programa(self.pix('T'))

    def agrega_widget_a_la_barra_derecha(self, wg):
        self.hly_top_derecha.addWidget(wg)

    def ancho_alto(self, w, h):
        self.W = w
        self.H = h
        self.resize(self.W, self.H)

    def restaura(self):
        self.resize(self.W, self.H)
        self.posv.centrar()


if __name__=="__main__":
    import sys
    from PyQt6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    mvn = MiVentana()
    mvn.show()
    sys.exit(app.exec())
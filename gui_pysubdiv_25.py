from PyQt5.QtWidgets import QMessageBox, QInputDialog, QApplication, QWidget, QLineEdit, QFileDialog, QSizeGrip, QSlider
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import files
import os
import control_cage


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self, name_mesh=None, name_cage=None, path_mesh=[], path_cage=None,
                status_data_cage=None, parts_array = [], flip_mesh = None, flip_cage = [], iter_subdiv = None, def_vol = []):
        self.path_mesh = path_mesh
        self.name_mesh = name_mesh
        self.path_cage = path_cage
        self.name_cage = name_cage
        self.status_data_cage = status_data_cage
        self.part = parts_array
        self.flip_mesh = flip_mesh
        self.flip_cage = flip_cage
        self.iter_subdiv = iter_subdiv
        self.def_vol = def_vol

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setGeometry(1150, 612,751, 373)
        MainWindow.setWindowIcon(QIcon("image/cgre.PNG"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(751, 393))
        MainWindow.setMaximumSize(QtCore.QSize(751, 393))
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(751, 393))
        self.centralwidget.setMaximumSize(QtCore.QSize(751, 393))
        self.centralwidget.setStyleSheet("*{\n"
"    color: #000;\n"
"    border: none\n"
"}\n"
"\n"
"#leftMenu{\n"
"    background-color: #2596be;\n"
"}\n"
"\n"
"#mainBody{\n"
"    background-color: #eeeee4;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    background: transparent;\n"
"    border: 2px solid #2596be;\n"
"    color: #2596be;\n"
"}\n"
" \n"
"#searchFrame{\n"
"    border-radius: 10px;\n"
"    border: 2px solid #2596be;\n"
"}\n"
"\n"
"#searchFrame_2{\n"
"    border-radius: 10px;\n"
"    border: 2px solid #2596be;\n"
"}\n"
"\n"
"#searchFrame_3{\n"
"    border-radius: 10px;\n"
"    border: 2px solid #2596be;\n"
"}\n"
"\n"
"#searchFrame_4{\n"
"    border-radius: 10px;\n"
"    border: 2px solid #2596be;\n"
"}\n"
"\n"
"#appHeader{\n"
"    color: #2596be;\n"
"}\n"
"\n"
"#searchFile{\n"
"    color: #2596be;\n"
"}\n"
"\n"
"#searchFile_2{\n"
"    color: #2596be;\n"
"}\n"
"\n"
"#searchFile_3{\n"
"    color: #2596be;\n"
"}\n"
"\n"
"#searchFile_4{\n"
"    color: #2596be;\n"
"}\n"
"\n"
"#statusData{\n"
"    color: #2596be;\n"
"}\n"
"\n"
"#statusData_2{\n"
"    color: #2596be;\n"
"}\n"
"\n"
"#butInspect{\n"
"    background-color: #2596be;\n"
"    color: #fff;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#butOptimizer{\n"
"    background-color: #daffb7;\n"
"    color: #00000;\n"
"    border-radius: 3px;\n"
"    border-color: #00000;\n"
"}\n"
"\n"
"#butSingCC{\n"
"    background-color: #2596be;\n"
"    color: #fff;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#butMeshStatus{\n"
"    background-color: #2596be;\n"
"    color: #fff;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#butGmesh{\n"
"    background-color: #daffb7;\n"
"    color: #00000;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#butCageStatus{\n"
"    background-color: #2596be;\n"
"    color: #fff;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"\n"
"#butMulCC{\n"
"    background-color: #2596be;\n"
"    color: #fff;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#butInstructionCC{\n"
"    background-color: #000000;\n"
"    color: #fff;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#butInstructionIns{\n"
"    background-color: #000000;\n"
"    color: #fff;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#butInstructionInt{\n"
"    background-color: #000000;\n"
"    color: #fff;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#butdef_vol{\n"
"    background-color: #2596be;\n"
"    color: #fff;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#butVol_info{\n"
"    background-color: #000000;\n"
"    color: #fff;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#butIntVis{\n"
"    background-color: #2596be;\n"
"    color: #fff;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#butMesh{\n"
"    background-color: #2596be;\n"
"    color: #fff;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#butSubMulCC{\n"
"    background-color: #2596be;\n"
"    color: #fff;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#butSubSinCC{\n"
"    background-color: #2596be;\n"
"    color: #fff;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#butSubInt{\n"
"    background-color: #2596be;\n"
"    color: #fff;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#butExport{\n"
"    background-color: #2596be;\n"
"    color: #fff;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#butExport_2{\n"
"    background-color: #2596be;\n"
"    color: #fff;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#butPrevious{\n"
"    background-color: #000000;\n"
"    color: #fff;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#butPrevious_2{\n"
"    background-color: #000000;\n"
"    color: #fff;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#butReset{\n"
"    background-color: #2596be;\n"
"    color: #fff;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#butStatus_3{\n"
"    background-color: #2596be;\n"
"    color: #fff;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#frameCrease{\n"
"    border-radius: 10px;\n"
"    border: 2px solid #2596be;\n"
"}\n"
"\n"
"#frameGeodesic{\n"
"    border-radius: 10px;\n"
"    border: 2px solid #2596be;\n"
"}\n"
"\n"
"#frameVolume{\n"
"    border-radius: 10px;\n"
"    border: 2px solid #2596be;\n"
"}\n"
"\n"
"#frameCrease{\n"
"    border-radius: 10px;\n"
"    border: 2px solid #2596be;\n"
"}\n"
"\n"
"#frameMesh{\n"
"    border-radius: 10px;\n"
"    border: 2px solid #2596be;\n"
"}\n"
"\n"
"#frameCrease{\n"
"    border-radius: 10px;\n"
"    border: 2px solid #2596be;\n"
"}\n"
"\n"
"#frame_27{\n"
"    border-radius: 10px;\n"
"    border: 2px solid #2596be;\n"
"}\n"
"\n"
"#frame_ins{\n"
"    border-radius: 10px;\n"
"    border: 2px solid #2596be;\n"
"}\n"
"\n"
"#frame_MultCC{\n"
"    border-radius: 10px;\n"
"    border: 2px solid #2596be;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.mainBody = QtWidgets.QWidget(self.centralwidget)
        self.mainBody.setGeometry(QtCore.QRect(0, 0, 751, 373))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        self.mainBody.setMinimumSize(QtCore.QSize(751, 373))
        self.mainBody.setMaximumSize(QtCore.QSize(751, 373))
        self.mainBody.setStyleSheet("#mainBody{\n"
"    background-color: #eeeee4;\n"
"}")
        self.mainBody.setObjectName("mainBody")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainBody)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerFrame = QtWidgets.QWidget(self.mainBody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headerFrame.sizePolicy().hasHeightForWidth())
        self.headerFrame.setSizePolicy(sizePolicy)
        self.headerFrame.setMinimumSize(QtCore.QSize(736, 65))
        self.headerFrame.setMaximumSize(QtCore.QSize(736, 65))
        self.headerFrame.setObjectName("headerFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.headerFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.headerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.menuBtn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuBtn.sizePolicy().hasHeightForWidth())
        self.menuBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.menuBtn.setFont(font)
        self.menuBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/blue_ocean/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QtCore.QSize(32, 32))
        self.menuBtn.setObjectName("menuBtn")
        self.horizontalLayout_5.addWidget(self.menuBtn)
        self.appHeader = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.appHeader.sizePolicy().hasHeightForWidth())
        self.appHeader.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.appHeader.setFont(font)
        self.appHeader.setObjectName("appHeader")
        self.horizontalLayout_5.addWidget(self.appHeader)
        self.horizontalLayout.addWidget(self.widget, 0, QtCore.Qt.AlignLeft)
        self.widget_17 = QtWidgets.QWidget(self.headerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy)
        self.widget_17.setObjectName("widget_17")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_17)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.searchFrame_3 = QtWidgets.QFrame(self.widget_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchFrame_3.sizePolicy().hasHeightForWidth())
        self.searchFrame_3.setSizePolicy(sizePolicy)
        self.searchFrame_3.setMinimumSize(QtCore.QSize(170, 36))
        self.searchFrame_3.setMaximumSize(QtCore.QSize(170, 36))
        self.searchFrame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searchFrame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searchFrame_3.setObjectName("searchFrame_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.searchFrame_3)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.searchFrame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(30, 30))
        self.label_7.setMaximumSize(QtCore.QSize(30, 30))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("icons/blue_ocean/search.svg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.searchFile_3 = QtWidgets.QPushButton(self.searchFrame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchFile_3.sizePolicy().hasHeightForWidth())
        self.searchFile_3.setSizePolicy(sizePolicy)
        self.searchFile_3.setMinimumSize(QtCore.QSize(116, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.searchFile_3.setFont(font)
        self.searchFile_3.setObjectName("searchFile_3")
        self.horizontalLayout_9.addWidget(self.searchFile_3)
        self.horizontalLayout_7.addWidget(self.searchFrame_3)
        self.searchFrame_4 = QtWidgets.QFrame(self.widget_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchFrame_4.sizePolicy().hasHeightForWidth())
        self.searchFrame_4.setSizePolicy(sizePolicy)
        self.searchFrame_4.setMinimumSize(QtCore.QSize(40, 36))
        self.searchFrame_4.setMaximumSize(QtCore.QSize(168, 36))
        self.searchFrame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searchFrame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searchFrame_4.setObjectName("searchFrame_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.searchFrame_4)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.searchFrame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(30, 30))
        self.label_11.setMaximumSize(QtCore.QSize(30, 30))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("icons/blue_ocean/search.svg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        self.searchFile_4 = QtWidgets.QPushButton(self.searchFrame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchFile_4.sizePolicy().hasHeightForWidth())
        self.searchFile_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.searchFile_4.setFont(font)
        self.searchFile_4.setObjectName("searchFile_4")
        self.horizontalLayout_10.addWidget(self.searchFile_4, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_7.addWidget(self.searchFrame_4, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.widget_17)
        self.widget_3 = QtWidgets.QWidget(self.headerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(50, 0))
        self.widget_3.setSizeIncrement(QtCore.QSize(50, 0))
        self.widget_3.setBaseSize(QtCore.QSize(50, 0))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(30, 30))
        self.label_9.setMaximumSize(QtCore.QSize(30, 30))
        self.label_9.setSizeIncrement(QtCore.QSize(30, 30))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("icons/blue_ocean/file-text.svg"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.frame_6 = QtWidgets.QFrame(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(105, 0))
        self.frame_6.setMaximumSize(QtCore.QSize(111, 16777215))
        self.frame_6.setSizeIncrement(QtCore.QSize(80, 0))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setContentsMargins(-1, 1, -1, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.statusData = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusData.sizePolicy().hasHeightForWidth())
        self.statusData.setSizePolicy(sizePolicy)
        self.statusData.setMinimumSize(QtCore.QSize(73, 14))
        self.statusData.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.statusData.setFont(font)
        self.statusData.setObjectName("statusData")
        self.verticalLayout_9.addWidget(self.statusData)
        self.butMeshStatus = QtWidgets.QPushButton(self.frame_6)
        self.butMeshStatus.setMinimumSize(QtCore.QSize(95, 16))
        self.butMeshStatus.setMaximumSize(QtCore.QSize(95, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.butMeshStatus.setFont(font)
        self.butMeshStatus.setObjectName("butMeshStatus")
        self.verticalLayout_9.addWidget(self.butMeshStatus)
        self.butCageStatus = QtWidgets.QPushButton(self.frame_6)
        self.butCageStatus.setMinimumSize(QtCore.QSize(95, 16))
        self.butCageStatus.setMaximumSize(QtCore.QSize(95, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.butCageStatus.setFont(font)
        self.butCageStatus.setObjectName("butCageStatus")
        self.verticalLayout_9.addWidget(self.butCageStatus)
        self.horizontalLayout_4.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.widget_3, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.headerFrame, 0, QtCore.Qt.AlignLeft)
        self.cardsFrame = QtWidgets.QWidget(self.mainBody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(250)
        sizePolicy.setHeightForWidth(self.cardsFrame.sizePolicy().hasHeightForWidth())
        self.cardsFrame.setSizePolicy(sizePolicy)
        self.cardsFrame.setMinimumSize(QtCore.QSize(746, 240))
        self.cardsFrame.setMaximumSize(QtCore.QSize(746, 240))
        self.cardsFrame.setSizeIncrement(QtCore.QSize(0, 250))
        self.cardsFrame.setBaseSize(QtCore.QSize(0, 250))
        self.cardsFrame.setObjectName("cardsFrame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.cardsFrame)
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget_6 = QtWidgets.QWidget(self.cardsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(250)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMinimumSize(QtCore.QSize(267, 250))
        self.widget_6.setMaximumSize(QtCore.QSize(267, 250))
        self.widget_6.setSizeIncrement(QtCore.QSize(0, 250))
        self.widget_6.setBaseSize(QtCore.QSize(0, 250))
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.butSingCC = QtWidgets.QPushButton(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butSingCC.sizePolicy().hasHeightForWidth())
        self.butSingCC.setSizePolicy(sizePolicy)
        self.butSingCC.setMinimumSize(QtCore.QSize(240, 22))
        self.butSingCC.setMaximumSize(QtCore.QSize(240, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.butSingCC.setFont(font)
        self.butSingCC.setAutoFillBackground(False)
        self.butSingCC.setObjectName("butSingCC")
        self.verticalLayout_4.addWidget(self.butSingCC, 0, QtCore.Qt.AlignHCenter)
        self.frameCrease = QtWidgets.QFrame(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameCrease.sizePolicy().hasHeightForWidth())
        self.frameCrease.setSizePolicy(sizePolicy)
        self.frameCrease.setMinimumSize(QtCore.QSize(245, 210))
        self.frameCrease.setMaximumSize(QtCore.QSize(245, 210))
        self.frameCrease.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCrease.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCrease.setObjectName("frameCrease")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frameCrease)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_14 = QtWidgets.QWidget(self.frameCrease)
        self.widget_14.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_14.setObjectName("widget_14")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget_14)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.widget_23 = QtWidgets.QWidget(self.widget_14)
        self.widget_23.setMaximumSize(QtCore.QSize(16777215, 91))
        self.widget_23.setObjectName("widget_23")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.widget_23)
        self.verticalLayout_14.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_16 = QtWidgets.QLabel(self.widget_23)
        self.label_16.setMinimumSize(QtCore.QSize(0, 45))
        self.label_16.setMaximumSize(QtCore.QSize(200, 44))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_14.addWidget(self.label_16)
        self.widget_24 = QtWidgets.QWidget(self.widget_23)
        self.widget_24.setObjectName("widget_24")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.widget_24)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(5)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.widget_24)
        self.lineEdit_14.setMinimumSize(QtCore.QSize(45, 32))
        self.lineEdit_14.setMaximumSize(QtCore.QSize(45, 35))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.horizontalLayout_19.addWidget(self.lineEdit_14)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.widget_24)
        self.lineEdit_15.setMinimumSize(QtCore.QSize(45, 35))
        self.lineEdit_15.setMaximumSize(QtCore.QSize(45, 35))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.horizontalLayout_19.addWidget(self.lineEdit_15)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.widget_24)
        self.lineEdit_16.setMinimumSize(QtCore.QSize(45, 35))
        self.lineEdit_16.setMaximumSize(QtCore.QSize(45, 35))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.horizontalLayout_19.addWidget(self.lineEdit_16)
        self.verticalLayout_14.addWidget(self.widget_24)
        self.verticalLayout_13.addWidget(self.widget_23)
        self.widget_26 = QtWidgets.QWidget(self.widget_14)
        self.widget_26.setMaximumSize(QtCore.QSize(16777215, 61))
        self.widget_26.setObjectName("widget_26")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_26)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_20 = QtWidgets.QLabel(self.widget_26)
        self.label_20.setMinimumSize(QtCore.QSize(148, 24))
        self.label_20.setMaximumSize(QtCore.QSize(148, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_2.addWidget(self.label_20)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.widget_26)
        self.lineEdit_18.setMinimumSize(QtCore.QSize(45, 35))
        self.lineEdit_18.setMaximumSize(QtCore.QSize(45, 35))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.horizontalLayout_2.addWidget(self.lineEdit_18)
        self.verticalLayout_13.addWidget(self.widget_26)
        self.verticalLayout_5.addWidget(self.widget_14)
        self.butInstructionCC = QtWidgets.QPushButton(self.frameCrease)
        self.butInstructionCC.setMinimumSize(QtCore.QSize(110, 18))
        self.butInstructionCC.setMaximumSize(QtCore.QSize(110, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.butInstructionCC.setFont(font)
        self.butInstructionCC.setObjectName("butInstructionCC")
        self.verticalLayout_5.addWidget(self.butInstructionCC, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addWidget(self.frameCrease)
        self.horizontalLayout_6.addWidget(self.widget_6)
        self.widget_8 = QtWidgets.QWidget(self.cardsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(250)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setMinimumSize(QtCore.QSize(267, 250))
        self.widget_8.setMaximumSize(QtCore.QSize(267, 250))
        self.widget_8.setSizeIncrement(QtCore.QSize(0, 250))
        self.widget_8.setBaseSize(QtCore.QSize(0, 250))
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.butIntVis = QtWidgets.QPushButton(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butIntVis.sizePolicy().hasHeightForWidth())
        self.butIntVis.setSizePolicy(sizePolicy)
        self.butIntVis.setMinimumSize(QtCore.QSize(240, 0))
        self.butIntVis.setMaximumSize(QtCore.QSize(240, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.butIntVis.setFont(font)
        self.butIntVis.setObjectName("butIntVis")
        self.verticalLayout_6.addWidget(self.butIntVis, 0, QtCore.Qt.AlignHCenter)
        self.frameVolume = QtWidgets.QFrame(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameVolume.sizePolicy().hasHeightForWidth())
        self.frameVolume.setSizePolicy(sizePolicy)
        self.frameVolume.setMinimumSize(QtCore.QSize(245, 210))
        self.frameVolume.setMaximumSize(QtCore.QSize(245, 210))
        self.frameVolume.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameVolume.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameVolume.setObjectName("frameVolume")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frameVolume)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.widget_5 = QtWidgets.QWidget(self.frameVolume)
        self.widget_5.setMinimumSize(QtCore.QSize(241, 195))
        self.widget_5.setMaximumSize(QtCore.QSize(241, 195))
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_10 = QtWidgets.QWidget(self.widget_5)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_17 = QtWidgets.QLabel(self.widget_10)
        self.label_17.setMaximumSize(QtCore.QSize(185, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_17.addWidget(self.label_17)
        self.horizontalSlider = QtWidgets.QSlider(self.widget_10)
        self.horizontalSlider.setMaximum(3)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_17.addWidget(self.horizontalSlider)
        self.verticalLayout_7.addWidget(self.widget_10)
        self.widget_16 = QtWidgets.QWidget(self.widget_5)
        self.widget_16.setObjectName("widget_16")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.widget_16)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_19 = QtWidgets.QLabel(self.widget_16)
        self.label_19.setMaximumSize(QtCore.QSize(132, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_18.addWidget(self.label_19)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.widget_16)
        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setMaximum(10)
        self.horizontalSlider_2.setSingleStep(1)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.verticalLayout_18.addWidget(self.horizontalSlider_2)
        self.verticalLayout_7.addWidget(self.widget_16)
        self.butInstructionInt = QtWidgets.QPushButton(self.widget_5)
        self.butInstructionInt.setMinimumSize(QtCore.QSize(110, 18))
        self.butInstructionInt.setMaximumSize(QtCore.QSize(110, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.butInstructionInt.setFont(font)
        self.butInstructionInt.setObjectName("butInstructionInt")
        self.verticalLayout_7.addWidget(self.butInstructionInt, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_21.addWidget(self.widget_5)
        self.verticalLayout_6.addWidget(self.frameVolume)
        self.horizontalLayout_6.addWidget(self.widget_8)
        self.widget_2 = QtWidgets.QWidget(self.cardsFrame)
        self.widget_2.setMinimumSize(QtCore.QSize(192, 240))
        self.widget_2.setMaximumSize(QtCore.QSize(192, 240))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.butInspect = QtWidgets.QPushButton(self.widget_2)
        self.butInspect.setMinimumSize(QtCore.QSize(140, 22))
        self.butInspect.setMaximumSize(QtCore.QSize(140, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.butInspect.setFont(font)
        self.butInspect.setAutoFillBackground(False)
        self.butInspect.setObjectName("butInspect")
        self.verticalLayout_3.addWidget(self.butInspect, 0, QtCore.Qt.AlignHCenter)
        self.frame_ins = QtWidgets.QFrame(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_ins.sizePolicy().hasHeightForWidth())
        self.frame_ins.setSizePolicy(sizePolicy)
        self.frame_ins.setMinimumSize(QtCore.QSize(170, 125))
        self.frame_ins.setMaximumSize(QtCore.QSize(170, 135))
        self.frame_ins.setSizeIncrement(QtCore.QSize(170, 0))
        self.frame_ins.setBaseSize(QtCore.QSize(170, 0))
        self.frame_ins.setObjectName("frame_ins")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_ins)
        self.verticalLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.butFaces = QtWidgets.QPushButton(self.frame_ins)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.butFaces.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/blue_ocean/triangle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butFaces.setIcon(icon1)
        self.butFaces.setObjectName("butFaces")
        self.verticalLayout_2.addWidget(self.butFaces, 0, QtCore.Qt.AlignLeft)
        self.butVertices = QtWidgets.QPushButton(self.frame_ins)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.butVertices.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/blue_ocean/stop-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butVertices.setIcon(icon2)
        self.butVertices.setObjectName("butVertices")
        self.verticalLayout_2.addWidget(self.butVertices, 0, QtCore.Qt.AlignLeft)
        self.butStatus = QtWidgets.QPushButton(self.frame_ins)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.butStatus.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/blue_ocean/book-open.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butStatus.setIcon(icon3)
        self.butStatus.setObjectName("butStatus")
        self.verticalLayout_2.addWidget(self.butStatus, 0, QtCore.Qt.AlignLeft)
        self.butInstructionIns = QtWidgets.QPushButton(self.frame_ins)
        self.butInstructionIns.setMinimumSize(QtCore.QSize(110, 18))
        self.butInstructionIns.setMaximumSize(QtCore.QSize(110, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.butInstructionIns.setFont(font)
        self.butInstructionIns.setObjectName("butInstructionIns")
        self.verticalLayout_2.addWidget(self.butInstructionIns, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.frame_ins, 0, QtCore.Qt.AlignHCenter)
        self.widget_9 = QtWidgets.QWidget(self.widget_2)
        self.widget_9.setMinimumSize(QtCore.QSize(170, 81))
        self.widget_9.setMaximumSize(QtCore.QSize(170, 81))
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.butdef_vol = QtWidgets.QPushButton(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butdef_vol.sizePolicy().hasHeightForWidth())
        self.butdef_vol.setSizePolicy(sizePolicy)
        self.butdef_vol.setMinimumSize(QtCore.QSize(170, 22))
        self.butdef_vol.setMaximumSize(QtCore.QSize(170, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.butdef_vol.setFont(font)
        self.butdef_vol.setObjectName("butdef_vol")
        self.verticalLayout_10.addWidget(self.butdef_vol)
        self.frame_27 = QtWidgets.QFrame(self.widget_9)
        self.frame_27.setMaximumSize(QtCore.QSize(170, 41))
        self.frame_27.setSizeIncrement(QtCore.QSize(170, 41))
        self.frame_27.setObjectName("frame_27")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_27)
        self.horizontalLayout_8.setContentsMargins(2, 1, 2, 1)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.butVol_info = QtWidgets.QPushButton(self.frame_27)
        self.butVol_info.setMinimumSize(QtCore.QSize(110, 18))
        self.butVol_info.setMaximumSize(QtCore.QSize(110, 18))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.butVol_info.setFont(font)
        self.butVol_info.setObjectName("butVol_info")
        self.horizontalLayout_8.addWidget(self.butVol_info)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.frame_27)
        self.lineEdit_20.setMinimumSize(QtCore.QSize(41, 27))
        self.lineEdit_20.setMaximumSize(QtCore.QSize(41, 27))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_20.setFont(font)
        self.lineEdit_20.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.horizontalLayout_8.addWidget(self.lineEdit_20)
        self.verticalLayout_10.addWidget(self.frame_27)
        self.verticalLayout_3.addWidget(self.widget_9)
        self.horizontalLayout_6.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.cardsFrame, 0, QtCore.Qt.AlignLeft)
        self.widget_4 = QtWidgets.QWidget(self.mainBody)
        self.widget_4.setMinimumSize(QtCore.QSize(744, 30))
        self.widget_4.setMaximumSize(QtCore.QSize(744, 30))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.butPrevious_2 = QtWidgets.QPushButton(self.widget_4)
        self.butPrevious_2.setMinimumSize(QtCore.QSize(140, 18))
        self.butPrevious_2.setMaximumSize(QtCore.QSize(140, 18))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.butPrevious_2.setFont(font)
        self.butPrevious_2.setMouseTracking(True)
        self.butPrevious_2.setTabletTracking(True)
        self.butPrevious_2.setObjectName("butPrevious_2")
        self.horizontalLayout_3.addWidget(self.butPrevious_2)
        self.butPrevious = QtWidgets.QPushButton(self.widget_4)
        self.butPrevious.setMinimumSize(QtCore.QSize(140, 18))
        self.butPrevious.setMaximumSize(QtCore.QSize(140, 18))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.butPrevious.setFont(font)
        self.butPrevious.setMouseTracking(True)
        self.butPrevious.setTabletTracking(True)
        self.butPrevious.setObjectName("butPrevious")
        self.horizontalLayout_3.addWidget(self.butPrevious)
        self.butExport_2 = QtWidgets.QPushButton(self.widget_4)
        self.butExport_2.setMinimumSize(QtCore.QSize(140, 18))
        self.butExport_2.setMaximumSize(QtCore.QSize(140, 18))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.butExport_2.setFont(font)
        self.butExport_2.setObjectName("butExport_2")
        self.horizontalLayout_3.addWidget(self.butExport_2)
        self.butExport = QtWidgets.QPushButton(self.widget_4)
        self.butExport.setMinimumSize(QtCore.QSize(140, 18))
        self.butExport.setMaximumSize(QtCore.QSize(140, 18))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.butExport.setFont(font)
        self.butExport.setObjectName("butExport")
        self.horizontalLayout_3.addWidget(self.butExport)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_19.setMinimumSize(QtCore.QSize(126, 19))
        self.lineEdit_19.setMaximumSize(QtCore.QSize(39, 19))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_19.setFont(font)
        self.lineEdit_19.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.horizontalLayout_3.addWidget(self.lineEdit_19)
        self.verticalLayout.addWidget(self.widget_4, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.widget_7 = QtWidgets.QWidget(self.mainBody)
        self.widget_7.setMinimumSize(QtCore.QSize(670, 30))
        self.widget_7.setMaximumSize(QtCore.QSize(738, 30))
        self.widget_7.setObjectName("widget_7")
        self.label_10 = QtWidgets.QLabel(self.widget_7)
        self.label_10.setGeometry(QtCore.QRect(0, 2, 330, 26))
        self.label_10.setMinimumSize(QtCore.QSize(330, 26))
        self.label_10.setMaximumSize(QtCore.QSize(330, 26))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.butOptimizer = QtWidgets.QPushButton(self.widget_7)
        self.butOptimizer.setGeometry(QtCore.QRect(440, 4, 139, 22))
        self.butOptimizer.setMinimumSize(QtCore.QSize(139, 22))
        self.butOptimizer.setMaximumSize(QtCore.QSize(145, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.butOptimizer.setFont(font)
        self.butOptimizer.setObjectName("butOptimizer")
        self.butGmesh = QtWidgets.QPushButton(self.widget_7)
        self.butGmesh.setGeometry(QtCore.QRect(590, 4, 144, 22))
        self.butGmesh.setMinimumSize(QtCore.QSize(144, 22))
        self.butGmesh.setMaximumSize(QtCore.QSize(144, 22))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.butGmesh.setFont(font)
        self.butGmesh.setObjectName("butGmesh")
        self.verticalLayout.addWidget(self.widget_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # INSPECTION BUTTON
        self.butInspect.clicked.connect(self.show_inspect)
        self.butVertices.clicked.connect(self.inspect_vertices)
        self.butFaces.clicked.connect(self.inspect_faces)
        self.butStatus.clicked.connect(self.status_popup)

        # INTERACTIVE VISUAL BUTTON
        self.butIntVis.clicked.connect(self.vis_mesh)
        self.horizontalSlider.valueChanged.connect(lambda v: self.slide_value(str(v)))
        self.horizontalSlider_2.valueChanged.connect(lambda v: self.slide_value_2(str(v / 10)))

        # MULTI CAGE BUTTON
        self.butSingCC.clicked.connect(self.mulcage)
        self.lineEdit_14.textChanged.connect(self.auto_submit_vert1)
        self.lineEdit_15.textChanged.connect(self.auto_submit_vert2)
        self.lineEdit_16.textChanged.connect(self.auto_submit_vert3)
        self.lineEdit_18.textChanged.connect(self.auto_submit_meshindex)

        # MULTI FILE BUTTON
        self.searchFile_3.clicked.connect(self.data_input_cage)
        self.searchFile_4.clicked.connect(self.data_input_mesh)

        # IMPORTED DATA
        self.butMeshStatus.clicked.connect(self.info_mesh)
        self.butCageStatus.clicked.connect(self.info_cage)

        # INSTRUCTION
        self.butInstructionCC.clicked.connect(self.inst_cc)
        self.butInstructionInt.clicked.connect(self.inst_int)
        self.butInstructionIns.clicked.connect(self.inst_ins)
        self.butVol_info.clicked.connect(self.inst_defvol)

        # PREVIOUS DATA
        self.butPrevious_2.clicked.connect(self.flip_cc)
        # self.butPrevious_2.clicked.connect(self.previous_mesh)
        self.butPrevious.clicked.connect(self.flip_vismesh)

        # EXPORT DATA
        self.butExport.clicked.connect(self.export_cage)
        self.butExport_2.clicked.connect(self.export_mesh)

        # MESH OPTIMIZER
        self.butOptimizer.clicked.connect(self.opt_mesh)

        # DEFINE VOLUME
        self.butdef_vol.clicked.connect(self.define_vol)
        self.lineEdit_20.textChanged.connect(self.auto_submit_defvol)

        # FINITE ELEMENT ANALYSIS
        self.butGmesh.clicked.connect(self.gmesh)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PySubDiv"))
        self.appHeader.setText(_translate("MainWindow", "PySubDiv"))
        self.searchFile_3.setText(_translate("MainWindow", "Cage .OBJ File"))
        self.searchFile_4.setText(_translate("MainWindow", "Mesh .OBJ File"))
        self.statusData.setText(_translate("MainWindow", "Active Data"))
        self.butMeshStatus.setText(_translate("MainWindow", "Mesh Empty"))
        self.butCageStatus.setText(_translate("MainWindow", "Cage Empty"))
        self.butSingCC.setText(_translate("MainWindow", "Create Control Cage"))
        self.label_16.setText(_translate("MainWindow", "Input Vertices:"))
        self.label_20.setText(_translate("MainWindow", "Mesh Confirmation:"))
        self.butInstructionCC.setText(_translate("MainWindow", "Instruction"))
        self.butIntVis.setText(_translate("MainWindow", "Interactive Visualization"))
        self.label_17.setText(_translate("MainWindow", "Subdivision Iteration: "))
        self.label_19.setText(_translate("MainWindow", "Sharpness: "))
        self.butInstructionInt.setText(_translate("MainWindow", "Instruction"))
        self.butInspect.setText(_translate("MainWindow", "Inspection"))
        self.butFaces.setText(_translate("MainWindow", "Inspect Faces"))
        self.butVertices.setText(_translate("MainWindow", "Inspect Vertices"))
        self.butStatus.setText(_translate("MainWindow", "Saved Status"))
        self.butInstructionIns.setText(_translate("MainWindow", "Instruction"))
        self.butdef_vol.setText(_translate("MainWindow", "Define Volume"))
        self.butVol_info.setText(_translate("MainWindow", "Vol. Confirmation"))
        self.butPrevious_2.setText(_translate("MainWindow", "Finalize Cage"))
        self.butPrevious.setText(_translate("MainWindow", "Finalize Mesh"))
        self.butExport_2.setText(_translate("MainWindow", "Export Mesh File (.obj)"))
        self.butExport.setText(_translate("MainWindow", "Export Cage File (.obj)"))
        self.label_10.setText(_translate("MainWindow", "by: Wellmann, F., Moulaeifard, M., Bernard S., and Andika, R.B. (2021)"))
        self.butOptimizer.setText(_translate("MainWindow", "Mesh Optimizer"))
        self.butGmesh.setText(_translate("MainWindow", "Finite Element Analysis"))
# import resources_rc

#INSPECTION
    def show_inspect(self):
        if len(self.part)==1 and self.path_cage==None:
                try:
                        files.read(self.part[0]).gui_pick()
                except:
                        self.error_calling('File Error, please input correct (.OBJ) file')

        elif self.path_cage != None and len(self.part)==0:
                try:
                        self.path_cage.gui_pick()
                except:
                        self.error_calling('File Error, please input (.OBJ) correct file')

        else:
                self.error_calling('Please input one Mesh (.OBJ) or one Control-Cage (.OBJ)')

    def status_popup(self):
        psx = QMessageBox()
        psx.setGeometry(640, 480, 500, 500)
        psx.setWindowTitle('Inspection Status')
        psx.setText('Summary of Inspection')
        psx.setIcon(QMessageBox.Information)
        psx.setDefaultButton(QMessageBox.Save)
        psx.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
        psx.setInformativeText('Show Details for Inspected Vertices/Faces')

        d = open('vertices_input.txt')
        lines_vert = str(d.read())

        h = open('faces_input.txt')
        lines_fac = str(h.read())

        lines = str('STATUS VERTICES:' + '\n' + '--------------' + '\n' + lines_vert + '\n' + '\n' + 'STATUS FACES:' + '\n' + '--------------' + '\n' + lines_fac)

        psx.setDetailedText(lines)

        x = psx.exec_()

    def inspect_faces(self):
        with open('face_input.txt', 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]

        psy = QMessageBox()
        psy.setGeometry(640, 480, 200, 200)
        psy.setWindowTitle('Face Inspection')
        psy.setText('Information about Faces')
        psy.setIcon(QMessageBox.Information)
        psy.setStandardButtons(QMessageBox.Ok|QMessageBox.Save)
        psy.setDefaultButton(QMessageBox.Save)
        psy.setInformativeText(last_line)

        d = open('faces_input.txt')
        lines = str(d.read())

        psy.setDetailedText(lines)

        psy.buttonClicked.connect(self.popup_go)

        x = psy.exec_()

    def inspect_vertices(self):
        with open('data_input.txt', 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]

        psy = QMessageBox()
        psy.setGeometry(640, 480, 200, 200)
        psy.setWindowTitle('Vertices Inspection')
        psy.setText('Information about Vertices')
        psy.setIcon(QMessageBox.Information)
        psy.setStandardButtons(QMessageBox.Ok|QMessageBox.Save)
        psy.setDefaultButton(QMessageBox.Save)
        psy.setInformativeText(last_line)

        d = open('vertices_input.txt')
        lines = str(d.read())
        psy.setDetailedText(lines)

        psy.buttonClicked.connect(self.popup_save)
        # QMessageBox.save.connect(self.popup_save())
        # QMessageBox.Save.buttonClicked.connect(self.popup_save)

        x = psy.exec_()

    def popup_save(self, i):
        if i.text() == 'Ok':
                with open('data_input.txt', 'r') as f:
                        lines = f.read().splitlines()
                        last_line = lines[-1]
                        del last_line

        elif i.text() == 'Save':
                with open('data_input.txt', 'r') as f:
                        lines = f.read().splitlines()
                        last_line = lines[-1]

                with open('vertices_input.txt', 'a+') as a:
                        a.write(last_line+'\n')

        else:
                pass

    def popup_go(self, i):
        if i.text() == 'Ok':
                with open('face_input.txt', 'r') as f:
                        lines = f.read().splitlines()
                        last_line = lines[-1]
                        del last_line

        elif i.text() == 'Save':
                with open('face_input.txt', 'r') as f:
                        lines = f.read().splitlines()
                        last_line = lines[-1]

                with open('faces_input.txt', 'a+') as a:
                        a.write(last_line+'\n')

        else:
                pass

    def popup_option(self, i):
        if i.text() == 'Ok':
                with open('face_input.txt', 'r') as f:
                        lines = f.read().splitlines()
                        last_line = lines[-1]
                        del last_line

        elif i.text() == 'Save':
                with open('face_input.txt', 'r') as f:
                        lines = f.read().splitlines()
                        last_line = lines[-1]

                with open('faces_input.txt', 'a+') as a:
                        a.write(last_line+'\n')

        else:
                pass


# MESH OPTIMIZATION
    def opt_mesh(self):
        try:
                os.system('gui_optimizer_3.py')
        except:
                pass

    def auto_submit_defvol(self, text):
            tes = str(text)
            f = open('temp_define_vol.txt', 'w+')
            f.write(tes)
            f.close()


# DEFINE VOLUME
    def define_vol(self):
        if len(self.part)==1 and self.path_cage==None:
                try:
                        files.read(self.part[0]).define_volumes()

                except:
                        self.error_calling('File Error, please input correct (.OBJ) file')

        elif self.path_cage != None and len(self.part)==0:
                try:
                        self.path_cage.define_volumes()

                except:
                        self.error_calling('File Error, please input (.OBJ) correct file')

        else:
                self.error_calling('Please input one Mesh (.OBJ) or one Control-Cage (.OBJ)')

    def inst_defvol(self):
            lines = str(open('temp_instruction_defvolume.txt').read())
            psx = QMessageBox()
            psx.setGeometry(640, 480, 500, 500)
            psx.setWindowTitle('PySubDiv: Define Volume')
            psx.setText('Information about Define Volume ')
            psx.setIcon(QMessageBox.Information)
            psx.setDefaultButton(QMessageBox.Save)
            psx.setStandardButtons(QMessageBox.Ok | QMessageBox.Save)
            psx.setInformativeText(lines)
            psx.setInformativeText('Show Details for Defined Volumes')

            d = str(open('temp_info_vol_def.txt').read())

            dtes = list(d.split("],"))

            a = open('temp_info_vol_def_text.txt', 'w+')
            for i in dtes:
                    if i[-1] == "}":
                            a.write(str(i) + '\n')
                    else:
                            a.write(str(i) + ']' + '\n')
            a.close()

            psx.setDetailedText(str(open('temp_info_vol_def_text.txt').read()))

            psx.buttonClicked.connect(self.popup_defvol_option)

            x = psx.exec_()

    def popup_defvol_option(self, i):
            if i.text() == 'Save':
                    a = open('temp_info_vol_def.txt').read()
                    b = open('exported_volume/exported_volume.txt','w+')
                    b.write(a)
                    b.close()
                    print('ryan')

            else:
                    pass


# G-MESH
    def gmesh(self):
            self.error_calling('Tools not ready yet')


#INTERACTIVE VISUALIZATION
    def vis_mesh(self):
        try:
                self.path_mesh = []
                for part in self.part:
                        try:
                                self.path_mesh.append(files.read(part))
                        except:
                                self.error_calling('File Error, please input correct Mesh and Control Cage (.OBJ) file')
                                break

                try:
                        self.flip_mesh = self.path_cage.visualize_mesh_interactive(additional_meshes=self.path_mesh,
                                                                                   iteration=int(self.iter_subdiv))

                except:
                        self.error_calling('File Error, please input correct Mesh and Control-Cage (.OBJ) file')

        except:
                self.error_calling('Please Input the Mesh and Control-Cage (.OBJ) Data')

    def slide_value(self, text):
        tes = str(text)

        self.iter_subdiv = tes

        f = open('temp_slide_input.txt', 'w+')
        f.write(tes)
        f.close()

        self.label_17.setText("Subdivision Iteration: "+ tes)
        self.label_17.adjustSize()

    def slide_value_2(self, text):
        tes = str(text)

        f = open('temp_sharp_input.txt', 'w+')
        f.write(tes)
        f.close()

        self.label_19.setText("Sharpness: " + tes)
        self.label_19.adjustSize()

    def flip_vismesh(self):
            try:
                    self.flip_mesh = self.path_cage.visualize_mesh_interactive(additional_meshes=self.path_mesh,
                                                                               iteration=int(self.iter_subdiv),
                                                                               close_pref = True)
                    self.flip_mesh.visualize_mesh_conventional()

            except:
                    self.error_calling('Mesh not ready, please try again')


#MULTI CAGE
    def mulcage(self):
        try:
                self.path_mesh = []
                for part in self.part:
                        self.path_mesh.append(files.read(part))

                try:
                        self.flip_cage = []
                        self.flip_cage.append(control_cage.create_control_cage(self.path_mesh, find_vertices=True,
                                                                               calc_intersection=False,
                                                                               add_boundary_box=False,
                                                                               use_dynamic_faces=True))
                except:
                        self.error_calling('Process error, please try again')

        except:
                self.error_calling('Please Input Mesh (.OBJ) File Data')

    def flip_cc(self):
            try:
                    aa = control_cage.add_cc(control_cage_faces=self.flip_cage[0][0],
                                        p_cloud_complete=self.flip_cage[0][1],
                                        dynamic_face=self.flip_cage[0][2],
                                        dynamic_vertices_dict=self.flip_cage[0][3],
                                        vertices_fit=self.flip_cage[0][4],
                                        use_dynamic_faces=self.flip_cage[0][5])

                    aa.save_mesh('exported_obj/temp_cage.obj')
                    aa.save_data('exported_obj/temp_cage_data')

                    files.read('exported_obj/temp_cage.obj').visualize_mesh_conventional()

                    try:
                            new_cage = files.read('exported_obj/temp_cage.obj').load_data('exported_obj/temp_cage_data')
                            self.success_calling('Control Cage is Ready for Mesh Optimizer Module.')

                    except:
                            self.error_calling('Static - Dynamic data assessment is not match for Mesh Optimizer. Please create again.')

            except:
                    self.error_calling('Process Error, Please Try Again')

    def auto_submit_vert1(self, text):
            tes = str(text)
            f = open('temp_vert1.txt', 'w+')
            f.write(tes)
            f.close()

    def auto_submit_vert2(self, text):
            tes = str(text)
            f = open('temp_vert2.txt', 'w+')
            f.write(tes)
            f.close()

    def auto_submit_vert3(self, text):
            tes = str(text)
            f = open('temp_vert3.txt', 'w+')
            f.write(tes)
            f.close()

    def auto_submit_dynface(self, text):
            tes = str(text)
            f = open('temp_dynface.txt', 'w+')
            f.write(tes)
            f.close()

    def auto_submit_meshindex(self, text):
            tes = str(text)
            f = open('temp_confmesh.txt', 'w+')
            f.write(tes)
            f.close()


# SINGLE INPUT FILE (CAGE)
    def data_input_cage(self):
            self.open_dialog_box_cage()

    def open_dialog_box_cage(self):
            try:
                    filename = QFileDialog.getOpenFileName()
                    a = filename[0]
                    self.name_cage = str(a)
                    self.status_name_cage()
                    self.butCageStatus.setText("Cage Ready 1")
                    self.path_cage = files.read(a)

            except:
                    pass

    def status_name_cage(self):
            for i in range(len(self.name_cage) - 1, -1, -1):
                    if self.name_cage[i] != '/':
                            continue
                    else:
                            a = self.name_cage[i + 1:]
                            break

            self.status_data_cage = a

    def info_cage(self):
            lines = str(self.status_data_cage)
            psx = QMessageBox()
            psx.setGeometry(640, 480, 500, 500)
            psx.setWindowTitle('PySubDiv: Cage Input')
            psx.setText('Information about Input Control Cage Data ')
            psx.setIcon(QMessageBox.Information)
            psx.setDefaultButton(QMessageBox.Save)
            psx.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            psx.setInformativeText('Control Cage: ' + lines)

            psx.buttonClicked.connect(self.popup_cage_option)

            x = psx.exec_()

    def reset_cage(self):
            self.path_cage = None
            self.status_data_cage = None
            self.butCageStatus.setText("Cage Empty")

    def popup_cage_option(self, i):
            if i.text() == 'OK':
                    pass

            else:
                    self.reset_cage()


# MULTIPLE INPUT FILE (mesh)
    def data_input_mesh(self):
        self.open_dialog_box_mesh()

    def open_dialog_box_mesh(self):
        try:
            filename = QFileDialog.getOpenFileName()
            if not filename[0]:
                    pass
            else:
                    a = filename[0]
                    self.part.append(a)
                    self.butMeshStatus.setText("Mesh Ready " + str(len(self.part)))
                    self.status_name_multi_mesh()
        except:
            pass

    def status_name_multi_mesh(self):
        tes2 = self.part
        aa = []
        for j in tes2:
                for i in range(len(j) - 1, -1, -1):
                        if j[i] != '/':
                                continue
                        else:
                                aa.append(j[i + 1:])
                                break

        self.name_mesh = str(aa)

    def reset_multi_data(self):
        self.part = []
        self.name_mesh = str(self.part)
        self.butMeshStatus.setText("Mesh Empty")

    def info_mesh(self):
            psx = QMessageBox()
            psx.setGeometry(640, 480, 500, 500)
            psx.setText('Information about Input Mesh Data')
            psx.setWindowTitle('PySubDiv: Mesh Input')
            psx.setIcon(QMessageBox.Information)
            psx.setDefaultButton(QMessageBox.Save)
            psx.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            psx.setInformativeText('Show Details for all Data Input')

            if self.name_mesh != None:
                    lines = self.name_mesh
                    tes = list(lines.split(","))

                    a = open('temp_meshes_input.txt', 'w+')
                    for i in tes:
                            a.write('Mesh: ' + str(tes.index(i)) + ' | ' + str(i) + '\n')
                    a.close()

                    psx.setDetailedText(str(open('temp_meshes_input.txt').read()))

            else:
                    psx.setDetailedText(str('None'))

            psx.buttonClicked.connect(self.popup_mesh_option)

            x = psx.exec_()

    def popup_mesh_option(self, i):
            if i.text() == 'OK':
                    pass

            else:
                    self.reset_multi_data()


# INSTRUCTION
    def inst_cc(self):
            lines = str(open('temp_instruction_mulcage.txt').read())
            psx = QMessageBox()
            psx.setGeometry(640, 480, 500, 500)
            psx.setWindowTitle('PySubDiv: Cage Input')
            psx.setText('Information about Input Control Cage Data ')
            psx.setIcon(QMessageBox.Information)
            psx.setDefaultButton(QMessageBox.Save)
            psx.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
            psx.setInformativeText(lines)

            x = psx.exec_()

    def inst_int(self):
            lines = str(open('temp_instruction_interactive.txt').read())
            psx = QMessageBox()
            psx.setGeometry(640, 480, 500, 500)
            psx.setWindowTitle('PySubDiv: Cage Input')
            psx.setText('Information about Input Control Cage Data ')
            psx.setIcon(QMessageBox.Information)
            psx.setDefaultButton(QMessageBox.Save)
            psx.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
            psx.setInformativeText(lines)

            x = psx.exec_()

    def inst_ins(self):
            lines = str(open('temp_instruction_inspection.txt').read())
            psx = QMessageBox()
            psx.setGeometry(640, 480, 500, 500)
            psx.setWindowTitle('PySubDiv: Cage Input')
            psx.setText('Information about Input Control Cage Data ')
            psx.setIcon(QMessageBox.Information)
            psx.setDefaultButton(QMessageBox.Save)
            psx.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
            psx.setInformativeText(lines)

            x = psx.exec_()


# EXPORT FILE
    def export_mesh(self):
        try:
                export_name = self.lineEdit_19.text()
                # tes = files.read('exported_obj/temp_mesh.obj')
                self.flip_mesh.save_mesh('exported_obj/'+ export_name + '.obj')

                psy = QMessageBox()
                psy.setGeometry(640, 480, 200, 200)
                psy.setWindowTitle('Export File .OBJ')
                psy.setText('Data Exported: ' + export_name +'.obj')
                psy.setIcon(QMessageBox.Information)
                psy.setStandardButtons(QMessageBox.Ok)
                psy.setDefaultButton(QMessageBox.Ok)

                x = psy.exec_()

        except:
                self.error_calling('Please input name of Exported Mesh (.OBJ) file')

    def export_cage(self):
        try:
                export_name = self.lineEdit_19.text()
                tes = files.read('exported_obj/temp_cage.obj')
                tes.save_mesh('exported_obj/'+ export_name + '.obj')
                tes.save_data('exported_obj/'+ export_name + '_data')

                psy = QMessageBox()
                psy.setGeometry(640, 480, 200, 200)
                psy.setWindowTitle('Export File .OBJ')
                psy.setText('Data Exported: ' + export_name +'.obj')
                psy.setIcon(QMessageBox.Information)
                psy.setStandardButtons(QMessageBox.Ok)
                psy.setDefaultButton(QMessageBox.Ok)

                x = psy.exec_()

        except:
                self.error_calling('Please input name of Exported Cage (.OBJ) file')


# Calling Error
    def error_calling(self, text):
            psy = QMessageBox()
            psy.setGeometry(640, 480, 200, 200)
            psy.setWindowTitle('Process Error')
            psy.setText(text)
            psy.setIcon(QMessageBox.Critical)
            psy.setStandardButtons(QMessageBox.Ok)
            psy.setDefaultButton(QMessageBox.Ok)

            x = psy.exec_()

    def success_calling(self, text):
            psy = QMessageBox()
            psy.setGeometry(640, 480, 200, 200)
            psy.setWindowTitle('Process Successful')
            psy.setText(text)
            psy.setIcon(QMessageBox.Information)
            psy.setStandardButtons(QMessageBox.Ok)
            psy.setDefaultButton(QMessageBox.Ok)

            x = psy.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

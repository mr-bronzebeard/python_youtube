# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_app_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 600))
        MainWindow.setBaseSize(QtCore.QSize(1280, 600))
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1281, 615))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, -1, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_name = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        self.label_name.setMinimumSize(QtCore.QSize(240, 0))
        self.label_name.setMaximumSize(QtCore.QSize(240, 240))
        self.label_name.setBaseSize(QtCore.QSize(240, 240))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_name.setFont(font)
        self.label_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_name.setAutoFillBackground(False)
        self.label_name.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_name.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_name.setTextFormat(QtCore.Qt.AutoText)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.gridLayout_2.addWidget(self.label_name, 1, 0, 1, 1)
        self.label_avatar = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_avatar.sizePolicy().hasHeightForWidth())
        self.label_avatar.setSizePolicy(sizePolicy)
        self.label_avatar.setMinimumSize(QtCore.QSize(240, 240))
        self.label_avatar.setMaximumSize(QtCore.QSize(240, 240))
        self.label_avatar.setBaseSize(QtCore.QSize(240, 240))
        self.label_avatar.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_avatar.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_avatar.setAlignment(QtCore.Qt.AlignCenter)
        self.label_avatar.setObjectName("label_avatar")
        self.gridLayout_2.addWidget(self.label_avatar, 0, 0, 1, 1)
        self.label_statistic = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_statistic.setMinimumSize(QtCore.QSize(240, 0))
        self.label_statistic.setMaximumSize(QtCore.QSize(240, 240))
        self.label_statistic.setBaseSize(QtCore.QSize(240, 15))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.label_statistic.setFont(font)
        self.label_statistic.setObjectName("label_statistic")
        self.gridLayout_2.addWidget(self.label_statistic, 3, 0, 1, 1)
        self.textBrowser_statistic = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser_statistic.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_statistic.sizePolicy().hasHeightForWidth())
        self.textBrowser_statistic.setSizePolicy(sizePolicy)
        self.textBrowser_statistic.setMaximumSize(QtCore.QSize(240, 300))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.textBrowser_statistic.setFont(font)
        self.textBrowser_statistic.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.textBrowser_statistic.setLineWidth(1)
        self.textBrowser_statistic.setMidLineWidth(0)
        self.textBrowser_statistic.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textBrowser_statistic.setReadOnly(True)
        self.textBrowser_statistic.setObjectName("textBrowser_statistic")
        self.gridLayout_2.addWidget(self.textBrowser_statistic, 4, 0, 1, 1)
        self.label_login = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_login.setMinimumSize(QtCore.QSize(240, 0))
        self.label_login.setMaximumSize(QtCore.QSize(240, 240))
        self.label_login.setBaseSize(QtCore.QSize(240, 15))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.label_login.setFont(font)
        self.label_login.setAlignment(QtCore.Qt.AlignCenter)
        self.label_login.setObjectName("label_login")
        self.gridLayout_2.addWidget(self.label_login, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.tabWidget = QtWidgets.QTabWidget(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setIconSize(QtCore.QSize(32, 32))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1021, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(5, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.lineEdit_search = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.horizontalLayout_3.addWidget(self.lineEdit_search)
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButton_search = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_search.setObjectName("pushButton_search")
        self.horizontalLayout_3.addWidget(self.pushButton_search)
        spacerItem2 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton_clear = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout_3.addWidget(self.pushButton_clear)
        spacerItem3 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.textBrowser_test_search_result = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.textBrowser_test_search_result.setFont(font)
        self.textBrowser_test_search_result.setObjectName("textBrowser_test_search_result")
        self.verticalLayout.addWidget(self.textBrowser_test_search_result)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, 9, 991, 501))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube Test API Antonenko"))
        self.label_name.setText(_translate("MainWindow", "Name"))
        self.label_avatar.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Ваш аватар</span></p></body></html>"))
        self.label_avatar.setText(_translate("MainWindow", "Здесь мог быть аватар"))
        self.label_statistic.setText(_translate("MainWindow", "Статистика:"))
        self.label_login.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Переход на страницу Вашего канала</span></p></body></html>"))
        self.label_login.setText(_translate("MainWindow", "Login"))
        self.lineEdit_search.setPlaceholderText(_translate("MainWindow", "Введите запрос для поиска"))
        self.pushButton_search.setText(_translate("MainWindow", "search"))
        self.pushButton_clear.setText(_translate("MainWindow", "clear"))
        self.textBrowser_test_search_result.setPlaceholderText(_translate("MainWindow", "Здесь будут результаты поиска"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Поиск"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Популярные видео (возможно)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Комментраии к видео (возможно)"))


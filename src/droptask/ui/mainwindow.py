# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QVBoxLayout, QWidget)
from src.droptask.ui import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(1039, 665)
        MainWindow.setStyleSheet(u"")
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.iconOnlySideBarWidget = QWidget(self.centralwidget)
        self.iconOnlySideBarWidget.setObjectName(u"iconOnlySideBarWidget")
        self.verticalLayout_3 = QVBoxLayout(self.iconOnlySideBarWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.iconSidebarLogo = QLabel(self.iconOnlySideBarWidget)
        self.iconSidebarLogo.setObjectName(u"iconSidebarLogo")
        self.iconSidebarLogo.setMinimumSize(QSize(50, 50))
        self.iconSidebarLogo.setMaximumSize(QSize(50, 50))
        self.iconSidebarLogo.setPixmap(QPixmap(u":/icons/icons/logo.png"))
        self.iconSidebarLogo.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.iconSidebarLogo)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.iconTodoButton = QPushButton(self.iconOnlySideBarWidget)
        self.iconTodoButton.setObjectName(u"iconTodoButton")
        icon = QIcon()
        icon.addFile(u":/icons/icons/todo_sidebar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.iconTodoButton.setIcon(icon)
        self.iconTodoButton.setIconSize(QSize(20, 20))
        self.iconTodoButton.setCheckable(True)
        self.iconTodoButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.iconTodoButton)

        self.iconFocusButton = QPushButton(self.iconOnlySideBarWidget)
        self.iconFocusButton.setObjectName(u"iconFocusButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/focus_sidebar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.iconFocusButton.setIcon(icon1)
        self.iconFocusButton.setIconSize(QSize(20, 20))
        self.iconFocusButton.setCheckable(True)
        self.iconFocusButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.iconFocusButton)

        self.iconPlanButton = QPushButton(self.iconOnlySideBarWidget)
        self.iconPlanButton.setObjectName(u"iconPlanButton")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/planned_sidebar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.iconPlanButton.setIcon(icon2)
        self.iconPlanButton.setIconSize(QSize(20, 20))
        self.iconPlanButton.setCheckable(True)
        self.iconPlanButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.iconPlanButton)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 398, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.iconSettingButton = QPushButton(self.iconOnlySideBarWidget)
        self.iconSettingButton.setObjectName(u"iconSettingButton")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.iconSettingButton.setIcon(icon3)
        self.iconSettingButton.setIconSize(QSize(20, 20))
        self.iconSettingButton.setCheckable(True)
        self.iconSettingButton.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.iconSettingButton)


        self.gridLayout.addWidget(self.iconOnlySideBarWidget, 0, 0, 1, 1)

        self.fullSidebarWidget = QWidget(self.centralwidget)
        self.fullSidebarWidget.setObjectName(u"fullSidebarWidget")
        self.verticalLayout_4 = QVBoxLayout(self.fullSidebarWidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.logoAndNameLayout = QHBoxLayout()
        self.logoAndNameLayout.setObjectName(u"logoAndNameLayout")
        self.fullSidebarLogo = QLabel(self.fullSidebarWidget)
        self.fullSidebarLogo.setObjectName(u"fullSidebarLogo")
        self.fullSidebarLogo.setMinimumSize(QSize(40, 40))
        self.fullSidebarLogo.setMaximumSize(QSize(40, 40))
        self.fullSidebarLogo.setPixmap(QPixmap(u":/icons/icons/logo.png"))
        self.fullSidebarLogo.setScaledContents(True)

        self.logoAndNameLayout.addWidget(self.fullSidebarLogo)

        self.appName = QLabel(self.fullSidebarWidget)
        self.appName.setObjectName(u"appName")

        self.logoAndNameLayout.addWidget(self.appName)


        self.verticalLayout_4.addLayout(self.logoAndNameLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.fullTodoButton = QPushButton(self.fullSidebarWidget)
        self.fullTodoButton.setObjectName(u"fullTodoButton")
        self.fullTodoButton.setIcon(icon)
        self.fullTodoButton.setIconSize(QSize(14, 14))
        self.fullTodoButton.setCheckable(True)
        self.fullTodoButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.fullTodoButton)

        self.fullFocusButton = QPushButton(self.fullSidebarWidget)
        self.fullFocusButton.setObjectName(u"fullFocusButton")
        self.fullFocusButton.setIcon(icon1)
        self.fullFocusButton.setIconSize(QSize(14, 14))
        self.fullFocusButton.setCheckable(True)
        self.fullFocusButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.fullFocusButton)

        self.fullPlanButton = QPushButton(self.fullSidebarWidget)
        self.fullPlanButton.setObjectName(u"fullPlanButton")
        self.fullPlanButton.setIcon(icon2)
        self.fullPlanButton.setIconSize(QSize(14, 14))
        self.fullPlanButton.setCheckable(True)
        self.fullPlanButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.fullPlanButton)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 408, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.fullSettingButton = QPushButton(self.fullSidebarWidget)
        self.fullSettingButton.setObjectName(u"fullSettingButton")
        self.fullSettingButton.setIcon(icon3)
        self.fullSettingButton.setIconSize(QSize(14, 14))
        self.fullSettingButton.setCheckable(True)
        self.fullSettingButton.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.fullSettingButton)


        self.gridLayout.addWidget(self.fullSidebarWidget, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menuButton = QPushButton(self.widget)
        self.menuButton.setObjectName(u"menuButton")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuButton.setIcon(icon4)
        self.menuButton.setCheckable(True)
        self.menuButton.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.menuButton)

        self.horizontalSpacer = QSpacerItem(211, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.searchButton = QPushButton(self.widget)
        self.searchButton.setObjectName(u"searchButton")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.searchButton.setIcon(icon5)

        self.horizontalLayout.addWidget(self.searchButton)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(211, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_4.addWidget(self.checkBox)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(380, 280, 66, 18))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(410, 270, 66, 18))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(380, 260, 66, 18))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_7 = QLabel(self.page_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(390, 280, 66, 18))
        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menuButton.toggled.connect(self.iconOnlySideBarWidget.setVisible)
        self.menuButton.toggled.connect(self.fullSidebarWidget.setHidden)
        self.iconTodoButton.toggled.connect(self.fullTodoButton.setChecked)
        self.iconFocusButton.toggled.connect(self.fullFocusButton.setChecked)
        self.iconPlanButton.toggled.connect(self.fullPlanButton.setChecked)
        self.iconSettingButton.toggled.connect(self.fullSettingButton.setChecked)
        self.fullTodoButton.toggled.connect(self.iconTodoButton.setChecked)
        self.fullFocusButton.toggled.connect(self.iconFocusButton.setChecked)
        self.fullPlanButton.toggled.connect(self.iconPlanButton.setChecked)
        self.fullSettingButton.toggled.connect(self.iconSettingButton.setChecked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DropTask", None))
        self.iconSidebarLogo.setText("")
        self.iconTodoButton.setText("")
        self.iconFocusButton.setText("")
        self.iconPlanButton.setText("")
        self.iconSettingButton.setText("")
        self.fullSidebarLogo.setText("")
        self.appName.setText(QCoreApplication.translate("MainWindow", u"Viet Mind", None))
        self.fullTodoButton.setText(QCoreApplication.translate("MainWindow", u"Tasks", None))
        self.fullFocusButton.setText(QCoreApplication.translate("MainWindow", u"Focus", None))
        self.fullPlanButton.setText(QCoreApplication.translate("MainWindow", u"Plans", None))
        self.fullSettingButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuButton.setText("")
        self.searchButton.setText("")
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Viet", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Task", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Focus", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Planned", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi


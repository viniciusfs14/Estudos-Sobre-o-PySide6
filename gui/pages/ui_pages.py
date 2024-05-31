# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesOsojmM.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

class Ui_aplication_pages(object):
    def setupUi(self, aplication_pages):
        if not aplication_pages.objectName():
            aplication_pages.setObjectName(u"aplication_pages")
        aplication_pages.resize(901, 477)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.horizontalLayout = QHBoxLayout(self.page_1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.page_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        aplication_pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_2 = QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        aplication_pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout = QVBoxLayout(self.page_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        aplication_pages.addWidget(self.page_3)

        self.retranslateUi(aplication_pages)

        QMetaObject.connectSlotsByName(aplication_pages)
    # setupUi

    def retranslateUi(self, aplication_pages):
        aplication_pages.setWindowTitle(QCoreApplication.translate("aplication_pages", u"StackedWidget", None))
        self.label_3.setText(QCoreApplication.translate("aplication_pages", u"P\u00e1gina 1", None))
        self.label_2.setText(QCoreApplication.translate("aplication_pages", u"P\u00e1gina 2", None))
        self.label.setText(QCoreApplication.translate("aplication_pages", u"P\u00e1gina 3", None))
    # retranslateUi


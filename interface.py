from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtChart import QChartView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1900, 940)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"QWidget{\n"
                                  "	background-color : white;\n"
                                  "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1900, 940))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.head_layout = QHBoxLayout()
        self.head_layout.setSpacing(20)
        self.head_layout.setObjectName(u"head_layout")
        self.name_layout = QVBoxLayout()
        self.name_layout.setSpacing(0)
        self.name_layout.setObjectName(u"name_layout")
        self.name_label = QLabel(self.centralwidget)
        self.name_label.setObjectName(u"name_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy1)
        self.name_label.setMinimumSize(QSize(460, 90))
        self.name_label.setMaximumSize(QSize(460, 90))
        font = QFont()
        font.setFamily(u"DengXian")
        font.setPointSize(42)
        font.setBold(False)
        font.setItalic(False)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet(u"QLabel{\n"
                                       "	background-color: #806EC2;\n"
                                       "	color: #FFD966;\n"
                                       "	font: 42pt \"DengXian\";\n"
                                       "}\n")
        self.name_label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        self.name_layout.addWidget(self.name_label)

        self.service_label = QLabel(self.centralwidget)
        self.service_label.setObjectName(u"service_label")
        sizePolicy1.setHeightForWidth(self.service_label.sizePolicy().hasHeightForWidth())
        self.service_label.setSizePolicy(sizePolicy1)
        self.service_label.setMinimumSize(QSize(460, 30))
        self.service_label.setMaximumSize(QSize(460, 30))
        self.service_label.setStyleSheet(u"QLabel{\n"
                                          "	background-color: #806EC2;\n"
                                          "	color: #FFD966;\n"
                                          "	font: 14pt \"DengXian\";\n"
                                          "}\n")
        self.service_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.name_layout.addWidget(self.service_label)


        self.head_layout.addLayout(self.name_layout)

        self.requires_layout = QVBoxLayout()
        self.requires_layout.setSpacing(0)
        self.requires_layout.setObjectName(u"requires_layout")
        self.requires_box = QComboBox(self.centralwidget)
        self.requires_box.setObjectName(u"requires_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.requires_box.sizePolicy().hasHeightForWidth())
        self.requires_drop_down = QListView(self.requires_box)
        self.requires_drop_down.setFont(QFont("DengXian", 9))
        self.requires_drop_down.setStyleSheet("QListView::item {                    \
                                     border-bottom: 5px solid white; margin:1px; }  \
                                     QListView::item:selected {                     \
                                     margin:3px;    \
                                     color: black;                                  \
                                    }                                               \
                                    ")
        self.requires_box.setSizePolicy(sizePolicy2)
        self.requires_box.setMinimumSize(QSize(1100, 55))
        self.requires_box.setMaximumSize(QSize(1400, 60))
        self.requires_box.setStyleSheet(u" QComboBox {\n"
                                         "     border: 3px solid #FFD966;\n"
                                         "     border-radius: 8px;\n"
                                         "     padding: 0 8px;\n"
                                         "     background: white;\n"
                                         "     selection-background-color: darkgray;\n"
                                         " }")

        self.requires_layout.addWidget(self.requires_box)

        self.hint_label = QLabel(self.centralwidget)
        self.hint_label.setObjectName(u"hint_label")
        sizePolicy1.setHeightForWidth(self.hint_label.sizePolicy().hasHeightForWidth())
        self.hint_label.setSizePolicy(sizePolicy1)
        self.hint_label.setMinimumSize(QSize(0, 20))
        self.hint_label.setMaximumSize(QSize(1400, 20))
        font1 = QFont()
        font1.setFamily(u"DengXian")
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.hint_label.setFont(font1)
        self.hint_label.setStyleSheet(u"QLabel{\n"
                                       "	font: 11pt \"DengXian\";\n"
                                       "	color : #5A45A5;\n"
                                       "}")

        self.requires_layout.addWidget(self.hint_label)


        self.head_layout.addLayout(self.requires_layout)


        self.verticalLayout.addLayout(self.head_layout)

        self.body_layout = QHBoxLayout()
        self.body_layout.setSpacing(30)
        self.body_layout.setObjectName(u"body_layout")
        self.body_layout.setSizeConstraint(QLayout.SetMaximumSize)
        self.categories_layout = QVBoxLayout()
        self.categories_layout.setSpacing(12)
        self.categories_layout.setObjectName(u"categories_layout")
        self.categories_layout.setSizeConstraint(QLayout.SetMinimumSize)
        self.categries_name = QLabel(self.centralwidget)
        self.categries_name.setObjectName(u"categries_name")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.categries_name.sizePolicy().hasHeightForWidth())
        self.categries_name.setSizePolicy(sizePolicy3)
        self.categries_name.setMinimumSize(QSize(200, 40))
        self.categries_name.setMaximumSize(QSize(450, 40))
        font2 = QFont()
        font2.setFamily(u"DengXian")
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setItalic(False)
        self.categries_name.setFont(font2)
        self.categries_name.setStyleSheet(u"QLabel{\n"
                                           "	font: 18pt \"DengXian\";\n"
                                           "	color : #5A45A5;\n"
                                           "}")

        self.categories_layout.addWidget(self.categries_name)

        self.categories_txt = QTreeView(self.centralwidget)
        self.categories_txt.setObjectName(u"categories_txt")
        sizePolicy3.setHeightForWidth(self.categories_txt.sizePolicy().hasHeightForWidth())
        self.categories_txt.setSizePolicy(sizePolicy3)
        self.categories_txt.setMinimumSize(QSize(400, 500))
        self.categories_txt.setMaximumSize(QSize(450, 800))
        self.categories_txt.setFrameShape(QFrame.NoFrame)
        self.categories_txt.setWordWrap(True)
        self.categories_txt.setItemDelegate(ItemWordWrap(self.categories_txt))

        self.categories_layout.addWidget(self.categories_txt)


        self.body_layout.addLayout(self.categories_layout)

        self.similar_case_layuot = QVBoxLayout()
        self.similar_case_layuot.setSpacing(12)
        self.similar_case_layuot.setObjectName(u"similar_case_layuot")
        self.similar_case_layuot.setSizeConstraint(QLayout.SetMaximumSize)
        self.similar_case_name = QLabel(self.centralwidget)
        self.similar_case_name.setObjectName(u"similar_case_name")
        sizePolicy3.setHeightForWidth(self.similar_case_name.sizePolicy().hasHeightForWidth())
        self.similar_case_name.setSizePolicy(sizePolicy3)
        self.similar_case_name.setMinimumSize(QSize(285, 40))
        self.similar_case_name.setMaximumSize(QSize(285, 40))
        self.similar_case_name.setFont(font2)
        self.similar_case_name.setStyleSheet(u"QLabel{\n"
                                              "	font: 18pt \"DengXian\";\n"
                                              "	color : #5A45A5;\n"
                                              "}")

        self.similar_case_layuot.addWidget(self.similar_case_name)

        self.similar_case_txt = QTableView(self.centralwidget)
        self.similar_case_txt.setObjectName(u"similar_case_txt")
        self.similar_case_txt.setFrameShape(QFrame.NoFrame)
        self.similar_case_txt.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.similar_case_txt.horizontalHeader().setFont(QFont("DengXian", 9))
        self.similar_case_txt.setGridStyle(Qt.NoPen)
        self.similar_case_txt.verticalHeader().setVisible(False)
        self.similar_case_txt.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.similar_case_layuot.addWidget(self.similar_case_txt)


        self.body_layout.addLayout(self.similar_case_layuot)

        self.analys_layout = QVBoxLayout()
        self.analys_layout.setSpacing(12)
        self.analys_layout.setObjectName(u"analys_layout")
        self.analys_layout.setSizeConstraint(QLayout.SetMinimumSize)
        self.analys_name = QLabel(self.centralwidget)
        self.analys_name.setObjectName(u"analys_name")
        sizePolicy3.setHeightForWidth(self.analys_name.sizePolicy().hasHeightForWidth())
        self.analys_name.setSizePolicy(sizePolicy3)
        self.analys_name.setMinimumSize(QSize(139, 40))
        self.analys_name.setMaximumSize(QSize(139, 40))
        self.analys_name.setFont(font2)
        self.analys_name.setStyleSheet(u"QLabel{\n"
"	font: 18pt \"DengXian\";\n"
"	color : #5A45A5;\n"
"}")

        self.analys_layout.addWidget(self.analys_name)

        self.analys_sum = QTextEdit(self.centralwidget)
        self.analys_sum.setObjectName(u"analys_sum")
        sizePolicy3.setHeightForWidth(self.analys_sum.sizePolicy().hasHeightForWidth())
        self.analys_sum.setSizePolicy(sizePolicy3)
        self.analys_sum.setMinimumSize(QSize(400, 200))
        self.analys_sum.setMaximumSize(QSize(450, 245))
        self.analys_sum.setStyleSheet(u"QTextEdit{\n"
                                       "border-color: rgb(255, 255, 255);\n"
                                       "color : #203864\n"
                                       "font: 18pt \"Candara Light\";\n"
                                       "}")
        self.analys_sum.setReadOnly(True)
        self.analys_sum.setFrameShape(QFrame.NoFrame)

        self.analys_layout.addWidget(self.analys_sum)

        self.analys_pic = QChartView(self.centralwidget)
        self.analys_pic.setObjectName(u"analys_pic")
        sizePolicy3.setHeightForWidth(self.analys_pic.sizePolicy().hasHeightForWidth())
        self.analys_pic.setSizePolicy(sizePolicy3)
        self.analys_pic.setMinimumSize(QSize(400, 300))
        self.analys_pic.setMaximumSize(QSize(450, 350))

        self.analys_layout.addWidget(self.analys_pic)

        self.analys_txt = QListView(self.centralwidget)
        self.analys_txt.setObjectName(u"analys_txt")
        sizePolicy3.setHeightForWidth(self.analys_txt.sizePolicy().hasHeightForWidth())
        self.analys_txt.setSizePolicy(sizePolicy3)
        self.analys_txt.setMinimumSize(QSize(400, 130))
        self.analys_txt.setMaximumSize(QSize(450, 150))
        self.analys_txt.setFrameShape(QFrame.NoFrame)

        self.analys_layout.addWidget(self.analys_txt)


        self.body_layout.addLayout(self.analys_layout)


        self.verticalLayout.addLayout(self.body_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0446\u0435\u0434\u0435\u043d\u0442", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0420\u0415\u0426\u0415\u0414\u0415\u041d\u0422", None))
        self.service_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0432\u0438\u0441 \u0430\u043d\u0430\u043b\u0438\u0437\u0430 \u0441\u0443\u0434\u0435\u0431\u043d\u043e\u0439 \u043f\u0440\u0430\u0442\u0438\u043a\u0438", None))
        self.hint_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.categries_name.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0434\u0435\u043b:", None))
        self.similar_case_name.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0445\u043e\u0436\u0438\u0435 \u0434\u0435\u043b\u0430:", None))
        self.analys_name.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437:", None))
    # retranslateUi


class ScrollLabel(QScrollArea):
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)
        self.setFixedSize(700, 550)
        self.setWidgetResizable(True)
        content = QWidget(self)
        self.setWidget(content)
        lay = QVBoxLayout(content)
        self.label = QLabel(content)
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setFont(QFont('Arial', 10))
        lay.addWidget(self.label)

    def setText(self, text):
        self.label.setText(text)


class AnotherWindow(QWidget):
    def __init__(self, text):
        super().__init__()

        self.scroll = ScrollLabel(self)
        self.scroll.setGeometry(10, 10, 800, 650)
        self.scroll.setText(text)


class ItemWordWrap(QStyledItemDelegate):
    def __init__(self, parent=None):
        QStyledItemDelegate.__init__(self, parent)
        self.parent = parent

    def paint(self, painter, option, index):
        text = index.model().data(index)
        document = QTextDocument()
        document.setHtml(text)
        document.setTextWidth(option.rect.width())
        painter.save()
        painter.translate(option.rect.x(), option.rect.y())
        document.drawContents(painter)
        index.model().setData(index, option.rect.width(), Qt.UserRole + 1)
        painter.restore()

    def sizeHint(self, option, index):
        text = index.model().data(index)
        document = QTextDocument()
        document.setHtml(text)
        width = index.model().data(index, Qt.UserRole + 1)
        if not width:
            width = 20
        document.setTextWidth(width)
        return QSize(document.idealWidth() + 10,  document.size().height())
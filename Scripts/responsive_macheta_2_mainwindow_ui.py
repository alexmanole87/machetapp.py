# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'responsive_macheta_2_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Macheta(object):
    def setupUi(self, Macheta):
        Macheta.setObjectName("Macheta")
        Macheta.resize(1816, 901)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        Macheta.setFont(font)
        Macheta.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        Macheta.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(Macheta)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(36, 0, 2152, 851))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.def_label = QtWidgets.QLabel(self.widget)
        self.def_label.setObjectName("def_label")
        self.gridLayout.addWidget(self.def_label, 3, 25, 1, 2)
        self.nume_parinti_inc = QtWidgets.QLineEdit(self.widget)
        self.nume_parinti_inc.setObjectName("nume_parinti_inc")
        self.gridLayout.addWidget(self.nume_parinti_inc, 4, 16, 1, 12)
        self.parinti_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.parinti_label.setFont(font)
        self.parinti_label.setObjectName("parinti_label")
        self.gridLayout.addWidget(self.parinti_label, 4, 13, 1, 3)
        self.nume_inc = QtWidgets.QLineEdit(self.widget)
        self.nume_inc.setObjectName("nume_inc")
        self.gridLayout.addWidget(self.nume_inc, 4, 1, 1, 12)
        self.oblig_3_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.oblig_3_label.setFont(font)
        self.oblig_3_label.setObjectName("oblig_3_label")
        self.gridLayout.addWidget(self.oblig_3_label, 11, 23, 3, 3)
        self.inc_doc = QtWidgets.QPushButton(self.widget)
        self.inc_doc.setFlat(True)
        self.inc_doc.setObjectName("inc_doc")
        self.gridLayout.addWidget(self.inc_doc, 0, 0, 1, 9)
        self.obl_1 = QtWidgets.QLineEdit(self.widget)
        self.obl_1.setText("")
        self.obl_1.setObjectName("obl_1")
        self.gridLayout.addWidget(self.obl_1, 8, 26, 1, 6)
        self.an_ds_instanta = QtWidgets.QComboBox(self.widget)
        self.an_ds_instanta.setObjectName("an_ds_instanta")
        self.an_ds_instanta.addItem("")
        self.an_ds_instanta.addItem("")
        self.an_ds_instanta.addItem("")
        self.an_ds_instanta.addItem("")
        self.gridLayout.addWidget(self.an_ds_instanta, 3, 10, 1, 2)
        self.sent_label = QtWidgets.QLabel(self.widget)
        self.sent_label.setObjectName("sent_label")
        self.gridLayout.addWidget(self.sent_label, 3, 12, 1, 2)
        self.instit_2_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.instit_2_label.setFont(font)
        self.instit_2_label.setObjectName("instit_2_label")
        self.gridLayout.addWidget(self.instit_2_label, 13, 28, 3, 3)
        self.nlp = QtWidgets.QPushButton(self.widget)
        self.nlp.setFlat(True)
        self.nlp.setObjectName("nlp")
        self.gridLayout.addWidget(self.nlp, 0, 29, 1, 2)
        self.cnp_label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cnp_label_2.setFont(font)
        self.cnp_label_2.setObjectName("cnp_label_2")
        self.gridLayout.addWidget(self.cnp_label_2, 4, 28, 1, 2)
        self.infr_3_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.infr_3_label.setFont(font)
        self.infr_3_label.setObjectName("infr_3_label")
        self.gridLayout.addWidget(self.infr_3_label, 11, 0, 2, 2)
        self.svp_luni = QtWidgets.QSpinBox(self.widget)
        self.svp_luni.setMaximum(11)
        self.svp_luni.setObjectName("svp_luni")
        self.gridLayout.addWidget(self.svp_luni, 6, 17, 1, 5)
        self.data_nastere_inc = QtWidgets.QDateEdit(self.widget)
        self.data_nastere_inc.setObjectName("data_nastere_inc")
        self.gridLayout.addWidget(self.data_nastere_inc, 5, 1, 1, 6)
        self.oblig_1_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.oblig_1_label.setFont(font)
        self.oblig_1_label.setObjectName("oblig_1_label")
        self.gridLayout.addWidget(self.oblig_1_label, 7, 23, 2, 4)
        self.sent_nr = QtWidgets.QLineEdit(self.widget)
        self.sent_nr.setText("")
        self.sent_nr.setDragEnabled(True)
        self.sent_nr.setClearButtonEnabled(True)
        self.sent_nr.setObjectName("sent_nr")
        self.gridLayout.addWidget(self.sent_nr, 3, 14, 1, 4)
        self.ds_svp = QtWidgets.QLabel(self.widget)
        self.ds_svp.setObjectName("ds_svp")
        self.gridLayout.addWidget(self.ds_svp, 2, 10, 1, 5)
        self.re = QtWidgets.QPushButton(self.widget)
        self.re.setFlat(True)
        self.re.setObjectName("re")
        self.gridLayout.addWidget(self.re, 0, 31, 1, 1)
        self.infr_3 = QtWidgets.QLineEdit(self.widget)
        self.infr_3.setObjectName("infr_3")
        self.gridLayout.addWidget(self.infr_3, 12, 2, 1, 21)
        self.dom_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dom_label.setFont(font)
        self.dom_label.setObjectName("dom_label")
        self.gridLayout.addWidget(self.dom_label, 5, 15, 1, 4)
        self.adresa_inc = QtWidgets.QLineEdit(self.widget)
        self.adresa_inc.setObjectName("adresa_inc")
        self.gridLayout.addWidget(self.adresa_inc, 5, 19, 1, 13)
        self.ped_zile = QtWidgets.QSpinBox(self.widget)
        self.ped_zile.setMaximum(29)
        self.ped_zile.setObjectName("ped_zile")
        self.gridLayout.addWidget(self.ped_zile, 6, 8, 1, 3)
        self.ds_inst_label = QtWidgets.QLabel(self.widget)
        self.ds_inst_label.setObjectName("ds_inst_label")
        self.gridLayout.addWidget(self.ds_inst_label, 3, 0, 1, 3)
        self.instit_1_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.instit_1_label.setFont(font)
        self.instit_1_label.setObjectName("instit_1_label")
        self.gridLayout.addWidget(self.instit_1_label, 14, 4, 2, 5)
        self.an_ds_svp = QtWidgets.QComboBox(self.widget)
        self.an_ds_svp.setObjectName("an_ds_svp")
        self.an_ds_svp.addItem("")
        self.an_ds_svp.addItem("")
        self.an_ds_svp.addItem("")
        self.an_ds_svp.addItem("")
        self.gridLayout.addWidget(self.an_ds_svp, 2, 21, 1, 2)
        self.separator = QtWidgets.QLabel(self.widget)
        self.separator.setObjectName("separator")
        self.gridLayout.addWidget(self.separator, 3, 18, 1, 2)
        self.obl_2 = QtWidgets.QLineEdit(self.widget)
        self.obl_2.setObjectName("obl_2")
        self.gridLayout.addWidget(self.obl_2, 10, 26, 1, 6)
        self.nastere_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nastere_label.setFont(font)
        self.nastere_label.setObjectName("nastere_label")
        self.gridLayout.addWidget(self.nastere_label, 5, 0, 1, 1)
        self.infr_2_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.infr_2_label.setFont(font)
        self.infr_2_label.setObjectName("infr_2_label")
        self.gridLayout.addWidget(self.infr_2_label, 9, 0, 2, 2)
        self.oblig_2_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.oblig_2_label.setFont(font)
        self.oblig_2_label.setObjectName("oblig_2_label")
        self.gridLayout.addWidget(self.oblig_2_label, 9, 23, 2, 4)
        self.inc_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.inc_label.setFont(font)
        self.inc_label.setObjectName("inc_label")
        self.gridLayout.addWidget(self.inc_label, 4, 0, 1, 1)
        self.indicativ_ds_inst = QtWidgets.QLineEdit(self.widget)
        self.indicativ_ds_inst.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.indicativ_ds_inst.setDragEnabled(True)
        self.indicativ_ds_inst.setClearButtonEnabled(True)
        self.indicativ_ds_inst.setObjectName("indicativ_ds_inst")
        self.gridLayout.addWidget(self.indicativ_ds_inst, 3, 6, 1, 4)
        self.infr1 = QtWidgets.QLineEdit(self.widget)
        self.infr1.setText("")
        self.infr1.setObjectName("infr1")
        self.gridLayout.addWidget(self.infr1, 8, 2, 1, 21)
        self.CNP = QtWidgets.QLineEdit(self.widget)
        self.CNP.setText("")
        self.CNP.setMaxLength(13)
        self.CNP.setObjectName("CNP")
        self.gridLayout.addWidget(self.CNP, 4, 30, 1, 2)
        self.instit_1 = QtWidgets.QComboBox(self.widget)
        self.instit_1.setObjectName("instit_1")
        self.instit_1.addItem("")
        self.instit_1.addItem("")
        self.instit_1.addItem("")
        self.instit_1.addItem("")
        self.instit_1.addItem("")
        self.instit_1.addItem("")
        self.instit_1.addItem("")
        self.instit_1.addItem("")
        self.instit_1.addItem("")
        self.instit_1.addItem("")
        self.instit_1.addItem("")
        self.instit_1.addItem("")
        self.instit_1.addItem("")
        self.instit_1.addItem("")
        self.instit_1.addItem("")
        self.instit_1.addItem("")
        self.instit_1.addItem("")
        self.instit_1.addItem("")
        self.instit_1.addItem("")
        self.gridLayout.addWidget(self.instit_1, 14, 9, 2, 1)
        self.separator_2 = QtWidgets.QLabel(self.widget)
        self.separator_2.setObjectName("separator_2")
        self.gridLayout.addWidget(self.separator_2, 2, 23, 1, 1)
        self.optiuni_def = QtWidgets.QComboBox(self.widget)
        self.optiuni_def.setObjectName("optiuni_def")
        self.optiuni_def.addItem("")
        self.optiuni_def.addItem("")
        self.gridLayout.addWidget(self.optiuni_def, 3, 27, 1, 5)
        self.nr_ds_svp = QtWidgets.QLineEdit(self.widget)
        self.nr_ds_svp.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.nr_ds_svp.setDragEnabled(True)
        self.nr_ds_svp.setPlaceholderText("")
        self.nr_ds_svp.setClearButtonEnabled(True)
        self.nr_ds_svp.setObjectName("nr_ds_svp")
        self.gridLayout.addWidget(self.nr_ds_svp, 2, 15, 1, 3)
        self.loc_nastere_inc = QtWidgets.QLineEdit(self.widget)
        self.loc_nastere_inc.setObjectName("loc_nastere_inc")
        self.gridLayout.addWidget(self.loc_nastere_inc, 5, 7, 1, 6)
        self.zile_mfc = QtWidgets.QSpinBox(self.widget)
        self.zile_mfc.setMinimum(30)
        self.zile_mfc.setMaximum(120)
        self.zile_mfc.setProperty("value", 60)
        self.zile_mfc.setObjectName("zile_mfc")
        self.gridLayout.addWidget(self.zile_mfc, 14, 0, 2, 4)
        self.svp_zile = QtWidgets.QSpinBox(self.widget)
        self.svp_zile.setMaximum(29)
        self.svp_zile.setObjectName("svp_zile")
        self.gridLayout.addWidget(self.svp_zile, 6, 22, 1, 4)
        self.infr_1_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.infr_1_label.setFont(font)
        self.infr_1_label.setObjectName("infr_1_label")
        self.gridLayout.addWidget(self.infr_1_label, 7, 0, 2, 2)
        self.data_ds_svp = QtWidgets.QDateEdit(self.widget)
        self.data_ds_svp.setObjectName("data_ds_svp")
        self.gridLayout.addWidget(self.data_ds_svp, 2, 24, 1, 3)
        self.separator_1 = QtWidgets.QLabel(self.widget)
        self.separator_1.setObjectName("separator_1")
        self.gridLayout.addWidget(self.separator_1, 2, 19, 1, 2)
        self.data_ds_svp_3 = QtWidgets.QDateEdit(self.widget)
        self.data_ds_svp_3.setObjectName("data_ds_svp_3")
        self.gridLayout.addWidget(self.data_ds_svp_3, 3, 20, 1, 5)
        self.copy = QtWidgets.QLabel(self.widget)
        self.copy.setObjectName("copy")
        self.gridLayout.addWidget(self.copy, 18, 16, 1, 1)
        self.stiu_msj = QtWidgets.QCheckBox(self.widget)
        self.stiu_msj.setCheckable(True)
        self.stiu_msj.setChecked(False)
        self.stiu_msj.setTristate(False)
        self.stiu_msj.setObjectName("stiu_msj")
        self.gridLayout.addWidget(self.stiu_msj, 1, 0, 1, 12)
        self.svp_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.svp_label.setFont(font)
        self.svp_label.setObjectName("svp_label")
        self.gridLayout.addWidget(self.svp_label, 6, 11, 1, 4)
        self.sent_inc = QtWidgets.QLabel(self.widget)
        self.sent_inc.setObjectName("sent_inc")
        self.gridLayout.addWidget(self.sent_inc, 0, 9, 1, 20)
        self.instit_2 = QtWidgets.QComboBox(self.widget)
        self.instit_2.setObjectName("instit_2")
        self.instit_2.addItem("")
        self.instit_2.addItem("")
        self.instit_2.addItem("")
        self.instit_2.addItem("")
        self.instit_2.addItem("")
        self.instit_2.addItem("")
        self.instit_2.addItem("")
        self.instit_2.addItem("")
        self.instit_2.addItem("")
        self.instit_2.addItem("")
        self.instit_2.addItem("")
        self.instit_2.addItem("")
        self.instit_2.addItem("")
        self.instit_2.addItem("")
        self.instit_2.addItem("")
        self.instit_2.addItem("")
        self.instit_2.addItem("")
        self.instit_2.addItem("")
        self.instit_2.addItem("")
        self.gridLayout.addWidget(self.instit_2, 15, 31, 1, 1)
        self.svp_ani = QtWidgets.QSpinBox(self.widget)
        self.svp_ani.setMaximum(4)
        self.svp_ani.setProperty("value", 2)
        self.svp_ani.setObjectName("svp_ani")
        self.gridLayout.addWidget(self.svp_ani, 6, 15, 1, 2)
        self.infr2 = QtWidgets.QLineEdit(self.widget)
        self.infr2.setObjectName("infr2")
        self.gridLayout.addWidget(self.infr2, 10, 2, 1, 21)
        self.ped_an = QtWidgets.QSpinBox(self.widget)
        self.ped_an.setPrefix("")
        self.ped_an.setMinimum(0)
        self.ped_an.setMaximum(3)
        self.ped_an.setProperty("value", 0)
        self.ped_an.setObjectName("ped_an")
        self.gridLayout.addWidget(self.ped_an, 6, 1, 1, 4)
        self.ped_luni = QtWidgets.QSpinBox(self.widget)
        self.ped_luni.setMaximum(11)
        self.ped_luni.setObjectName("ped_luni")
        self.gridLayout.addWidget(self.ped_luni, 6, 5, 1, 3)
        self.nr_ds_inst = QtWidgets.QLineEdit(self.widget)
        self.nr_ds_inst.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.nr_ds_inst.setDragEnabled(True)
        self.nr_ds_inst.setClearButtonEnabled(True)
        self.nr_ds_inst.setObjectName("nr_ds_inst")
        self.gridLayout.addWidget(self.nr_ds_inst, 3, 3, 1, 3)
        self.obl_3 = QtWidgets.QLineEdit(self.widget)
        self.obl_3.setObjectName("obl_3")
        self.gridLayout.addWidget(self.obl_3, 12, 26, 1, 6)
        self.ped_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ped_label.setFont(font)
        self.ped_label.setObjectName("ped_label")
        self.gridLayout.addWidget(self.ped_label, 6, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 17, 16, 1, 1)
        Macheta.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Macheta)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1816, 28))
        self.menubar.setObjectName("menubar")
        Macheta.setMenuBar(self.menubar)

        self.retranslateUi(Macheta)
        QtCore.QMetaObject.connectSlotsByName(Macheta)
        Macheta.setTabOrder(self.nr_ds_svp, self.an_ds_svp)
        Macheta.setTabOrder(self.an_ds_svp, self.data_ds_svp)
        Macheta.setTabOrder(self.data_ds_svp, self.nr_ds_inst)
        Macheta.setTabOrder(self.nr_ds_inst, self.indicativ_ds_inst)
        Macheta.setTabOrder(self.indicativ_ds_inst, self.an_ds_instanta)
        Macheta.setTabOrder(self.an_ds_instanta, self.sent_nr)
        Macheta.setTabOrder(self.sent_nr, self.data_ds_svp_3)
        Macheta.setTabOrder(self.data_ds_svp_3, self.optiuni_def)
        Macheta.setTabOrder(self.optiuni_def, self.nume_inc)
        Macheta.setTabOrder(self.nume_inc, self.nume_parinti_inc)
        Macheta.setTabOrder(self.nume_parinti_inc, self.CNP)
        Macheta.setTabOrder(self.CNP, self.data_nastere_inc)
        Macheta.setTabOrder(self.data_nastere_inc, self.loc_nastere_inc)
        Macheta.setTabOrder(self.loc_nastere_inc, self.adresa_inc)
        Macheta.setTabOrder(self.adresa_inc, self.ped_an)
        Macheta.setTabOrder(self.ped_an, self.ped_luni)
        Macheta.setTabOrder(self.ped_luni, self.ped_zile)
        Macheta.setTabOrder(self.ped_zile, self.svp_ani)
        Macheta.setTabOrder(self.svp_ani, self.svp_luni)
        Macheta.setTabOrder(self.svp_luni, self.svp_zile)
        Macheta.setTabOrder(self.svp_zile, self.infr1)
        Macheta.setTabOrder(self.infr1, self.infr2)
        Macheta.setTabOrder(self.infr2, self.infr_3)
        Macheta.setTabOrder(self.infr_3, self.obl_1)
        Macheta.setTabOrder(self.obl_1, self.obl_2)
        Macheta.setTabOrder(self.obl_2, self.obl_3)
        Macheta.setTabOrder(self.obl_3, self.zile_mfc)
        Macheta.setTabOrder(self.zile_mfc, self.instit_1)
        Macheta.setTabOrder(self.instit_1, self.instit_2)
        Macheta.setTabOrder(self.instit_2, self.inc_doc)
        Macheta.setTabOrder(self.inc_doc, self.stiu_msj)
        Macheta.setTabOrder(self.stiu_msj, self.nlp)
        Macheta.setTabOrder(self.nlp, self.re)

    def retranslateUi(self, Macheta):
        _translate = QtCore.QCoreApplication.translate
        Macheta.setWindowTitle(_translate("Macheta", "MainWindow"))
        self.def_label.setText(_translate("Macheta", "Definitivă prin:"))
        self.nume_parinti_inc.setPlaceholderText(_translate("Macheta", "prenume părinți inculpat"))
        self.parinti_label.setText(_translate("Macheta", "părinți:"))
        self.nume_inc.setPlaceholderText(_translate("Macheta", "nume prenume inculpat"))
        self.oblig_3_label.setWhatsThis(_translate("Macheta", "Fără MFC!"))
        self.oblig_3_label.setText(_translate("Macheta", "Obligații"))
        self.inc_doc.setToolTip(_translate("Macheta", "Dacă ai o sentință o poți adugă pentru preluarea datelor"))
        self.inc_doc.setText(_translate("Macheta", "Încarcă documentul"))
        self.obl_1.setPlaceholderText(_translate("Macheta", "inclusiv MFC"))
        self.an_ds_instanta.setToolTip(_translate("Macheta", "<html><head/><body><p>an dosar instanță</p></body></html>"))
        self.an_ds_instanta.setWhatsThis(_translate("Macheta", "<html><head/><body><p>Dosarul de instanță are trei părți.</p><p>100/300/2020</p><p>100 = numărul dosarului</p><p>300 = indicativul instanței</p><p>2020 = anul dosarului</p></body></html>"))
        self.an_ds_instanta.setItemText(0, _translate("Macheta", "2021"))
        self.an_ds_instanta.setItemText(1, _translate("Macheta", "2018"))
        self.an_ds_instanta.setItemText(2, _translate("Macheta", "2019"))
        self.an_ds_instanta.setItemText(3, _translate("Macheta", "2020"))
        self.sent_label.setText(_translate("Macheta", "Sentință"))
        self.instit_2_label.setText(_translate("Macheta", "Instit MFC 2"))
        self.nlp.setToolTip(_translate("Macheta", "Procesarea Limbajului Natural"))
        self.nlp.setText(_translate("Macheta", "NLP"))
        self.cnp_label_2.setText(_translate("Macheta", "CNP:"))
        self.infr_3_label.setText(_translate("Macheta", "Infracțiune 3"))
        self.svp_luni.setSuffix(_translate("Macheta", " luni"))
        self.oblig_1_label.setWhatsThis(_translate("Macheta", "Fără MFC!"))
        self.oblig_1_label.setText(_translate("Macheta", "Obligații"))
        self.sent_nr.setPlaceholderText(_translate("Macheta", "număr"))
        self.ds_svp.setText(_translate("Macheta", "Dosar supraveghere"))
        self.re.setToolTip(_translate("Macheta", "Expresii Regulate"))
        self.re.setText(_translate("Macheta", "RE"))
        self.infr_3.setPlaceholderText(_translate("Macheta", "articol infracțiune"))
        self.dom_label.setText(_translate("Macheta", "Domiciliu:"))
        self.adresa_inc.setToolTip(_translate("Macheta", "<html><head/><body><p>Lăsați sectorul ultimul!</p></body></html>"))
        self.adresa_inc.setText(_translate("Macheta", "București, "))
        self.adresa_inc.setPlaceholderText(_translate("Macheta", "adresă inculpat"))
        self.ped_zile.setSuffix(_translate("Macheta", " zile"))
        self.ds_inst_label.setText(_translate("Macheta", "Dosar instanță:"))
        self.instit_1_label.setText(_translate("Macheta", "Instit MFC 1"))
        self.an_ds_svp.setItemText(0, _translate("Macheta", "2021"))
        self.an_ds_svp.setItemText(1, _translate("Macheta", "2018"))
        self.an_ds_svp.setItemText(2, _translate("Macheta", "2019"))
        self.an_ds_svp.setItemText(3, _translate("Macheta", "2020"))
        self.separator.setText(_translate("Macheta", "/"))
        self.obl_2.setPlaceholderText(_translate("Macheta", "inclusiv MFC"))
        self.nastere_label.setText(_translate("Macheta", "Naștere:"))
        self.infr_2_label.setText(_translate("Macheta", "Infracțiune 2"))
        self.oblig_2_label.setWhatsThis(_translate("Macheta", "Fără MFC!"))
        self.oblig_2_label.setText(_translate("Macheta", "Obligații"))
        self.inc_label.setText(_translate("Macheta", "Inculpat:"))
        self.indicativ_ds_inst.setToolTip(_translate("Macheta", "<html><head/><body><p>Numărul dintre &quot;/&quot;</p></body></html>"))
        self.indicativ_ds_inst.setWhatsThis(_translate("Macheta", "<html><head/><body><p>Dosarul de instanță are trei părți.</p><p>100/300/2020</p><p>100 = numărul dosarului</p><p>300 = indicativul instanței</p><p>2020 = anul dosarului</p><p><br/></p></body></html>"))
        self.indicativ_ds_inst.setPlaceholderText(_translate("Macheta", "indicativ"))
        self.infr1.setPlaceholderText(_translate("Macheta", "articol infracțiune"))
        self.instit_1.setItemText(0, _translate("Macheta", "Administrația Domeniului Public București-Sector I"))
        self.instit_1.setItemText(1, _translate("Macheta", "Administrația Domeniului Public București-Sector II"))
        self.instit_1.setItemText(2, _translate("Macheta", "Administrația Domeniului Public București-Sector II"))
        self.instit_1.setItemText(3, _translate("Macheta", "Administrația Domeniului Public București-Sector IV"))
        self.instit_1.setItemText(4, _translate("Macheta", "SC Amenajare Edilitară și Salubrizare SA Sector V"))
        self.instit_1.setItemText(5, _translate("Macheta", "Administrația Domeniului Public și Dezvoltare Urbană Sector 6"))
        self.instit_1.setItemText(6, _translate("Macheta", "Direcția Generală de Asistență Socială și Protecție a Copilului Sector I"))
        self.instit_1.setItemText(7, _translate("Macheta", "Direcția Generală de Asistență Socială și Protecție a Copilului Sector II"))
        self.instit_1.setItemText(8, _translate("Macheta", "Direcția Generală de Asistență Socială și Protecție a Copilului Sector III"))
        self.instit_1.setItemText(9, _translate("Macheta", "Direcția Generală de Asistență Socială și Protecție a Copilului Sector IV"))
        self.instit_1.setItemText(10, _translate("Macheta", "Direcția Generală de Asistență Socială și Protecție a Copilului Sector V"))
        self.instit_1.setItemText(11, _translate("Macheta", "Direcția Generală de Asistență Socială și Protecție a Copilului Sector VI"))
        self.instit_1.setItemText(12, _translate("Macheta", "Administrația Lacuri, Parcuri și Agrement București"))
        self.instit_1.setItemText(13, _translate("Macheta", "Poliția Locală a Sectorului I"))
        self.instit_1.setItemText(14, _translate("Macheta", "Fundația pentru Promovarea Sancțiunilor Comunitare"))
        self.instit_1.setItemText(15, _translate("Macheta", "Administrația Cimitirelor și Crematoriilor Umane"))
        self.instit_1.setItemText(16, _translate("Macheta", "Arhiepiscopia Bucureștilor"))
        self.instit_1.setItemText(17, _translate("Macheta", "La alegerea SP"))
        self.instit_1.setItemText(18, _translate("Macheta", "în afara comeptentei SP"))
        self.separator_2.setText(_translate("Macheta", "/"))
        self.optiuni_def.setItemText(0, _translate("Macheta", "neapelare la data de"))
        self.optiuni_def.setItemText(1, _translate("Macheta", "decizia penală nr.:"))
        self.nr_ds_svp.setToolTip(_translate("Macheta", "<html><head/><body><p>Daca nr dosarului e 1/SP/S/2020 aici scrii 1</p></body></html>"))
        self.nr_ds_svp.setWhatsThis(_translate("Macheta", "<html><head/><body><p>Numărul dosarului este format din trei elemente: numar înregistrare/indicativ instanta / an dosar. </p><p><br/></p><p>Să luam ca exemplu dosarul 1/300/2020</p><p><br/></p><p>1 = numărul de înregistrare al dosarului la instanță</p><p>300 = indicativul instanței (300 este indicativul JS2). Orice dosar va avea indicativul instantei de fond</p><p>2020 = anul înregistrării dosarului</p></body></html>"))
        self.loc_nastere_inc.setPlaceholderText(_translate("Macheta", "loc nastere inculpat"))
        self.zile_mfc.setSuffix(_translate("Macheta", " zile MFC"))
        self.svp_zile.setSuffix(_translate("Macheta", " zile"))
        self.infr_1_label.setText(_translate("Macheta", "Infracțiune 1"))
        self.separator_1.setText(_translate("Macheta", "/"))
        self.copy.setText(_translate("Macheta", "<html><head/><body><p><span style=\" font-size:9pt; color:#1b24d5;\">Program creat de Alexandru Manole</span></p></body></html>"))
        self.stiu_msj.setToolTip(_translate("Macheta", "<html><head/><body><p>Dacă ați văzut mesajul când apăsați &quot;Încarcă documentul&quot; puteți să bifați</p></body></html>"))
        self.stiu_msj.setText(_translate("Macheta", "Știu deja tot ceea ce e de știut!"))
        self.svp_label.setText(_translate("Macheta", "Supraveghere:"))
        self.sent_inc.setText(_translate("Macheta", "Nicio sentință încărcată"))
        self.instit_2.setItemText(0, _translate("Macheta", "Administrația Domeniului Public București-Sector I"))
        self.instit_2.setItemText(1, _translate("Macheta", "Administrația Domeniului Public București-Sector II"))
        self.instit_2.setItemText(2, _translate("Macheta", "Administrația Domeniului Public București-Sector II"))
        self.instit_2.setItemText(3, _translate("Macheta", "Administrația Domeniului Public București-Sector IV"))
        self.instit_2.setItemText(4, _translate("Macheta", "SC Amenajare Edilitară și Salubrizare SA Sector V"))
        self.instit_2.setItemText(5, _translate("Macheta", "Administrația Domeniului Public și Dezvoltare Urbană Sector 6"))
        self.instit_2.setItemText(6, _translate("Macheta", "Direcția Generală de Asistență Socială și Protecție a Protecția a Copilului Sector I"))
        self.instit_2.setItemText(7, _translate("Macheta", "Direcția Generală de Asistență Socială și Protecție a Protecția a Copilului Sector II"))
        self.instit_2.setItemText(8, _translate("Macheta", "Direcția Generală de Asistență Socială și Protecție a Protecția a Copilului Sector III"))
        self.instit_2.setItemText(9, _translate("Macheta", "Direcția Generală de Asistență Socială și Protecție a Protecția a Copilului Sector IV"))
        self.instit_2.setItemText(10, _translate("Macheta", "Direcția Generală de Asistență Socială și Protecție a Protecția a Copilului Sector V"))
        self.instit_2.setItemText(11, _translate("Macheta", "Direcția Generală de Asistență Socială și Protecție a Protecția a Copilului Sector VI"))
        self.instit_2.setItemText(12, _translate("Macheta", "Administrația Lacuri, Parcuri și Agrement București"))
        self.instit_2.setItemText(13, _translate("Macheta", "Poliția Locală a Sectorului I"))
        self.instit_2.setItemText(14, _translate("Macheta", "Fundația pentru Promovarea Sancțiunilor Comunitare"))
        self.instit_2.setItemText(15, _translate("Macheta", "Administrația Cimitirelor și Crematoriilor Umane"))
        self.instit_2.setItemText(16, _translate("Macheta", "Arhiepiscopia Bucureștilor"))
        self.instit_2.setItemText(17, _translate("Macheta", "La alegerea SP"))
        self.instit_2.setItemText(18, _translate("Macheta", "în afara comeptentei SP"))
        self.svp_ani.setSuffix(_translate("Macheta", " ani"))
        self.infr2.setPlaceholderText(_translate("Macheta", "articol infracțiune"))
        self.ped_an.setSuffix(_translate("Macheta", " ani"))
        self.ped_luni.setSuffix(_translate("Macheta", " luni"))
        self.nr_ds_inst.setToolTip(_translate("Macheta", "<html><head/><body><p>Prima parte a numărului dosarului</p></body></html>"))
        self.nr_ds_inst.setWhatsThis(_translate("Macheta", "<html><head/><body><p>Dosarul de instanță are trei părți.</p><p>100/300/2020</p><p>100 = numărul dosarului</p><p>300 = indicativul instanței</p><p>2020 = anul dosarului</p><p><br/></p></body></html>"))
        self.nr_ds_inst.setPlaceholderText(_translate("Macheta", "număr"))
        self.obl_3.setPlaceholderText(_translate("Macheta", "inclusiv MFC"))
        self.ped_label.setText(_translate("Macheta", "Pedeapsa:"))
        self.pushButton.setText(_translate("Macheta", "CREEAZĂ DOSAR ȘI LISTA  "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Macheta = QtWidgets.QMainWindow()
    ui = Ui_Macheta()
    ui.setupUi(Macheta)
    Macheta.show()
    sys.exit(app.exec_())
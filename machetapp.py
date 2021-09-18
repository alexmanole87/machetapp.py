# from PyQt5.QtGui import QKeyEvent
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QFileDialog
from selenium import webdriver
from selenium.webdriver.support.select import Select

from functii import *
# from interfata_grafica_macheta import *
from interfata_grafica_macheta_v3 import *
from splash import *
from vars import *

counter = 0
cfg = ConfigParser()
cfg.read('config.ini')


def nume_inst(ind):
    return toate_instantele[ind]


def set_dir_():
    dir_ = QFileDialog.getExistingDirectory()
    return dir_


class MachetaPyQt5(Ui_Macheta):
    def __init__(self, window2):
        self.setupUi(window2)
        self.creere_doc.clicked.connect(self.sern_lista)
        self.optiuni_def.currentTextChanged.connect(self.sel_def)
        self.nr_sent_apel.hide()
        self.data_def_apel.hide()
        self.separator_3.hide()
        self.iac1.hide()
        self.iac2.hide()
        self.svp_luni_minor.hide()
        self.svp_zile_minori.hide()
        self.indiv_ped_minori.hide()
        self.zile_amenda.hide()
        self.label_inmultire.hide()
        self.amenda_val.hide()
        self.zile_coada.hide()
        self.label.hide()
        self.infr1.setCompleter(self.auto_complete_infr)
        self.infr2.setCompleter(self.auto_complete_infr)
        self.infr_3.setCompleter(self.auto_complete_infr)
        self.obl_1.setCompleter(self.auto_complete_obl)
        self.obl_2.setCompleter(self.auto_complete_obl)
        self.obl_3.setCompleter(self.auto_complete_obl)
        self.obl_4.setCompleter(self.auto_complete_obl)
        self.studii_nesc.stateChanged.connect(self.disable_by_studii_nesc)
        # self.studii_nesc.keyPressEvent(self.keyPressEvent)
        self.studii_clase.valueChanged.connect(self.disable_by_studii_c)
        self.studii_s.stateChanged.connect(self.disable_by_studii_s)
        self.ped_an.valueChanged.connect(self.ped_singular_plural)
        self.ped_an.valueChanged.connect(self.disable)
        self.ped_luni.valueChanged.connect(self.ped_singular_plural)
        self.ped_zile.valueChanged.connect(self.ped_singular_plural)
        self.svp_ani.valueChanged.connect(self.svp_singular_plural)
        self.svp_ani.valueChanged.connect(self.disable)
        self.zile_coada.valueChanged.connect(self.calcul_treime)
        self.svp_luni.valueChanged.connect(self.svp_singular_plural)
        self.svp_zile.valueChanged.connect(self.svp_singular_plural)
        self.svp_luni_minor.valueChanged.connect(self.svp_singular_plural)
        self.svp_zile_minori.valueChanged.connect(self.svp_singular_plural)
        self.svp_luni_minor.valueChanged.connect(self.disable)
        self.instit_1.currentTextChanged.connect(self.show_iac1)
        self.instit_2.currentTextChanged.connect(self.show_iac2)
        self.indiv_ped.currentTextChanged.connect(self.disable)
        self.minor_major.currentTextChanged.connect(self.show_minori)
        self.zile_coada.valueChanged.connect(self.calcul_treime)
        self.obl_1.textChanged.connect(self.mfc_h)
        self.zile_mfc.setDisabled(True)
        self.zile_mfc.setMaximum(0)
        self.zile_mfc.setValue(0)
        self.instit_1.setCurrentText('')
        self.instit_2.setCurrentText('')
        # self.actionDosar_de_lucru.triggered.connect(self.set_dir_)

    def sector(self):
        return self.adresa_inc.text()[-1]

    def ds_suprav_func(self):
        return self.nr_ds_svp.text() + "/" + self.an_ds_svp.currentText() + "/S" + "   " + self.data_ds_svp.text()

    def studii_func(self):
        if self.studii_nesc.isChecked():
            return "neșcolarizat"
        elif self.studii_s.isChecked():
            return "studii superioare"
        elif int(self.studii_clase.text()[:2]) > 0:
            return self.studii_clase.text()

    def ds_pen(self):
        return self.nr_ds_inst.text() + '/' + self.indicativ_ds_inst.text() + '/' + self.an_ds_instanta.currentText()

    def sentinata_fun(self):
        return self.sent_nr.text() + '/' + self.data_sent.text()

    def sel_def(self):
        if self.optiuni_def.currentText() == 'decizia penală nr.:':
            self.nr_sent_apel.show()
            self.data_def_neapelare.hide()
            self.data_def_apel.show()
            self.separator_3.show()
        else:
            self.nr_sent_apel.hide()
            self.data_def_neapelare.show()
            self.data_def_apel.hide()
            self.separator_3.hide()

    def disable(self):
        if self.minor_major.currentText() == "Major":
            # limit pedeapsa
            if self.ped_an.text() == '3 ani':
                self.ped_luni.setMaximum(0)
                self.ped_zile.setMaximum(0)
            else:
                self.ped_luni.setMaximum(11)
                self.ped_zile.setMaximum(30)
            # limit supraveghere
            if self.svp_ani.text() == '4 ani':
                self.svp_luni.setMaximum(0)
                self.svp_zile.setMaximum(0)
            else:
                self.svp_luni.setMaximum(11)
                self.svp_zile.setMaximum(30)

            def show(self):
                self.ped_an.show()
                self.ped_an.show()
                self.ped_luni.show()
                self.ped_zile.show()
                self.ped_label.show()

            def hide(self):
                self.label.hide()
                self.zile_amenda.hide()
                self.label_inmultire.hide()
                self.amenda_val.hide()
                self.zile_coada.hide()

            def doi_ani(self):
                # ani
                self.svp_ani.setMinimum(2)
                self.svp_ani.setMaximum(2)
                # luni
                self.svp_luni.setMinimum(0)
                self.svp_luni.setMaximum(0)
                # zile
                self.svp_zile.setMinimum(0)
                self.svp_zile.setMaximum(0)

            def patru_ani(self):
                # ani
                self.svp_ani.setMinimum(2)
                self.svp_ani.setMaximum(4)
                # luni
                self.svp_luni.setMinimum(0)
                self.svp_luni.setMaximum(11)
                # zile
                self.svp_zile.setMinimum(0)
                self.svp_zile.setMaximum(29)

            # limit de la amanare
            if self.indiv_ped.currentText() == "Suspendarea executării pedepsei":
                show(self)
                hide(self)
                patru_ani(self)

            if self.indiv_ped.currentText() == "Amânarea aplicării pedepsei":
                show(self)
                hide(self)
                doi_ani(self)

            if self.indiv_ped.currentText() == "Liberarea condiţionată":
                self.ped_label.hide()
                self.ped_an.hide()
                self.ped_luni.hide()
                self.ped_zile.hide()
                self.label.show()
                self.zile_coada.show()
                self.zile_amenda.hide()
                self.label_inmultire.hide()
                self.amenda_val.hide()
                self.svp_ani.setMinimum(0)
                self.svp_ani.setMaximum(9)

            if self.indiv_ped.currentText() == "Înlocuirea amenzii cu mfc":
                self.ped_an.hide()
                self.ped_luni.hide()
                self.ped_zile.hide()
                self.zile_coada.hide()
                self.zile_amenda.show()
                self.ped_label.show()
                self.label_inmultire.show()
                self.label.hide()
                self.amenda_val.show()
                doi_ani(self)
        else:
            if self.svp_luni_minor.text() == '6 luni':
                self.svp_zile_minori.setMaximum(0)
                self.svp_zile_minori.setMaximum(0)
            else:
                self.svp_zile_minori.setMaximum(11)
                self.svp_zile_minori.setMaximum(30)

    def calcul_treime(self):
        treime_zile = None
        if len(self.zile_coada.text()) == 8:
            treime_zile = int(self.zile_coada.text()[0:4]) // 3
        if len(self.zile_coada.text()) == 9:
            treime_zile = int(self.zile_coada.text()[0:5]) // 3

        years = treime_zile // 360
        months = (treime_zile - years * 360) // 30
        days = (treime_zile - years * 360 - months * 30)

        self.svp_ani.setValue(years)
        self.svp_luni.setValue(months)
        self.svp_zile.setValue(days)

    def disable_by_studii_nesc(self):
        if self.studii_nesc.isChecked():
            self.studii_clase.setMinimum(0)
            self.studii_clase.setValue(0)
            self.studii_clase.setDisabled(True)
            self.studii_s.setDisabled(True)
        else:
            self.studii_clase.setMinimum(1)
            self.studii_clase.setValue(1)
            self.studii_clase.setEnabled(True)
            self.studii_s.setEnabled(True)

    def disable_by_studii_c(self):
        if int(self.studii_clase.text()[0]) > 0:
            self.studii_nesc.setDisabled(True)
            self.studii_s.setDisabled(True)
        else:
            self.studii_nesc.setDisabled(False)
            self.studii_s.setDisabled(False)

    def disable_by_studii_s(self):
        if self.studii_s.isChecked():
            self.studii_nesc.setDisabled(True)
            self.studii_clase.setDisabled(True)
        else:
            self.studii_nesc.setDisabled(False)
            self.studii_clase.setDisabled(False)

    def key_ev(self, event):
        if event.key() == Qt.K:
            self.enable_all_studii()

    def enable_all_studii(self):
        self.studii_clase.setMinimum(1)
        self.studii_clase.setValue(1)
        self.studii_clase.setEnabled(True)
        self.studii_s.setEnabled(True)
        self.studii_nesc.setDisabled(False)
        self.studii_s.setDisabled(False)
        self.studii_nesc.setDisabled(False)
        self.studii_clase.setDisabled(False)

    def data_mod_def_func(self, sel):
        if self.minor_major.currentText() == 'Major':
            return 'neapelare la data de ' + self.data_def_neapelare.text() if sel == 'neapelare la data de' else 'Decizia penală nr.:' + self.nr_sent_apel.text() + '/' + self.data_def_apel.text()
        else:
            return self.data_def_neapelare.text()

    def data_def(self, sel):
        return self.data_def_neapelare.text() if sel == 'neapelare la data de' else self.data_def_apel.text()

    def ped_singular_plural(self):
        if int(self.ped_an.text()[0]) == 1:
            self.ped_an.setSuffix(' an')
        else:
            self.ped_an.setSuffix(' ani')

        if int(self.ped_luni.text()[0:2]) == 1:
            self.ped_luni.setSuffix(' lună')
        else:
            self.ped_luni.setSuffix(' luni')

        if int(self.ped_zile.text()[0:2]) == 1:
            self.ped_zile.setSuffix(' zi')
        else:
            self.ped_zile.setSuffix(' zile')

    def pedeapsa_func(self):
        ani = int(self.ped_an.text()[0])
        luni = int(self.ped_luni.text()[0])
        zile = int(self.ped_zile.text()[0])
        if zile == 0 and luni == 0:
            return self.ped_an.text()
        # ani si luni
        elif zile == 0 and luni != 0:
            return self.ped_an.text() + 'și ' + self.ped_luni.text()
        # ani, luni, zile
        elif zile != 0 and self.ped_luni != 0 and ani != 0:
            return self.ped_an.text() + ', ' + self.ped_luni.text() + ' și ' + self.ped_zile.text()

    def indicativ(self):
        if self.minor_major.currentText() == 'Major':
            if self.indiv_ped.currentText() == "Suspendarea executării pedepsei":
                return 'S' + ' - ' + str(int(self.svp_ani.text()[:2]) * 12 + int(self.svp_luni.text()[:2]))
            elif self.indiv_ped.currentText() == "Amânarea aplicării pedepsei":
                return 'A - 24'
            elif self.indiv_ped.currentText() == "Liberarea condiţionată":
                return 'LC' + ' - ' + str(
                    int(self.svp_ani.text()[:2]) * 12 + int(self.svp_luni.text()[:2]) + int(self.svp_zile.text()[:2]))
            elif self.indiv_ped.currentText() == "Înlocuirea amenzii cu mfc":
                return 'IA - 24'
        else:
            if self.indiv_ped_minori.currentText() == "Suravegherea":
                return self.indiv_ped_minori.currentText() + ' ' + self.svp_luni_minor.text()[:2]
            elif self.indiv_ped_minori.currentText() == "Asistarea zilnică":
                return 'AZ' + '-' + self.svp_luni_minor.text()[:2]
            elif self.indiv_ped_minori.currentText() == "Stagiul de formare civică":
                return 'SFC' + '-' + self.svp_luni_minor.text()[:2]
            elif self.indiv_ped_minori.currentText() == "Consemnarea la sfârșit de săptămână":
                return 'CLSS' + '-' + self.svp_luni_minor.text()[:2]

    def ts(self):
        luni = int(self.svp_luni.text()[0])
        zile = int(self.svp_zile.text()[0])
        luni_minori = int(self.svp_luni_minor.text()[0])
        zile_minori = int(self.svp_zile_minori.text()[0:2])
        if self.minor_major.currentText() == 'Major':
            # 2 ani, 2 luni și 2 zile
            if luni > 0 and zile > 0:
                return self.svp_ani.text() + ' , ' + self.svp_luni.text() + ' și ' + self.svp_zile.text()
            # 2 ani si 2 luni
            elif luni > 0 and zile == 0:
                return self.svp_ani.text() + ' și ' + self.svp_luni.text()
            # 2 ani
            elif luni == 0 and zile == 0:
                return self.svp_ani.text()
        else:
            if luni_minori > 0 and zile_minori > 0:
                return self.svp_luni_minor.text() + ' și ' + self.svp_zile_minori.text()
            elif luni_minori > 0 and zile_minori == 0:
                return self.svp_luni_minor.text()
            elif luni_minori == 0 and zile_minori > 0:
                return self.svp_zile_minori.text()

    def svp_singular_plural(self):
        # print(int(self.svp_zile_minori.text()[0]))
        if int(self.svp_ani.text()[0]) == 1:
            self.svp_ani.setSuffix(' an')
        else:
            self.svp_ani.setSuffix(' ani')

        if int(self.svp_luni.text()[0:2]) == 1:
            self.svp_luni.setSuffix(' lună')
        else:
            self.svp_luni.setSuffix(' luni')

        if int(self.svp_zile.text()[0:2]) == 1:
            self.svp_zile.setSuffix(' zi')
        else:
            self.svp_zile.setSuffix(' zile')

        if int(self.svp_luni_minor.text()[0]) == 1:
            self.svp_luni_minor.setSuffix(' lună')
        else:
            self.svp_luni_minor.setSuffix(' luni')

        if int(self.svp_zile_minori.text()[0:2]) == 1:
            self.svp_zile_minori.setSuffix(' zi')
        else:
            self.svp_zile_minori.setSuffix(' zile')

    def mfc_zile(self):
        if self.obl_1.text() == 'să presteze o muncă neremunerată în folosul comunităţii, pe o perioadă cuprinsă între 30 și 60 de zile' or self.obl_1.text() == 'să presteze o muncă neremunerată în folosul comunităţii, pe o perioadă cuprinsă între 60 și 120 de zile':
            return self.zile_mfc.text()
        else:
            return "nothing"

    def mfc_h(self):
        if self.obl_1.text() == "să presteze o muncă neremunerată în folosul comunităţii, pe o perioadă cuprinsă între 30 și 60 de zile":
            self.zile_mfc.setMinimum(30)
            self.zile_mfc.setMaximum(60)
            self.zile_mfc.setValue(30)
            self.zile_mfc.setDisabled(False)
            ore = int(self.zile_mfc.text()[0:3]) * 2
            return str(ore)
        if self.obl_1.text() == "să presteze o muncă neremunerată în folosul comunităţii, pe o perioadă cuprinsă între 60 și 120 de zile":
            self.zile_mfc.setMinimum(60)
            self.zile_mfc.setMaximum(120)
            self.zile_mfc.setValue(60)
            self.zile_mfc.setDisabled(False)
            ore = int(self.zile_mfc.text()[0:3]) * 2
            return str(ore)
        if self.obl_1.text() != "să presteze o muncă neremunerată în folosul comunităţii, pe o perioadă cuprinsă între 30 și 60 de zile" or self.obl_1.text() != "să presteze o muncă neremunerată în folosul comunităţii, pe o perioadă cuprinsă între 60 și 120 de zile":
            self.zile_mfc.setDisabled(True)
            self.zile_mfc.setMaximum(0)
            self.zile_mfc.setValue(0)
            self.instit_1.setCurrentText('')
            self.instit_2.setCurrentText('')
            return ''

    def obl_func(self):
        obligatii_ = [self.obl_1.text(), self.obl_2.text(), self.obl_3.text()]
        return str(obligatii_)[2:-2]

    def fin_svp(self):
        data_inceput_dateobj = datetime.datetime.strptime(self.data_def(self.optiuni_def.currentText()), '%d.%m.%Y')
        if self.minor_major.currentText() == 'Major':
            zile = lambda: (int(self.svp_ani.text()[:1]) * 365 + int(self.svp_luni.text()[:2]) * 30) - 1
            data_fin = (data_inceput_dateobj + datetime.timedelta(days=zile())).strftime('%d.%m.%Y')
            return data_fin
        else:
            zile = lambda: (int(self.svp_luni_minor.text()[:1]) * 30 + int(self.svp_zile_minori.text()[:2])) - 1
            data_fin = (data_inceput_dateobj + datetime.timedelta(days=zile())).strftime('%d.%m.%Y')
            return data_fin

    def show_iac1(self):
        if self.instit_1.currentText() == 'în afara competentei SP 1':
            self.iac1.show()
        else:
            self.iac1.hide()

    def show_iac2(self):
        if self.instit_2.currentText() == 'în afara competentei SP 2':
            self.iac2.show()
        else:
            self.iac2.hide()

    def show_minori(self):
        if self.minor_major.currentText() == 'Minor':
            self.ped_label.hide()
            self.ped_an.hide()
            self.ped_luni.hide()
            self.ped_zile.hide()
            self.svp_ani.hide()
            self.svp_luni.hide()
            self.svp_zile.hide()
            self.ped_label.hide()
            self.indiv_ped.hide()

            self.svp_luni_minor.show()
            self.svp_zile_minori.show()
            self.indiv_ped_minori.show()
        else:
            self.ped_label.show()
            self.ped_an.show()
            self.ped_luni.show()
            self.ped_zile.show()
            self.svp_ani.show()
            self.svp_luni.show()
            self.svp_zile.show()
            self.ped_label.show()
            self.svp_label.show()
            self.indiv_ped.show()

            self.svp_luni_minor.hide()
            self.svp_zile_minori.hide()
            self.indiv_ped_minori.hide()

    def instit_nume1(self):
        if self.instit_1.currentText() == 'în afara competentei SP 1':
            return self.iac1.text()
        else:
            return self.instit_1.currentText()

    def instit_nume2(self):
        if self.instit_2.currentText() == 'în afara competentei SP 2':
            return self.iac2.text()
        else:
            return self.instit_2.currentText()

    def sern(self):
        if cfg['sernlista']['sern'] == 'da':
            f = webdriver.Firefox()
            try:
                f.get('https://e-probatiune.just.ro/sern/login')
            except Exception:
                f.get('https://e-probatiune.just.ro/sern/login')
            f.find_element_by_id('login').send_keys(cfg['sernlista']['user'])
            f.find_element_by_id('password').send_keys(cfg['sernlista']['pass'])
            f.find_element_by_id('loginBtn').click()
            f.get('https://e-probatiune.just.ro/sern/probation-subjects/edit')
            f.find_element_by_id('cnp').send_keys(self.CNP.text())
            f.find_element_by_id('offender.lastName').send_keys(self.nume_inc.text().split(" ")[0])
            f.find_element_by_id('offender.firstName').send_keys(
                str(self.nume_inc.text().split(" ")[1:]).replace('[', "").replace(",", "").replace("]", "").replace("'",
                                                                                                                    ""))
            Select(f.find_element_by_id('offender.county.code')).select_by_visible_text('București')
            f.find_element_by_id("offender.city").send_keys(self.sector())
            Select(f.find_element_by_id("offender.addressArea")).select_by_value("URBAN")
            f.find_element_by_id("offender.residenceAddress").send_keys(self.adresa_inc.text())
            if self.studii_nesc.isChecked():
                Select(f.find_element_by_id('offender.schoolEducation')).select_by_value('NONE')
            elif self.studii_s.isChecked():
                Select(f.find_element_by_id('offender.schoolEducation')).select_by_value('UNIVERSITY_STUDIES')
            elif int(self.studii_clase.text()[0:2]) > 0:
                s = self.studii_clase.text()
                if len(s) == 7:
                    Select(f.find_element_by_id('offender.schoolEducation')).select_by_visible_text(s[0])
                elif len(s) == 8:
                    Select(f.find_element_by_id("offender.schoolEducation")).select_by_visible_text(s[0:2])

            try:
                Select(f.find_element_by_id('offender.mainOccupation.id')).select_by_visible_text('Missing')
                Select(f.find_element_by_id('offender.secondaryOccupation.id')).select_by_visible_text('Missing')
                Select(f.find_element_by_id('offender.criminalHistory')).select_by_visible_text('Missing')
                tip_instanta = Select(f.find_element_by_id('courtOfAppealsTypeSelection'))
                oras_instanta = Select(f.find_element_by_id("courtOfAppealsSelection"))
                nume_inst_fara_diacritice = nume_inst(self.indicativ_ds_inst.text())[:-10].replace("ă", "a").replace(
                    "ş",
                    "s").replace(
                    " ", "_").upper()
                if "Judecătoria Sectorului" in nume_inst(self.indicativ_ds_inst.text()):
                    tip_instanta.select_by_value(nume_inst_fara_diacritice)
                elif "Judecători" in nume_inst(self.indicativ_ds_inst.text()) and "Sectorului" not in nume_inst(
                        self.indicativ_ds_inst.text()):
                    tip_instanta.select_by_value("JUDECATORIE")
                    oras_instanta.select_by_index(
                        jud_orase.index(nume_inst(self.indicativ_ds_inst.text())[12:].upper()))
                    # print(oras_instanta.select_by_value(jud_orase.index(nume_inst(self.indicativ_ds_inst.text())[12:].upper())))
                elif "Tribunal" in nume_inst(self.indicativ_ds_inst.text())[0:8]:
                    tip_instanta.select_by_value("TRIBUNAL")
                    oras_instanta.select_by_visible_text(nume_inst(self.indicativ_ds_inst.text())[11:].upper())
                elif "Curtea" in nume_inst(self.indicativ_ds_inst.text())[0:8]:
                    tip_instanta.select_by_value("CURTE_DE_APEL")
                    oras_instanta.select_by_value(curti_de_apel[nume_inst(self.indicativ_ds_inst.text())])
                elif "Înalta" in nume_inst(self.indicativ_ds_inst.text()):
                    tip_instanta.select_by_value("INALTA_CURTE_DE_CASATIE_SI_JUSTITIE")
            except Exception:
                print("Eroare la instanta!")

            f.find_element_by_id("sentenceNumber").send_keys(self.sentinata_fun())

            if self.infr1.text() != "":
                Select(f.find_element_by_id("criminalOffenceSelection")).select_by_index(
                    infractiuni.index(self.infr1.text()))
                f.find_element_by_id("addCriminalOffence").click()

            if self.infr2.text() != "":
                Select(f.find_element_by_id("criminalOffenceSelection")).select_by_index(
                    infractiuni.index(self.infr2.text()))
                f.find_element_by_id("addCriminalOffence").click()

            if self.infr_3.text() != "":
                Select(f.find_element_by_id("criminalOffenceSelection")).select_by_index(
                    infractiuni.index(self.infr_3.text()))
                f.find_element_by_id("addCriminalOffence").click()

            if self.minor_major.currentText() == "Major":
                Select(f.find_element_by_id("sanctionTypeSelect")).select_by_value(
                    individualizare[self.indiv_ped.currentText()])
            elif self.minor_major.currentText() == "Minor":
                Select(f.find_element_by_id("sanctionTypeSelect")).select_by_value(
                    individualizare[self.indiv_ped_minori.currentText()])

            if self.obl_1.text() != "" or self.obl_2.text() != "" or self.obl_3.text():
                Select(f.find_element_by_id("hasObligationSelect")).select_by_visible_text("Da")

            if self.obl_1.text() != "":
                Select(f.find_element_by_id("detailsObligationSelect")).select_by_value(
                    obligatii_sern[self.obl_1.text()])
                if f.execute_script("""return document.querySelector("#detailsObligationSelect").value""") == "414":
                    f.find_element_by_id("communityServiceHoursNoInput").send_keys(self.mfc_h())
                f.find_element_by_id("addSanction").click()

            if self.obl_2.text() != "":
                Select(f.find_element_by_id("detailsObligationSelect")).select_by_value(
                    obligatii_sern[self.obl_2.text()])
                f.find_element_by_id("communityServiceHoursNoInput").send_keys(" ")
                f.find_element_by_id("addSanction").click()

            if self.obl_3.text() != "":
                Select(f.find_element_by_id("detailsObligationSelect")).select_by_value(
                    obligatii_sern[self.obl_3.text()])
                f.find_element_by_id("communityServiceHoursNoInput").send_keys(" ")
                f.find_element_by_id("addSanction").click()

            f.find_element_by_id("registrationNumber").send_keys(
                self.nr_ds_svp.text() + "/" + self.an_ds_svp.currentText() + "/s")
            f.find_element_by_id("registrationDate").send_keys(self.data_ds_svp.text())

            f.find_element_by_id("probationStartDate").send_keys(
                self.data_mod_def_func(self.optiuni_def.currentText())[-10:])
            # f.find_element_by_id("probationStartDate").send_keys(Keys.TAB)
            f.find_element_by_id("probationEndDate").send_keys(self.fin_svp())
            # f.find_element_by_id("saveProbationFile").click()
        else:
            print('nu s-a înregistrat în SERN')

    def lista(self):
        if cfg['sernlista']['lista'] == 'da':
            try:
                dir_inc = QFileDialog.getExistingDirectory() + f"/{self.nume_inc.text()}"
                os.mkdir(dir_inc)
                print(dir_inc)

                documente = document_supraveghere(dsSuprav=self.ds_suprav_func(), nume=self.nume_inc.text(),
                                                  numeP=self.nume_parinti_inc.text(),
                                                  datan=self.data_nastere_inc.text() + ' în ' + self.loc_nastere_inc.text(),
                                                  adresa=self.adresa_inc.text(), cnp=self.CNP.text(),
                                                  studii=self.studii_func(), infr1=self.infr1.text(),
                                                  infr2=self.infr2.text(), infr3=self.infr_3.text(),
                                                  dsinst=self.ds_pen(),
                                                  nrSentinta=self.sentinata_fun(),
                                                  instanta=nume_inst(self.indicativ_ds_inst.text()),
                                                  defin=self.data_mod_def_func(self.optiuni_def.currentText()),
                                                  pedeapsa=self.pedeapsa_func(),
                                                  indicativ=self.indicativ(), ts=self.ts(),
                                                  dataVenire=self.data_venire.text(), oraVenire=self.ora_venire.text(),
                                                  sector=self.sector(), sectie_pol=self.sectie.text(),
                                                  data_svp_i=self.data_mod_def_func(self.optiuni_def.currentText())[
                                                             -10:],
                                                  data_svp_f=self.fin_svp(), obligatii=self.obl_func(),
                                                  mfc_z=self.mfc_zile(), mfc_h=self.mfc_h(),
                                                  mfc_instit_1_n=self.instit_nume1(),
                                                  mfc_instit_1_a=activitati(self.instit_nume1()),
                                                  mfc_instit_2_n=self.instit_nume2(),
                                                  mfc_instit_2_a=activitati(self.instit_2.currentText()))

                # documente.pp(dir_inc + f"\\Prima pagină {nume_inculpat_e.get()}.docx")

                documente.macheta_lista(dir_inc + f"\\{self.nume_inc.text()}.docx")

                # documente.pp(dir_inc + f"\\{nume_inculpat_e.get()}.docx")
                dir__ = str(dir_inc).replace('/', '\\')
                os.system(f"""start explorer {dir__}""")
                os.system(f"""" start explorer {cfg['sernlista']['lm']} """)
            except PermissionError:
                with open('errors.txt', "a+") as err:
                    err.write(f"{str(datetime.datetime.now())} -- {str(sys.exc_info())} \n")

                _ = QMessageBox()
                _.setWindowTitle('Eroare!')
                _.setText('Selectează un folder unde să salvezi folder-ul cu numele beneficiarului!')
                _.setIcon(QMessageBox.Warning)

                __ = _.exec_()

            except FileExistsError:
                with open('errors.txt', "a+") as err:
                    err.write(f"{str(datetime.datetime.now())} -- {str(sys.exc_info())} \n")

                _ = QMessageBox()
                _.setWindowTitle('Eroare!')
                _.setText('Fie mai ai un beneficiar cu același nume, fie ai uitat să pui numele lui! ')
                _.setIcon(QMessageBox.Warning)

                __ = _.exec_()

            except KeyError:
                with open('errors.txt', "a+") as err:
                    err.write(f"{str(datetime.datetime.now())} -- {str(sys.exc_info())} \n")

                _ = QMessageBox()
                _.setWindowTitle('Eroare!')
                _.setText(
                    "Introdu indicativul instanței (numărul dintre '/'). A doua căsuță de la rubrica dosar instanță")
                _.setIcon(QMessageBox.Warning)

                __ = _.exec_()
        else:
            print('Nu s-a creat dosarul de probațiune!')

    def test_print(self):
        self.svp_ani.setMinimum(0)
        self.svp_ani.setValue(0)
        print(self.svp_ani.text())

    def sern_lista(self):
        self.sern()
        self.lista()

    # self.test_print()


class Splash(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        self.timer.start(35)

        self.show()

    def progress(self):
        global counter

        self.ui.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()

            self.main = QtWidgets.QMainWindow()
            self.main.ui = MachetaPyQt5(self.main)
            self.main.show()

            self.close()

        counter += 4


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Splash()

    app.exec_()

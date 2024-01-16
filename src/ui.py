# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eurostat_downloader_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import (
    QtCore,
    QtWidgets
)
from qgis import (
    gui,
    core
)




class UIDialog:
    def setupUi(self, EurostatDialogBase):
        EurostatDialogBase.setObjectName("EurostatDialogBase")
        EurostatDialogBase.resize(1022, 900)
        self.gridLayout = QtWidgets.QGridLayout(EurostatDialogBase)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonSearch = QtWidgets.QPushButton(EurostatDialogBase)
        self.buttonSearch.setObjectName("buttonSearch")
        self.horizontalLayout.addWidget(self.buttonSearch)
        self.lineSearch = QtWidgets.QLineEdit(EurostatDialogBase)
        self.lineSearch.setObjectName("lineSearch")
        self.horizontalLayout.addWidget(self.lineSearch)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listDatabase = QtWidgets.QListWidget(EurostatDialogBase)
        self.listDatabase.setObjectName("listDatabase")
        self.verticalLayout.addWidget(self.listDatabase)
        self.frameMainWindowJoinData = QtWidgets.QFrame(EurostatDialogBase)
        self.frameMainWindowJoinData.setMinimumSize(QtCore.QSize(330, 300))
        self.frameMainWindowJoinData.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMainWindowJoinData.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMainWindowJoinData.setObjectName("frameMainWindowJoinData")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frameMainWindowJoinData)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.buttonReset = QtWidgets.QPushButton(self.frameMainWindowJoinData)
        self.buttonReset.setObjectName("buttonReset")
        self.verticalLayout_7.addWidget(self.buttonReset)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frameMainWindowJoinData)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.qgsComboLayer = gui.QgsMapLayerComboBox(self.frameMainWindowJoinData)
        self.qgsComboLayer.setAllowEmptyLayer(True)
        self.qgsComboLayer.setShowCrs(True)
        self.qgsComboLayer.setFilters(core.Qgis.LayerFilter.PointLayer|core.Qgis.LayerFilter.LineLayer|core.Qgis.LayerFilter.NoGeometry|core.Qgis.LayerFilter.PolygonLayer)
        self.qgsComboLayer.setObjectName("qgsComboLayer")
        self.verticalLayout_3.addWidget(self.qgsComboLayer)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frameMainWindowJoinData)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.qgsComboLayerJoinField = gui.QgsFieldComboBox(self.frameMainWindowJoinData)
        self.qgsComboLayerJoinField.setObjectName("qgsComboLayerJoinField")
        self.verticalLayout_5.addWidget(self.qgsComboLayerJoinField)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.frameMainWindowJoinData)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.comboTableJoinField = QtWidgets.QComboBox(self.frameMainWindowJoinData)
        self.comboTableJoinField.setObjectName("comboTableJoinField")
        self.verticalLayout_6.addWidget(self.comboTableJoinField)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelEnterPrefix = QtWidgets.QLabel(self.frameMainWindowJoinData)
        self.labelEnterPrefix.setObjectName("labelEnterPrefix")
        self.verticalLayout_2.addWidget(self.labelEnterPrefix)
        self.linePrefix = QtWidgets.QLineEdit(self.frameMainWindowJoinData)
        self.linePrefix.setObjectName("linePrefix")
        self.verticalLayout_2.addWidget(self.linePrefix)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkExport = QtWidgets.QCheckBox(self.frameMainWindowJoinData)
        self.checkExport.setObjectName("checkExport")
        self.horizontalLayout_4.addWidget(self.checkExport)
        self.qgsFile = gui.QgsFileWidget(self.frameMainWindowJoinData)
        self.qgsFile.setStorageMode(gui.QgsFileWidget.StorageMode.SaveFile)
        self.qgsFile.setEnabled(False)
        self.qgsFile.setObjectName("qgsFile")
        self.horizontalLayout_4.addWidget(self.qgsFile)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.buttonJoin = QtWidgets.QPushButton(self.frameMainWindowJoinData)
        self.buttonJoin.setMinimumSize(QtCore.QSize(50, 25))
        self.buttonJoin.setObjectName("buttonJoin")
        self.verticalLayout_7.addWidget(self.buttonJoin)
        self.buttonAdd = QtWidgets.QPushButton(self.frameMainWindowJoinData)
        self.buttonAdd.setObjectName("buttonAdd")
        self.verticalLayout_7.addWidget(self.buttonAdd)
        self.verticalLayout.addWidget(self.frameMainWindowJoinData)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.tableDataset = QtWidgets.QTableView(EurostatDialogBase)
        self.tableDataset.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableDataset.setObjectName("tableDataset")
        self.horizontalLayout_2.addWidget(self.tableDataset)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.button_box = QtWidgets.QDialogButtonBox(EurostatDialogBase)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.verticalLayout_4.addWidget(self.button_box)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.retranslateUi(EurostatDialogBase)
        self.button_box.accepted.connect(EurostatDialogBase.accept) # type: ignore
        self.button_box.rejected.connect(EurostatDialogBase.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(EurostatDialogBase)

    def retranslateUi(self, EurostatDialogBase):
        _translate = QtCore.QCoreApplication.translate
        EurostatDialogBase.setWindowTitle(_translate("EurostatDialogBase", "Eurostat data downloader"))
        self.buttonSearch.setText(_translate("EurostatDialogBase", "Search"))
        self.buttonReset.setText(_translate("EurostatDialogBase", "Reset table"))
        self.label.setText(_translate("EurostatDialogBase", "Select layer"))
        self.label_2.setText(_translate("EurostatDialogBase", "Select layer join field"))
        self.label_3.setText(_translate("EurostatDialogBase", "Select table join field"))
        self.labelEnterPrefix.setText(_translate("EurostatDialogBase", "Add prefix to joined fields"))
        self.checkExport.setText(_translate("EurostatDialogBase", "Export data"))
        self.buttonJoin.setText(_translate("EurostatDialogBase", "Join data"))
        self.buttonAdd.setText(_translate("EurostatDialogBase", "Add table"))



class UIParameterSectionDialog:
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QtCore.QSize(500, 400))
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lineSearch = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineSearch.sizePolicy().hasHeightForWidth())
        self.lineSearch.setSizePolicy(sizePolicy)
        self.lineSearch.setFrame(True)
        self.lineSearch.setObjectName("lineSearch")
        self.gridLayout.addWidget(self.lineSearch, 0, 0, 1, 1)
        self.listItems = QtWidgets.QListWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listItems.sizePolicy().hasHeightForWidth())
        self.listItems.setSizePolicy(sizePolicy)
        self.listItems.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listItems.setObjectName("listItems")
        self.gridLayout.addWidget(self.listItems, 1, 0, 2, 1)
        self.buttonReset = QtWidgets.QPushButton(Dialog)
        self.buttonReset.setObjectName("buttonReset")
        self.gridLayout.addWidget(self.buttonReset, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Edit section"))
        self.buttonReset.setText(_translate("Dialog", "Reset selection"))


class UITimePeriodDialog:
    def setupUi(self, SelectTimePeriod):
        SelectTimePeriod.setObjectName("SelectTimePeriod")
        SelectTimePeriod.resize(440, 130)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SelectTimePeriod.sizePolicy().hasHeightForWidth())
        SelectTimePeriod.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(SelectTimePeriod)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frameStart = QtWidgets.QFrame(SelectTimePeriod)
        self.frameStart.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameStart.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameStart.setObjectName("frameStart")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameStart)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelStart = QtWidgets.QLabel(self.frameStart)
        self.labelStart.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labelStart.setObjectName("labelStart")
        self.verticalLayout_2.addWidget(self.labelStart)
        self.verticalLayout.addWidget(self.frameStart)
        self.frameEnd = QtWidgets.QFrame(SelectTimePeriod)
        self.frameEnd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameEnd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameEnd.setObjectName("frameEnd")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frameEnd)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelEnd = QtWidgets.QLabel(self.frameEnd)
        self.labelEnd.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labelEnd.setObjectName("labelEnd")
        self.verticalLayout_3.addWidget(self.labelEnd)
        self.verticalLayout.addWidget(self.frameEnd)
        self.buttonReset = QtWidgets.QPushButton(SelectTimePeriod)
        self.buttonReset.setObjectName("buttonReset")
        self.verticalLayout.addWidget(self.buttonReset)

        self.retranslateUi(SelectTimePeriod)
        QtCore.QMetaObject.connectSlotsByName(SelectTimePeriod)

    def retranslateUi(self, SelectTimePeriod):
        _translate = QtCore.QCoreApplication.translate
        SelectTimePeriod.setWindowTitle(_translate("SelectTimePeriod", "Select time period"))
        self.labelStart.setText(_translate("SelectTimePeriod", "Select start time"))
        self.labelEnd.setText(_translate("SelectTimePeriod", "Select end time"))
        self.buttonReset.setText(_translate("SelectTimePeriod", "Reset values"))
    
    def add_combobox_to_frames(self, object_name: str):
        for frame in (self.frameStart, self.frameEnd):
            widget = QComboboxCompleter(parent=frame)
            widget.setObjectName(object_name)
            frame.layout().addWidget(widget)
            setattr(frame, object_name, widget)
    
    def add_label_to_frames(self, object_name: str, text: str):
        for frame in (self.frameStart, self.frameEnd):
            widget = QtWidgets.QLabel(parent=frame, text=text)
            widget.setObjectName(object_name)
            frame.layout().addWidget(widget)
            setattr(frame, object_name, widget)


class QComboboxCompleter(QtWidgets.QComboBox):
    
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setEditable(True)
        self.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)

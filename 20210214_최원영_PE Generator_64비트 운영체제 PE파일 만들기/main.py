# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 18:28:56 2021

@author: GoldBigDragon
"""

import sys
import PyQt5 as qt
import pe

from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QIntValidator
from PyQt5 import QtWidgets

global ENTRYPOINT_EDIT
global IMAGE_BASE_EDIT
global SECTION_ALIGNMENT_EDIT
global FILE_ALIGNMENT_EDIT

# 에러메시지를 띄우는 함수
def sendErrorMessage(title, subtitle, description):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(subtitle)
    msg.setInformativeText(description)
    msg.setWindowTitle(title)
    msg.exec_()

# PE 파일 생성 성공 메시지를 띄우는 함수
def sendCompleteMessage():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText('성공적으로 PE파일이 생성되었습니다!')
    msg.setWindowTitle('PE 파일 생성 완료')
    msg.exec_()

# PE 파일 생성 규칙에 맞지 않을 경우,
# 자동 정렬을 사용할 것인지 묻는 메시지를 띄우는 함수
def sendAutoAlignMessage():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle("PE파일 생성 규칙에 맞지않는 값 입력")
    msg.setText("동작 가능한 값으로 자동 설정합니까?")
    msg.setInformativeText("No 클릭 시 현재 값으로 생성합니다.")
    msg.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
    retval = msg.exec_()
    return retval
	
# GUI창 틀을 생성하는 함수
class MainGUI(QMainWindow):
  def __init__(self):
    super().__init__()
    layout = MainLayout()
    self.setWindowIcon(QIcon('./res/img/icon.png'))
    self.setCentralWidget(layout)
    self.setWindowTitle("PE 뽑기 생성기")
    self.show()

# GUI창에 실질적인 위젯을 추가하는 함수
class MainLayout(QWidget):
  def __init__(self):
    global ENTRYPOINT_EDIT
    global IMAGE_BASE_EDIT
    global SECTION_ALIGNMENT_EDIT
    global FILE_ALIGNMENT_EDIT
    super().__init__()
    self.setStyleSheet(open('./res/css/basic.css').read())
    self.setWindowIcon(QIcon('./res/img/icon.png'))
    self.resize(1024, 720)
    
    self.GENERATE_LABEL = QLabel('생성 위치', self)
    self.GENERATE_LABEL.setAlignment(Qt.AlignCenter)
    self.GENERATE_LABEL.setToolTip("PE파일을 생성할 디렉터리입니다.")
    
    self.CREATE_PATH_LABEL = QLabel("지정된 경로가 없습니다.", self)
    self.CREATE_PATH_LABEL.setToolTip("PE파일을 생성할 디렉터리입니다.")
    self.CREATE_PATH_SELECT_BUTTON = QPushButton(self)
    self.CREATE_PATH_SELECT_BUTTON.setMinimumWidth(100)
    self.CREATE_PATH_SELECT_BUTTON.setMaximumWidth(100)
    self.CREATE_PATH_SELECT_BUTTON.setMinimumHeight(25)
    self.CREATE_PATH_SELECT_BUTTON.setMaximumHeight(25)
    self.CREATE_PATH_SELECT_BUTTON.setObjectName("FIND_PATH_BUTTON");
    self.CREATE_PATH_SELECT_BUTTON.setToolTip("PE파일이 생성될 디렉터리를 지정합니다.")
    self.CREATE_PATH_SELECT_BUTTON.clicked.connect(self.fileOpen)
    
    self.GENERATE_PE_BUTTON = QPushButton(self)
    self.GENERATE_PE_BUTTON.setEnabled(True)
    self.GENERATE_PE_BUTTON.setMinimumWidth(100)
    self.GENERATE_PE_BUTTON.setMaximumWidth(100)
    self.GENERATE_PE_BUTTON.setMinimumHeight(25)
    self.GENERATE_PE_BUTTON.setMaximumHeight(25)
    self.GENERATE_PE_BUTTON.setObjectName("CREATE_BUTTON");
    self.GENERATE_PE_BUTTON.setToolTip("위 설정대로 PE파일을 생성합니다.")
    self.GENERATE_PE_BUTTON.clicked.connect(self.checkCreate)
    
    ENTRYPOINT_EDIT, self.ENTRYPOINT_LABEL = self.createFieldAndLabel('EntryPoint', 4096, 4096, 1048575, "프로그램이 실행되는 코드의 상대 주소값(RVA) 입니다.\n보통 SectionAlignment값과 동일합니다.")
    IMAGE_BASE_EDIT, self.IMAGE_BASE_LABEL = self.createFieldAndLabel('ImageBase', 4194304, 65536, 1073741824, "가상메모리에서의 PE파일이 로딩 되는 주소로,\n65536의 배수만 설정 가능합니다. (65536 ~ 4294901760)\n \n예) 65536, 4194304, 7340032, 8847360")
    SECTION_ALIGNMENT_EDIT, self.SECTION_ALIGNMENT_LABEL = self.createFieldAndLabel('SectionAlignment', 4096, 4096, 1048575, "각 Section이 메모리 상에서 차지하는 최소 크기로,\nPage 단위(4096의 배수)로만 설정 가능하며,\nFileAlignment보다 커야 합니다. (4096 ~ 4294963200)\n \n예) 4096, 8192, 12288, 16384")
    FILE_ALIGNMENT_EDIT, self.FILE_ALIGNMENT_LABEL = self.createFieldAndLabel('FileAlignment', 512, 512, 32768, "각 Section이 디스크 상에서 차지하는 최소 크기로,\n512부터 65536사이의 2의 n승 형태로만 설정 가능하며,\nSectionAlignment보다 작아야 합니다. (512 ~ 32768)\n \n예) 512, 1024, 2048, 4096")
    self.AMOUNT_EDIT, self.AMOUNT_LABEL = self.createFieldAndLabel('생성할 PE파일 개수', 3, 1, 10000, "생성시킬 PE 파일의 개수입니다. (1 ~ 10000)\n \n예) 10, 100, 121")
    self.SUCCESS_AMOUNT, self.SUCCESS_LABEL = self.createFieldAndLabel('당첨 티켓 수', 1, 0, 10000, "생성된 PE 파일 중, 당첨 메시지를 띄울\nPE 파일의 개수를 지정합니다. (0 ~ 10000)\n \n예) 3, 6, 15")
    
    grid = QGridLayout()
    grid.setHorizontalSpacing(-1);
    grid.setVerticalSpacing(5);
    grid.addWidget(self.ENTRYPOINT_LABEL, 0, 0)
    grid.addWidget(ENTRYPOINT_EDIT, 0, 1, 1, 2)
    grid.addWidget(self.IMAGE_BASE_LABEL, 1, 0)
    grid.addWidget(IMAGE_BASE_EDIT, 1, 1, 1, 2)
    grid.addWidget(self.SECTION_ALIGNMENT_LABEL, 2, 0)
    grid.addWidget(SECTION_ALIGNMENT_EDIT, 2, 1, 1, 2)
    grid.addWidget(self.FILE_ALIGNMENT_LABEL, 3, 0)
    grid.addWidget(FILE_ALIGNMENT_EDIT, 3, 1, 1, 2)
    grid.addWidget(self.AMOUNT_LABEL, 4, 0)
    grid.addWidget(self.AMOUNT_EDIT, 4, 1, 1, 2)
    grid.addWidget(self.SUCCESS_LABEL, 5, 0)
    grid.addWidget(self.SUCCESS_AMOUNT, 5, 1, 1, 2)
    grid.addWidget(self.GENERATE_LABEL, 6, 0)
    grid.addWidget(self.CREATE_PATH_LABEL, 6, 1)
    grid.addWidget(self.CREATE_PATH_SELECT_BUTTON, 6, 2)
    
    vbox = QVBoxLayout()
    vbox.addStretch(1)
    vbox.addLayout(grid, 4)
    centerHbox = QHBoxLayout()
    centerHbox.addStretch(1)
    centerHbox.addWidget(self.GENERATE_PE_BUTTON, 4)
    centerHbox.addStretch(1)
    vbox.addLayout(centerHbox)
    vbox.addStretch(1)
    hbox = QHBoxLayout()
    hbox.addStretch(1)
    hbox.addLayout(vbox, 4)
    hbox.addStretch(1)
    self.setLayout(hbox)

  # 동일한 스타일의 필드와 라벨을 생성하는 함수
  def createFieldAndLabel(self, name, initValue, minValue, maxValue, description):
    field = QLineEdit(str(initValue), self)
    field.setToolTip(description)
    field.setValidator(QIntValidator(minValue, maxValue))
    label = QLabel(name, self)
    label.setAlignment(Qt.AlignCenter)
    label.setToolTip(description)
    label.setMinimumWidth(150)
    label.setMaximumWidth(150)
    return field, label

  # PE 파일 생성 디렉터리를 지정하는 함수
  def fileOpen(self):
    filename = QtWidgets.QFileDialog.getExistingDirectory(self, "PE 파일을 생성할 디렉터리 선택")
    if filename is not None and len(filename) > 0:
      self.CREATE_PATH_LABEL.setText(str(filename))

  # PE 파일 생성 가능 여부를 판단하고,
  # pe.py를 이용하여 PE 파일을 생성하는 함수
  def checkCreate(self):
    global ENTRYPOINT_EDIT
    global IMAGE_BASE_EDIT
    global SECTION_ALIGNMENT_EDIT
    global FILE_ALIGNMENT_EDIT
    entryPoint = ENTRYPOINT_EDIT.text()
    imageBase = IMAGE_BASE_EDIT.text()
    sectionAlignment = SECTION_ALIGNMENT_EDIT.text()
    fileAlignment = FILE_ALIGNMENT_EDIT.text()
    amount = self.AMOUNT_EDIT.text()
    successAmount = self.SUCCESS_AMOUNT.text()
    directory = self.CREATE_PATH_LABEL.text()
    if entryPoint == None or len(entryPoint) < 1:
        sendErrorMessage('필수 입력 값', 'EntryPoint 값을 설정 해 주세요!', None)
        return
    if imageBase == None or len(imageBase) < 1:
        sendErrorMessage('필수 입력 값', 'ImageBase 값을 설정 해 주세요!', None)
        return
    if sectionAlignment == None or len(sectionAlignment) < 1:
        sendErrorMessage('필수 입력 값', 'SectionAlignment 값을 설정 해 주세요!', None)
        return
    if fileAlignment == None or len(fileAlignment) < 1:
        sendErrorMessage('필수 입력 값', 'FileAlignment 값을 설정 해 주세요!', None)
        return
    if amount == None or len(amount) < 1:
        sendErrorMessage('필수 입력 값', '생성할 PE 파일의 개수를 입력 해 주세요!', None)
        return
    if successAmount == None or len(successAmount) < 1:
        sendErrorMessage('필수 입력 값', '당첨 PE 파일의 개수를 입력 해 주세요!', None)
        return
    if directory == None or len(directory) < 1 or directory == '지정된 경로가 없습니다.':
        sendErrorMessage('필수 입력 값', 'PE 파일 생성 위치를 입력 해 주세요!', None)
        return
    self.GENERATE_PE_BUTTON.setDisabled(True)
    
    if int(successAmount) > int(amount):
        self.SUCCESS_AMOUNT.setText(amount)
        successAmount = amount
    
    if int(sectionAlignment) != int(entryPoint) or int(sectionAlignment) < int(fileAlignment) or int(imageBase) < 65536 or int(imageBase)%65536 != 0 or int(sectionAlignment) < 4096 or int(sectionAlignment)%4096 != 0 or int(fileAlignment) < 512 or int(fileAlignment) % 512 != 0:
        retval = sendAutoAlignMessage()
        if retval == 65536:
            pe.generatePE(int(entryPoint), int(imageBase), int(sectionAlignment), int(fileAlignment), int(amount), int(successAmount), directory)
            sendCompleteMessage()
        else:
            ENTRYPOINT_EDIT.setText('4096')
            IMAGE_BASE_EDIT.setText('4194304')
            SECTION_ALIGNMENT_EDIT.setText('4096')
            FILE_ALIGNMENT_EDIT.setText('512')
    else:
        pe.generatePE(int(entryPoint), int(imageBase), int(sectionAlignment), int(fileAlignment), int(amount), int(successAmount), directory)
        sendCompleteMessage()
    self.GENERATE_PE_BUTTON.setDisabled(False)

# 파이선 스크립트 수행 시 가장 먼저 실행되는 함수
if __name__ == '__main__':
    app = qt.QtWidgets.QApplication(sys.argv)
    gui = MainGUI()
    sys.exit(app.exec_())
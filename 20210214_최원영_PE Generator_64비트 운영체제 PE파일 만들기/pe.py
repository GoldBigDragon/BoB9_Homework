# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 13:05:39 2021

@author: GoldBigDragon

"""
import time
import random
import os

DOS_HEADER = [77, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 0, 0, 0]
DOS_STUB = [14, 31, 186, 14, 0, 180, 9, 205, 33, 184, 1, 76, 205, 33, 84, 104, 
105, 115, 32, 112, 114, 111, 103, 114, 97, 109, 32, 99, 97, 110, 110, 111, 
116, 32, 98, 101, 32, 114, 117, 110, 32, 105, 110, 32, 68, 79, 83, 32, 
109, 111, 100, 101, 46, 13, 10, 36, 0, 0, 0, 0, 0, 0, 0, 0]
PE_HEADER = [80, 69, 0, 0, 100, 134, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 240, 0, 47, 0]
OPTIONAL_HEADER = [11, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 64, 0, 0, 0, 0, 0, 
0, 16, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
4, 0, 0, 0, 0, 0, 0, 0, 0, 80, 0, 0, 0, 2, 0, 0, 
0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0]
DATA_DIRECTORY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 48, 0, 0, 182, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
SECTION_TABLE = [
46, 116, 101, 120, 116, 0, 0, 0, 103, 0, 0, 0, 0, 16, 0, 0, # .text
0, 2, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 32, 0, 0, 96,
46, 100, 97, 116, 97, 0, 0, 0, 1, 0, 0, 0, 0, 32, 0, 0, # .data
0, 2, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 64, 0, 0, 192, 
46, 114, 100, 97, 116, 97, 0, 0, 182, 0, 0, 0, 0, 48, 0, 0, # .rdata
0, 2, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 64, 0, 0, 64,
46, 114, 115, 114, 99, 0, 0, 0, 1, 1, 0, 0, 0, 64, 0, 0, # .rsrc
0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 64, 0, 0, 64]
TEXT = [72, 131, 236, 8, 72, 131, 236, 32, 72, 199, 193, 0, 0, 0, 0, 235, 
14, 84, 82, 89, 32, 65, 71, 65, 73, 78, 33, 0, 0, 0, 0, 72, 
141, 21, 235, 255, 255, 255, 235, 18, 89, 111, 117, 114, 32, 114, 101, 115, 
117, 108, 116, 32, 58, 0, 0, 0, 0, 0, 76, 141, 5, 231, 255, 255, 
255, 73, 199, 193, 0, 0, 0, 0, 255, 21, 74, 32, 0, 0, 72, 131, 
196, 32, 72, 131, 236, 32, 72, 199, 193, 0, 0, 0, 0, 255, 21, 5, 
32, 0, 0, 72, 131, 196, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0]
DATA = [88, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 48, 0, 0, 
104, 48, 0, 0, 136, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
74, 48, 0, 0, 152, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 107, 101, 114, 110, 
101, 108, 51, 50, 46, 100, 108, 108, 0, 0, 117, 115, 101, 114, 51, 50, 
46, 100, 108, 108, 0, 0, 0, 0, 120, 48, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 120, 48, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 69, 120, 105, 116, 80, 114, 
111, 99, 101, 115, 115, 0, 0, 0, 168, 48, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 168, 48, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 77, 101, 115, 115, 97, 103, 
101, 66, 111, 120, 65, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
RDATA = [0]
RSRC = [0]

fileIndex = []


# 해당 파일을 바이너리 형태로 출력 해 주는 함수 (코드 생성용)
def cropBinaryArea(filename):
    buffer = ''
    counter = 0
    with open(filename, 'rb') as f:
      byte = f.read(1)
      while byte != b"":
          counter += 1
          buffer += str(int(byte.hex(), 16)) + ', '
          if counter > 15:
            buffer += '\n'
            counter = 0
          byte = f.read(1)
    print(buffer.replace(' 00,', ' 0,').replace('\n00,', '\n0,'))

# 10진수를 16진수로 리틀엔디언으로 변환 해 주는 함수
def getHexArray(value):
    hexString = '{:08x}'.format(value)
    returnArray = []
    tempArray = []
    for i in range(len(hexString)):
        tempArray.append(hexString[i])
        if len(tempArray) > 1:
            returnArray.append(int(tempArray[0]+tempArray[1], 16))
            tempArray.clear()
    if len(tempArray) != 0:
        returnArray.append(int(tempArray[0], 16))
    # 리틀엔디언 계산을 위한 reverse()
    returnArray.reverse()
    return returnArray

# Alignment에 Length가 미치려면 얼마나 많은 Padding이 필요한지 알려주는 함수
def getLacking(length, alignment):
    if length < alignment:
      return alignment-length
    elif length > alignment:
      mok = int(length / alignment)
      if length % alignment != 0:
        mok += 1
      return (alignment*mok)-length
    else:
      return 0

# Alignment를 기준으로 입력한 Array에 패딩을 추가하는 함수
def getPadding(targetArray, alignment):
    targetLength = len(targetArray)
    for i in range(getLacking(targetLength, alignment)):
      targetArray += [0]
    return targetArray

# rdata에 당첨 메시지를 입력하는 함수
def setSuccessText(textSection):
    text = [83, 85, 67, 67, 69, 83, 83, 33, 33, 33, 0, 0, 0, 0]
    for i in range(14):
        textSection[17+i] = text[i]
    return textSection

# rdata에 다시 뽑아 보라는 메시지를 입력하는 함수    
def setFailText(textSection):
    text = [84, 82, 89, 32, 65, 71, 65, 73, 78, 33, 0, 0, 0, 0]
    for i in range(14):
        textSection[17+i] = text[i]
    return textSection

# DirectoryRAW = DirectoryRVA - SectionRVA + SectionRAW
# RAW = RVA - VA + PointerToRawData(파일에서 섹션 시작 위치)
# https://zulloper.tistory.com/121
# 사용자가 입력한 입력 값을 계산하여 PE헤더에 적용하는 함수
def applyOptions(header, entryPoint, imageBase, sectionAlignment, fileAlignment):
    timeStamp = getHexArray(round(time.time() * 1000))
    
    entryImportVirtualAddressArray = getHexArray(sectionAlignment*3) # 12288
    
    headerLength = len(header)
    entryPointArray = getHexArray(entryPoint)
    imageBaseArray = getHexArray(imageBase)
    sectionAlignmentArray = getHexArray(sectionAlignment)
    fileAlignmentArray = getHexArray(fileAlignment)
    imageSizeArray = getHexArray(sectionAlignment * 5)
    headerSizeArray = getHexArray(headerLength)
    
    textRVirtualAddressArray = getHexArray(sectionAlignment)
    dataRVirtualAddressArray = getHexArray(sectionAlignment*2)
    rdataRVirtualAddressArray = getHexArray(sectionAlignment*3)
    rsrcRVirtualAddressArray = getHexArray(sectionAlignment*4)
    
    textPointerToRawDataArray = getHexArray(headerLength)
    textTableSize = 512 + getLacking(512, fileAlignment)
    dataPointerToRawDataArray = getHexArray(headerLength+textTableSize)
    dataTableSize = 512 + getLacking(512, fileAlignment)
    rdataPointerToRawDataArray = getHexArray(headerLength+textTableSize) # data와 공유
    rdataTableSize = 512 + getLacking(512, fileAlignment)
    rsrcPointerToRawDataArray = getHexArray(headerLength+textTableSize+dataTableSize+rdataTableSize)
    for i in range(4):
        #timeStamp
        header[136+i] = timeStamp[i]
        
        # Option Header
        header[168+i] = entryPointArray[i]
        header[176+i] = imageBaseArray[i]
        header[184+i] = sectionAlignmentArray[i]
        header[188+i] = fileAlignmentArray[i]
        header[208+i] = imageSizeArray[i]
        header[212+i] = headerSizeArray[i]
        
        # Data Directory RelativeVirtualAddress
        header[272+i] = entryImportVirtualAddressArray[i]
        
        # Section Table RelativeVirtualAddress
        header[404+i] = textRVirtualAddressArray[i]
        header[444+i] = dataRVirtualAddressArray[i]
        header[484+i] = rdataRVirtualAddressArray[i]
        header[524+i] = rsrcRVirtualAddressArray[i]
        
        # Section Table Size of Raw Data
        header[412+i] = textPointerToRawDataArray[i]
        header[452+i] = dataPointerToRawDataArray[i]
        header[492+i] = rdataPointerToRawDataArray[i]
        header[532+i] = rsrcPointerToRawDataArray[i]
    return header

# 유효한 파일 이름을 가져오는 함수
def getFileName():
    global fileIndex
    index = random.randint(0, len(fileIndex) - 1)
    returnIndex = fileIndex[index]
    del fileIndex[index]
    return str(returnIndex)

# 사용자 입력값을 받아 PE 파일을 생성하는 함수
def generatePE(entryPoint, imageBase, sectionAlignment, fileAlignment, amount, successAmount, directory):
    global TEXT
    global RDATA
    global DATA
    global RSRC
    global fileIndex
    fileIndex.clear()
    for index in range(1, amount+1):
        fileIndex.append(index)

    paddedTEXT = getPadding(TEXT, fileAlignment)
    paddedDATA = getPadding(DATA, fileAlignment)
    paddedRDATA = getPadding(RDATA, fileAlignment)
    paddedRSRC = getPadding(RSRC, fileAlignment)
    
    successText = setSuccessText(paddedTEXT.copy())
    failedText = setFailText(paddedTEXT.copy())
    
    basicPe = []
    basicPe += DOS_HEADER
    basicPe += DOS_STUB
    basicPe += PE_HEADER
    basicPe += OPTIONAL_HEADER
    basicPe += DATA_DIRECTORY
    basicPe += SECTION_TABLE
    basicPe = getPadding(basicPe, fileAlignment)
    basicPe = applyOptions(basicPe, entryPoint, imageBase, sectionAlignment, fileAlignment)
    successPe = basicPe+successText+paddedDATA+paddedRDATA+paddedRSRC
    failedPe = basicPe+failedText+paddedDATA+paddedRDATA+paddedRSRC
    
    if directory[-1] != '/':
        directory += '/'
    if os.path.isdir(directory) == False:
        os.mkdir(directory)
    
    for index in range(successAmount):
        newFile = open(directory+getFileName()+".exe", "wb")
        newFile.write(bytearray(successPe))
        newFile.close()
    for index in range(amount - successAmount):
        newFile = open(directory+getFileName()+".exe", "wb")
        newFile.write(bytearray(failedPe))
        newFile.close()

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 13:05:39 2021

@author: GoldBigDragon

"""
DoSHeader = [77, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 0, 0, 0]
DoSStub = [14, 31, 186, 14, 0, 180, 9, 205, 33, 184, 1, 76, 205, 33, 84, 104,
           105, 115, 32, 112, 114, 111, 103, 114, 97, 109, 32, 99, 97, 110, 110, 111,
           116, 32, 98, 101, 32, 114, 117, 110, 32, 105, 110, 32, 68, 79, 83, 32,
           109, 111, 100, 101, 46, 13, 13, 10, 36, 0, 0, 0, 0, 0, 0, 0]
PEHeader = [80, 69, 0, 0, 76, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 224, 0, 3, 1]


def getOptionalHeader(entryPoint, imageBase, sectionAlignment, fileAlignment):
    prefix = [11, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    suffix = []
    return bytearray()
if __name__ == "__main__":
    newFile = open("testa.exe", "wb")
    newFile.write(bytearray(DoSHeader))
    newFile.write(bytearray(DoSStub))
    newFile.write(bytearray(PEHeader))
    newFile.write(getOptionalHeader())
    newFile.close()
    """
    entryPoint = None
    imageBase = None
    sectionAlignment = None
    fileAlignment = None
    print('EntryPoint 주소를 입력하세요! (16진수)')
    print('(입력값 < FFFFFFFF)')
    entryPoint = input(' > ')
    print('ImageBase 주소를 입력하세요! (16진수)')
    print('(입력값 < 4294967296)')
    imageBase = input(' > ')
    print('SectionAlignment')
    sectionAlignment = input(' > ')
    print('FileAlignment')
    fileAlignment = input(' > ')
    """
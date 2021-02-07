from sklearn import svm, metrics
import glob, os.path, re, json

def getDataAndLabel(path):
    filesPathArrays = glob.glob(path+"\\*.txt")
    returnData = []
    returnLabel = []
    codeA = ord("a")
    codeZ = ord("z")
    for filePath in filesPathArrays:
        language = os.path.basename(filePath).split("-")[0]
        file = open(filePath, "r", encoding="utf-8")
        text = file.read().lower()
        file.close()
        count = [0 for n in range(0, 26)]
        for character in text:
            nowChar = ord(character)
            if codeA <= nowChar <= codeZ:
                count[nowChar - code_a] += 1
        total = sum(count)
        count = list(map(lambda n: n/total, count))
        returnData.append(count)
        returnLabel.append(language)
    return returnData, returnLabel

trainData, trainLabel = getDataAndLabel("C:\\Users\\dnwnd\\Downloads\\languageDetectionFiles\\train")
testData, testLabel = getDataAndLabel("C:\\Users\\dnwnd\\Downloads\\languageDetectionFiles\\test")

clf = svm.SVC()
clf.fit(trainData, trainLabel)
predict = clf.predict(testData)
accuracy = metrics.accuracy_score(testLabel, predict)
report = metrics.classification_report(testLabel, predict)
print("Accuracy :", accuracy)
print(report)
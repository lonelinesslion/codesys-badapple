sourceFilePath = input("Please input sourceFilePath: ")
sourceFileNumbers = input("Please input sourceFile Numbers: ")
fileNum = int(sourceFileNumbers) + 1

targetFilePath = input("Please input targetFilePath: ")
targetFileName = input("Please input targetFileName: ")

targetFile = open(targetFilePath + targetFileName, "wb")

for i in range(1, fileNum):
    sourceFileNum = str(i)
    sourceFile = open(sourceFilePath + sourceFileNum + ".bin", "rb")
    sourceData = sourceFile.read()
    targetFile.write(sourceData)
    sourceFile.close()
    # print(sourceFileNum + ".bin")

targetFile.close()

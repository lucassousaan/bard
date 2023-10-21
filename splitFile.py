import csv

openResults = open('results/classification_complete.csv', 'w', newline='')
writerResults = csv.writer(openResults)

with open('results/classification_result1.csv', 'rt') as result1:
    readerResult = csv.reader(result1)
    counterResult = 0
    for rowResult in readerResult:
        if (counterResult == 0):
            writerResults.writerow(rowResult)
        else:
            writerResults.writerow(rowResult)
        counterResult += 1
    result1.close()

with open('results/classification_result2.csv', 'rt') as result2:
    readerResult2 = csv.reader(result2)
    counterResult2 = 0
    for rowResult2 in readerResult2:
        if (counterResult2 > 0):
            writerResults.writerow(rowResult2)
        counterResult2 += 1
    result2.close()

with open('results/classification_result3.csv', 'rt') as result3:
    readerResult3 = csv.reader(result3)
    counterResult3 = 0
    for rowResult3 in readerResult3:
        if (counterResult3 > 0):
            writerResults.writerow(rowResult3)
        counterResult3 += 1
    result3.close()

with open('results/classification_result4.csv', 'rt') as result4:
    readerResult4 = csv.reader(result4)
    counterResult4 = 0
    for rowResult4 in readerResult4:
        if (counterResult4 > 0):
            writerResults.writerow(rowResult4)
        counterResult4 += 1
    result3.close()

# csvFile1 = open('dataset/dataset_label_1.csv', 'w', newline='')
# writerCsv1 = csv.writer(csvFile1)

# csvFile2 = open('dataset/dataset_label_2.csv', 'w', newline='')
# writerCsv2 = csv.writer(csvFile2)

# csvFile3 = open('dataset/dataset_label_3.csv', 'w', newline='')
# writerCsv3 = csv.writer(csvFile3)

# csvFile4 = open('dataset/dataset_label_4.csv', 'w', newline='')
# writerCsv4 = csv.writer(csvFile4)



# with open("dataset/dataset_label_shuffled.csv", 'rt') as fileShuffled:
#     readerShuffled = csv.reader(fileShuffled)
#     counterShuffled = 0
#     for rowFake in readerShuffled:
#         if counterShuffled == 0:
#             writerCsv1.writerow([rowFake[0], rowFake[1], rowFake[2], "is_fake_news"])
#             writerCsv2.writerow([rowFake[0], rowFake[1], rowFake[2], "is_fake_news"])
#             writerCsv3.writerow([rowFake[0], rowFake[1], rowFake[2], "is_fake_news"])
#             writerCsv4.writerow([rowFake[0], rowFake[1], rowFake[2], "is_fake_news"])
#         else:
#             if (counterShuffled <= 51):
#                 writerCsv1.writerow(rowFake)
#             elif (counterShuffled >= 51 and counterShuffled <= 101):
#                 writerCsv2.writerow(rowFake)
#             elif (counterShuffled >= 101 and counterShuffled <= 151):
#                 writerCsv3.writerow(rowFake)
#             else:
#                 writerCsv4.writerow(rowFake)
#         counterShuffled += 1
#     fileShuffled.close()
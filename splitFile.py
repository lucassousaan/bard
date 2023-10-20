import csv

csvFile1 = open('dataset/dataset_label_1.csv', 'w', newline='')
writerCsv1 = csv.writer(csvFile1)

csvFile2 = open('dataset/dataset_label_2.csv', 'w', newline='')
writerCsv2 = csv.writer(csvFile2)

csvFile3 = open('dataset/dataset_label_3.csv', 'w', newline='')
writerCsv3 = csv.writer(csvFile3)

csvFile4 = open('dataset/dataset_label_4.csv', 'w', newline='')
writerCsv4 = csv.writer(csvFile4)



with open("dataset/dataset_label_shuffled.csv", 'rt') as fileShuffled:
    readerShuffled = csv.reader(fileShuffled)
    counterShuffled = 0
    for rowFake in readerShuffled:
        if counterShuffled == 0:
            writerCsv1.writerow([rowFake[0], rowFake[1], rowFake[2], "is_fake_news"])
            writerCsv2.writerow([rowFake[0], rowFake[1], rowFake[2], "is_fake_news"])
            writerCsv3.writerow([rowFake[0], rowFake[1], rowFake[2], "is_fake_news"])
            writerCsv4.writerow([rowFake[0], rowFake[1], rowFake[2], "is_fake_news"])
        else:
            if (counterShuffled <= 51):
                writerCsv1.writerow(rowFake)
            elif (counterShuffled >= 51 and counterShuffled <= 101):
                writerCsv2.writerow(rowFake)
            elif (counterShuffled >= 101 and counterShuffled <= 151):
                writerCsv3.writerow(rowFake)
            else:
                writerCsv4.writerow(rowFake)
        counterShuffled += 1
    fileShuffled.close()
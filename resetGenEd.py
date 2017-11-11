import os
import createDB
import populateDB

def formatJSON(f):
    inFile = open(f,"r")
    fileString = inFile.read().replace("—","--").replace("é","e")
    inFile.close()

    outFile = open(f,"w")
    outFile.write(fileString)
    outFile.close()

def runScrapySpider(f):
    os.system("rm {}".format(f))
    os.system("scrapy crawl courseSpider")

def createDatabase(f):
    createDB.run(f)

def populateDatabase(f):
    populateDB.run(f)

def main(fName="lcCourses.json"):

    print("Running spider...")
    runScrapySpider(fName)
    formatJSON(fName)
    print("Complete")

    print("Creating Database...")
    createDatabase(fName)
    populateDatabase(fName)
    print("Complete")

    print("GenEd Reset Complete!")

if __name__ == "__main__":
    main()

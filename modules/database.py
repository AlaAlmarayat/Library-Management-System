from tkinter import * 
from datetime import datetime

bookInfoFilePath ='.\\files\\Book_Info.txt'
membersFilePath='.\\files\\Members.txt'
logFilePath ='.\\files\\logfile.txt'
bookTransactionHistoryFilePath='.\\files\\Book_Transaction_History.txt'

transactionHistoryTableHeader = ["    Book ID    ", "    Member ID    ", "    Genre    ", "    Title    ", "    Author    ", "  Purchase Price JOD  ", "  Loan Availability  "]


def addTransactionHistoryRecord (ID):
    global bookID,memberID,genre,title, Author,purchasePrice,loanAvailability 

    bookInfo = getBookByID(bookInfoFilePath,ID)
    bookLogInfo = getBookByID(logFilePath,ID)
    
    print(bookInfo)
    print(bookLogInfo)
    transactionHistory = [[bookInfo[1],bookLogInfo[2],bookInfo[2],bookInfo[3],bookInfo[4],bookInfo[5],bookLogInfo[6]]]
     
    insert(bookTransactionHistoryFilePath ,transactionHistory, transactionHistoryTableHeader,"History") 

def selectTopGenres(logFilePath):
    return getTop(logFilePath,3)     

def selectTopBooks(logFilePath):
    return getTop(logFilePath,4)     

# --------------------------------searchLogID---------------------------------------- #
def getBookStatusByID(ID):    
    """
    search log by ID and get avilability status\n
    Book ID as an argument (int)\n
    return status 0 if not exist | 1 if exist 
    """ 
    loanAvilabilityStatus = ""
    with open(logFilePath, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        templist = []
        resultList = []
        
       
        for line in lines[1:]:
            templist  = line.split("|")
            id = str(templist[1]).replace(" ","")
            fileId = int(id  )
            ID = int(ID)

            if fileId == ID and line.index != 0:
                line = line.replace(" ","")
                resultList  = line.split("|")
                loanAvilabilityStatus= resultList[6]
                

    return loanAvilabilityStatus   
# --------------------------------searchLogID---------------------------------------- #

# --------------------------------searchTitleLog---------------------------------------- #
def searchTitleLog(title):
    """
    search book log by title\n
    title as an 1st argument (string)\n
    return list of books
    """ 
    with open(logFilePath, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        status = 0
        templist = []
        resultList = []

        for line in lines[1:]: 
            templist2  = line.split("|")
            lineTitle = str(templist2[4]).replace(" ","").lower()
            fileTitle = title.lower()
                            
            if lineTitle.find(fileTitle) != -1 and lines.index != 0:
                line = line.replace(" ","")
                templist  = line.split("|")
                templist.pop(0)
                templist.pop(0)
                templist.pop(0)
                
                templist.pop(len(templist)-1)                
                templist.pop(len(templist)-1)                
                templist.pop(len(templist)-1)
                resultList.append(templist)
                

    return resultList     
# --------------------------------searchTitleLog---------------------------------------- #

# --------------------------------returnAllTitleLog---------------------------------------- #
def returnAllTitleLog():
    """
    get all book log data\n
    return all book log data
    """
     
    with open(logFilePath, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        status = 0
        templist = []
        resultList = []
        print(lines[0])
        for line in lines[1:]:
            
            line = line.replace(" ","")
            templist  = line.split("|")
            templist.pop(0)
            templist.pop(0)
            templist.pop(0)
            
            templist.pop(len(templist)-1)                
            templist.pop(len(templist)-1)                
            templist.pop(len(templist)-1)
            resultList.append(templist)
                

    return resultList  
# --------------------------------returnAllTitleLog---------------------------------------- #

# --------------------------------searchTitle---------------------------------------- #
def searchTitle(title):
    """
    search book by title\n
    title as an 1st argument (string)\n
    return list of books
    """ 
    with open(bookInfoFilePath, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        status = 0
        for line in lines: 
            if line.find(title) != -1:
                print( line)
                status = 1 
        if status == 0: 
           print('No Results Found')
# --------------------------------returnAllTitleLog---------------------------------------- #

# --------------------------------searchID---------------------------------------- #
def searchID(filepath,ID):
    """
    search by ID\n
    Book ID as an 1st argument (int)\n
    return list of books
    """ 
    with open(filepath, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        global status
        status = 0
        searchResult = []
        lineNumber = 0

        for line in lines:
            templist = []

            if lineNumber == 0:  
                id = line[0:20]
                if id.find(ID) != -1 and line.index != 0:
                    status = 1
                    searchResult=line.split("|")
                    break 
            else:
                templist  = line.split("|")
                id = str(templist[1]).replace(" ","")
                fileId = int(id  )
                ID = int(ID)

                if fileId == ID and line.index != 0:
                    status = 1
                    searchResult=line.split("|")
                    break 

    return searchResult
# --------------------------------searchID---------------------------------------- #

def getSearchStatus(filepath,ID):
    global status
    searchID(filepath,ID)

    return status

# --------------------------------update---------------------------------------- #
def getBookByID(filePath,ID):
    """
    get Book By ID\n
    Book ID as an 1st argument (int)\n
    return book details
    """

    with open(filePath, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines() 

        for line in lines[1:]:
            templist2  = line.split("|")
            id = str(templist2[1]).replace(" ","")
            fileId = int(id  )
            ID = int(ID)

            if fileId == ID and line.index != 0: 
                searchResult=line.split("|") 
                

    return searchResult  
# --------------------------------update---------------------------------------- #

# --------------------------------insert---------------------------------------- #
def insert(filePath,listItems, listTableHeader,type):
    """
    insert data into different files (database)\n
    File Path as an 1st argument (sting)\n
    List of Items as an 2nd argument (sting)\n
    TableHeader as an 3rd argument (sting)\n
    Data Type as an 4th argument (sting)\n
    return status of insert
    """

    num_cols = len(listTableHeader)
    header_row = "| "+ " | ".join(listTableHeader) + " |"
    nice_horizontal_rule = ("|" + "-" * (len(header_row)-2)+"|")
    print(nice_horizontal_rule)
    print(header_row)
    print(nice_horizontal_rule)
    status =""
    
    with open(filePath, 'a') as f:
       
      if getSearchStatus(filePath,listTableHeader[0]) == 0:
           f.write(header_row)
           f.write('\n')
      
           
      for item in listItems:
        # writing each row to a string,
        # then printing the string, is better for performance:)
        
        s = "|"
        for i in range(num_cols):
            entry = str(item[i])

            if type == "Members":
                entry = str(item)

            s += (" "+ entry+ " "*(len(listTableHeader[i]) - len(entry)+1)+ "|")
        

        if getSearchStatus(filePath,item[0]) == 0 and type != "History":
           print(s)
           f.write(s)
           f.write('\n')
           print(nice_horizontal_rule)
        elif type == "History":  
           print(s)
           f.write(s)
           f.write('\n')
           print(nice_horizontal_rule)
        else: 
           status = "Book ID already exists!" 
           
     

      return status
# --------------------------------insert---------------------------------------- #

# --------------------------------update---------------------------------------- #
def update(ID,memberId, dateToUpdate,newStatus):
    """
    update book log by ID\n
    Book ID as an 1st argument (int)\n
    oldStatus as an 2nd argument (sting)\n
    newStatus as an 3rd argument (sting)\n
    return status Loan Avilability Status
    """
 
    loanAvilabilityStatus = ""
    with open(logFilePath, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        lineNumber = 0
         
        templist = []
        headerList = []

        with open(logFilePath, 'w') as fw:
            
            for line in lines:
                # line.lower()
                # check if string present on a current line
                if lineNumber == 0:         
                    headerList  = line.split("|") 
                    headerList.pop(0)
                    headerList.pop(len(templist)-1) 
                    lineNumber += 1
                    fw.write(line)
                else:
                    templist2  = line.split("|")
                    id = str(templist2[1]).replace(" ","")
                    fileId = int(id  )
                    ID = int(ID)
                    if fileId == ID and line.index != 0:
            
                        templist  = line.split("|")    
                        templist[2] = memberId 
                        templist[6] = newStatus 
                        currentDate = str(datetime.today().strftime('%d/%m/%Y')) 
                        templist[dateToUpdate] = currentDate 

                        templist.pop(0)
                        templist.pop(len(templist)-1)  

                        numCol = len(headerList) 

                        s = "|"
                        for i in range(numCol):
                            entry = str(templist[i])

                            s += (entry+ " "*(len(headerList[i]) - len(entry)+1)+ "|")

                        fw.write(s)
                        fw.write('\n')
                    else: 
                        fw.write(line)
                

    return loanAvilabilityStatus  
# --------------------------------update---------------------------------------- #

# --------------------------------searchLogID---------------------------------------- #
def getTop(logFilePath,type):    
   
    with open(logFilePath, 'r') as fp:
        
        text = fp.readlines()
        # Create an empty dictionary
        genreDictionary = dict()
        
        
        # Loop through each line of the file
        for line in text[1:]:
            # Remove the leading spaces and newline character
            line = line.strip()
            line = line.replace(" ","")            
            templist  = line.split("|")            
            topTopic = templist[type]
            # Convert the characters in line to
            # lowercase to avoid case mismatch
            line = topTopic.lower()
        
            # Split the line into words
            words = line.split(" ")
        
            # Iterate over each word in line
            for word in words:
                # Check if the word is already in dictionary
                if word in genreDictionary:
                    # Increment count of word by 1
                    genreDictionary[word] = genreDictionary[word] + 1
                else:
                    # Add the word to dictionary with count 1
                    genreDictionary[word] = 1
              

    return genreDictionary  
# --------------------------------searchLogID---------------------------------------- #

# --------------------------------searchLogID---------------------------------------- #
def getAveragePrice(logFilePath,bookInfoFilePath,budget):    
    # this function generate recommendation list by doing the following steps 
    # 1.	Get top Genres from Book_Trascation_History based on number of checkouts/returns
    # 2.	Get average prices for each Genres
    # 3.	Create a recommended copies based on (budget/ Genres average price)
    # 4.	Combine the data in a list to be viewed in the screen 

    
    topGenreDictionarySorted = dict()
    topGenrePrices = dict()
    tempDictionary = dict()
    

    # sort the dictonary 
    tempDictionary = getTop(logFilePath,3)     
    sortedList = sorted(tempDictionary.items(), key=lambda item: item[1], reverse=True)  

    topGenreDictionarySorted = {key: value for key, value in sortedList}

    with open(bookInfoFilePath, 'r') as fp:
        
        text = fp.readlines()        
        
        # Loop through each line of the file
        for line in text[1:]:
            # Remove the leading spaces and newline character
            line = line.strip()
            line = line.replace(" ","")            
            templist  = line.split("|")            
            topTopic = templist[2]
            price = int(templist[5])
            # Convert the characters in line to
            # lowercase to avoid case mismatch
            line = topTopic.lower()
        
            # Split the line into words
            genres = line.split(" ")
        
            # Iterate over each word in line
            for genre in genres:
                # Check if the word is already in dictionary
                if genre in topGenrePrices:
                    # Increment count of word by 1
                    topGenrePrices[genre] = topGenrePrices[genre] + price
                else:
                    # Add the word to dictionary with count 1
                    topGenrePrices[genre] = price
        
        resultList =[]
        score = 0.7
        # tempList =[4]
        for genreInCount in topGenreDictionarySorted:
            
            for genreInPrice in topGenrePrices:
                if genreInCount == genreInPrice:
                   title =  genreInCount
                   count =  topGenreDictionarySorted[genreInCount]
                   averagePrice =  round(topGenrePrices[genreInPrice] / topGenreDictionarySorted[genreInCount])
                   recommededCopies = round( (budget * score) / (topGenrePrices[genreInPrice] / topGenreDictionarySorted[genreInCount]))
                   tempList = [ title, count, averagePrice, recommededCopies]

                   resultList.append(tempList)
                   budget = budget - (budget * score)
                   score -= 0.1
            
               
        print(resultList)


    return resultList  
# --------------------------------searchLogID---------------------------------------- #




from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from modules.bookSearch import *
from database import *


# --------------------------------searchMemberID---------------------------------------- #
def bookCheckOut(bookID,memberID,newStatus):
    """
    update book log by ID\n
    Book ID as an 1st argument (int)\n
    oldStatus as an 2nd argument (sting)\n
    newStatus as an 3rd argument (sting)\n
    return status Loan Avilability Status
    """
    
    update(bookID,memberID, 7,newStatus)
    
# --------------------------------searchMemberID---------------------------------------- #    
from tkinter import *
import tkinter as tk
import requests
import pandas as pd
from requests.packages.urllib3.exceptions import InsecureRequestWarning

#To ignore the Insecure Request Warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

m = Tk()

#Font style and height
LARGE_FONT= ("Cooper", 50)

#Defining the Website URL
url = 'https://www.dcrustedp.in/show_chart.php'
html = requests.get(url, verify=False).content
df_list = pd.read_html(html)

#Location of cell which contains the Date of Declaration
df = df_list[-1]
out = df.iat[0,4]

'''
Now create the function that checks the result is declared or not. In DCRUST Rsult declaration chart, initially 
the cells of table contains "X" until declaration of specific result. As soon as the result of any branch is 
declared, the "X" is replaced by the date on which the result is declared.
'''

def check():
    print(out)

    if out == "X":
        y = Label(m, text="Not Declared", font=LARGE_FONT)
        y.pack()
    else:
        l = Label(m, text="Declared !", font=LARGE_FONT)
        l.pack()

#Button for GUI Application
b4 = tk.Button(m, text="DCRUST CSE 5th Check Result",command=check)
b4.pack()

#Dimensions of Application
m.wm_geometry("450x200")

#Title of Application
m.title("DCRUST Result Checker")

m.mainloop()
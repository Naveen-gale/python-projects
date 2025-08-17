import  pyshorteners


link = input("enter the linke ")

x = pyshorteners.Shortener()
shorted_link = x.tinyurl.short(link)
print("shorted link is ", shorted_link)
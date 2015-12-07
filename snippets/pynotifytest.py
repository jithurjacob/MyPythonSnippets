import Notify
#def sendmessage(title, message):
if __name__ == '__main__':

	Notify.init("Testt")
	notice = Notify.Notification("title", "message","j")
	notice.show()
    #return
#
#sendmessage("title","hi")
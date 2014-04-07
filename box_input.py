#!/usr/bin/env python
import gtk
def responseToDialog(entry, dialog, response):
    dialog.response(response)
ans1 = "hello , i am pankaj."
def display_ans(ans):
	dialog = gtk.MessageDialog(
		None, 
		gtk.DIALOG_MODAL,
		gtk.MESSAGE_INFO,
		gtk.BUTTONS_CLOSE,
		ans)
	dialog.set_markup('Your <b> Answer </b> is :')
	dialog.format_secondary_text(ans)
	dialog.run()
	dialog.destroy()
def getText():
    #base this on a message dialog
    dialog = gtk.MessageDialog(
        None,
        gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
        gtk.MESSAGE_QUESTION,
        gtk.BUTTONS_OK,
        None)
    dialog.set_markup('Please enter your <b> QUESTION </b>:')
    #create the text input field
    entry = gtk.Entry()
    #allow the user to press enter to do ok
    entry.connect("activate", responseToDialog, dialog, gtk.RESPONSE_OK)
    #create a horizontal box to pack the entry and a label
    hbox = gtk.HBox()
    hbox.pack_start(gtk.Label("Question:"), False, 5, 5)
    hbox.pack_end(entry)
    #some secondary text
    dialog.format_secondary_markup("Please avoid spelling mistakes and no need to add [?] question mark.")
    #add it and show it
    dialog.vbox.pack_end(hbox, True, True, 0)
    dialog.show_all()
    #go go go
    dialog.run()
    text = entry.get_text()
    dialog.destroy()
    return text
if __name__ == '__main__':
    a = []
    a = getText()
    import main
    ans1 = main.get_answer(a)
    display_ans(ans1)
#    gtk.main()

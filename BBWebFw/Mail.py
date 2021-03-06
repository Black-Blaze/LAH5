from .FileRenderer import Template
import imaplib

template = Template()

class IMAP:
    def __init__(self):
        import getpass

        M = imaplib.IMAP4("imap.gmail.com", 993)
        M.login(getpass.getuser(), getpass.getpass())
        M.select()
        typ, data = M.search(None, 'ALL')
        for num in data[0].split():
            typ, data = M.fetch(num, '(RFC822)')
            print('Message %s\n%s\n' % (num, data[0][1]))
        M.close()
        M.logout()
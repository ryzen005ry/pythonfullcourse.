class dinesh():
    def phone(self):
        print("dinesh phone")

class rakesh():
    def tab (self):
        print("rakesh tab")

class mohan (dinesh,rakesh):
    def laptop(self):
        print("mohan laptop")

waheed=mohan()

waheed.tab()
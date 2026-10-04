def report_decorator(func):
    def wrapper(*args, **kwargs):
        print("=" * 60)
        print("DYNAMIC REPORT GENERATOR")
        print("=" * 60)
        func(*args, **kwargs)
        print("=" * 60)
        print("END OF REPORT")
        print("=" * 60)
    return wrapper


class Report:
    company_name = "ABC Technologies Pvt. Ltd."

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.contents = []

    def add_content(self, text):
        self.contents.append(text)

    @classmethod
    def display_report(cls, report_obj)

  

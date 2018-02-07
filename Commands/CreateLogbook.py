from Commands.Base.CommandBase import CommandBase
from Commands.Base.CommandBase import AtribType
import datetime
from Util.DateTimeUtil import DateTimeUtil
from docx import Document
from docx.shared import Inches


class CreateLogbookCommand (CommandBase):
    desc = 'Creates a logbook from/to given dates'
    usage = 'CreateLogbook'
    minArgNr = 2
    maxArgNr = 2
    types = {
        1: AtribType.DATE,
        2: AtribType.DATE
    }

    def main(self):
        fromDate = DateTimeUtil.to_date(self.args[1])
        toDate = DateTimeUtil.to_date(self.args[2])
        date_range = DateTimeUtil.get_range(fromDate, toDate)
        for date in date_range:
            if(DateTimeUtil.is_weekday(date)):
                print(str(date))
        print("Creating logbook from " + str(fromDate) + " to " + str(toDate))


command = CreateLogbookCommand (__name__ == "__main__")

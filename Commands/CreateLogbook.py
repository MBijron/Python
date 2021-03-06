from Commands.Base.CommandBase import AttributeType
from Commands.Base.CommandBase import CommandBase
from Util.DateTimeUtil import DateTimeUtil


class CreateLogbookCommand(CommandBase):
    desc = 'Creates a logbook from/to given dates'
    usage = 'CreateLogbook'
    minArgNr = 2
    maxArgNr = 2
    types = {
        1: AttributeType.DATE,
        2: AttributeType.DATE
    }

    def main(self):
        from_date = DateTimeUtil.to_date(self.args[1])
        to_date = DateTimeUtil.to_date(self.args[2])
        date_range = DateTimeUtil.get_range(from_date, to_date)
        for date in date_range:
            if DateTimeUtil.is_weekday(date):
                print(str(date))
        print("Creating logbook from " + str(from_date) + " to " + str(to_date))


command = CreateLogbookCommand(__name__ == "__main__")

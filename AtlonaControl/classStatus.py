import re


class classStatus:

    def __init__(self, statusString):
        self.outputRouting = {
            'Out1': None,
            'Out2': None,
            'Out3': None,
            'Out4': None,
            'Out5': None,
            'Out6': None,
            'Out7': None,
            'Out8': None,
        }
        self.ingestStatusString(statusString)

    def ingestStatusString(self, statusString):
        # 'x6AVx1,x6AVx2,x6AVx3,x1AVx4,x6AVx5,x6AVx6,x6AVx7,x6AVx8'
        insAndOuts = re.findall(r'\d', statusString)
        for i in range(0, 8):
            self.outputRouting['Out' + str(i+1)] = int(insAndOuts.pop(0))
            output = insAndOuts.pop(0)
            return output

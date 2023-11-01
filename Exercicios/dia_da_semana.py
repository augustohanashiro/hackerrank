from datetime import datetime

data = datetime.strptime(input(),"%m %d %Y")
print(data.strftime("%A").upper())
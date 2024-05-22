import model
import datetime
from dateutil.relativedelta import relativedelta

data = model.read_data(table="pembayaran")


for i in data:
    print(i)

# date_now = datetime.datetime.now() + relativedelta(months=+13)
# print(date_now.strftime('%Y-%m-%d %H:%M:%S'))

# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
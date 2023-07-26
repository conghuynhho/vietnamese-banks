import datetime
import requests
import json
import cookie

url = 'https://affiliate.shopee.vn/api/v1/payment_setting/bank_list'

response = requests.get(url, cookies=cookie.cookies)

# check response is success or not
if response.status_code != 200:
  print('Request error')
  exit()

# response will be in format:
# {code: 0, data: {list: [{id: 0, bank_name: "", spm_bank_id: "", country: "", valid_length_list: [], }]}}
response_json = response.json()

filtered_list = [item for item in response_json["data"]["list"] if item["sort_weight"] != 0]


# delete out the country and valid_length_list property of all item in list
for item in filtered_list:
  # delete item which has sort_weight = 0
  del item["country"]
  del item["valid_length_list"]
  del item["sort_weight"]

# get today with time
today = datetime.datetime.now()
today_str = today.strftime("%Y-%m-%d-%H-%M-%S")

# create new file
file_name = 'bank-list-' + today_str + '.json'
with open(file_name, 'w') as outfile:
  json.dump(filtered_list, outfile)

# print(response_json)

import datetime
import requests
import json
import cookie

endpoint = 'https://affiliate.shopee.vn/api/v1/payment_setting/bank_branch_list?spm_bank_id='
# read file to get bank_list
with open('bank-list-2023-07.json') as json_file:
  bank_list = json.load(json_file)

# loop through bank_list

bank_branches = []
bank_branch_indexed = {}

for item in bank_list:
  url = endpoint + str(item['spm_bank_id'])
  print(url)
  response = requests.get(url, cookies=cookie.cookies)
  # check response is success or not
  if response.status_code != 200:
    print('request fail' + url)
    continue
  # response will be in format: {data: {bank_branch_list: [{}]}}
  response_json = response.json()
  # get bank_branch_list
  bank_branch_list = response_json['data']['bank_branch_list']
  # push to bank_branches
  bank_branches.extend(bank_branch_list)
  # index bank_branch_list using key spm_bank_id
  bank_branch_indexed[item['spm_bank_id']] = bank_branch_list


# get today with time
today = datetime.datetime.now()
today_str = today.strftime("%Y-%m-%d-%H-%M-%S")

# create new file
file_name = 'bank-branches-' + today_str + '.json'
with open(file_name, 'w') as outfile:
  json.dump(bank_branches, outfile)

# create new file for bank_branch_indexed
file_name = 'bank-branches-indexed-' + today_str + '.json'
with open(file_name, 'w') as outfile:
  json.dump(bank_branch_indexed, outfile)

print('done')
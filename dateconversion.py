birthday = "1-May-12"

#Goal is to print dat as "5/1/2012"

import datetime

raw_date = "1-May-12"
date_format = "%d-%B-%y"

new_pattern = "%m/%d/%Y" 
#reading date string as it is (raw date) and the format
parsed_date = datetime.datetime.strptime(raw_date, date_format)

#print(parsed_date)
#date strand is now going to equal (calling method strftime) passing it a new format and assigning date strand
date_str = parsed_date.strftime(new_pattern) # 01/11/17

print(date_str)
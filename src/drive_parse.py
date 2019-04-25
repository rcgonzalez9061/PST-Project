import pandas as pd
import re
from datetime import datetime

pst_info = open("Y:\PST Project\PST-Files-RA.txt", 'r')
directory = None
# pst_info_str = pst_info.read()

end_of_dir_regex = r"\d +File\(s\) \s+ (\d+,)+\d+ bytes"
pst_df = pd.DataFrame(columns=['Name', 'User', 'Size', 'Date', 'Directory'])

line = pst_info.readline()
end_regex = r"\s+Total Files Listed:"
date_regex = r'\d{2}/\d{2}/\d{4}.{9}M'
size_regex = r'(\d+,)+\d+'


while not re.findall(end_regex, line):
    # print(line)
    if "Directory of " in line:
        directory = line[14:-1]
    # elif re.findall(end_of_dir_regex, line):
        # print("break")
    elif re.search(date_regex, line):
        # date and time handling
        date_and_time = re.search(date_regex, line).group()
        date_time_obj = datetime.strptime(date_and_time, "%m/%d/%Y  %H:%M %p")
        date = date_time_obj.date()
        time = date_time_obj.time()

        # Size handling
        size = re.search(size_regex, line).group()

        # Name handling
        len_before_size = 25
        name = line[39:-1]

        # User handling
        user = None
        if re.search(r'\\USERS\\(\w| )+', directory):
            user = re.search(r'\\USERS\\(\w| )+', directory).group()[7:]

        # Insert to dataframe
        pst_df.loc[len(pst_df)] = [name, user, size, date, directory]
    else:
        if line != '\n':
            print(line)

    # Go to next line
    line = pst_info.readline()

print(pst_df)
pst_df.to_csv('Y:\PST Project\psts.csv')
pst_info.close()


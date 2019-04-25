import numpy as np
import pandas as pd
import re

pst_info = open("Y:\PST Project\PST-Files-RA.txt", 'r')
pst_info_str = pst_info.read()

end_of_dir_regex = "\d +File\(s\) \s+ (\d+,)+\d+ bytes"

pst_dataframe = pd.DataFrame()


pst_info.close()


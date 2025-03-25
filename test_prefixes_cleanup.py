

# check which DOIs are on a test prefix, such as 10.5555, 10.505050
# from API calls:
# https://api.crossref.org/members?query=test%20accounts
# https://api.crossref.org/members?query=Crossref

import pandas as pd
from pandas import DataFrame, Series
from colorama import Fore,Style,Back,init # just for fun

test_prefixes = ["10.5555",
                "10.88888",
                "10.30444",
                "10.30446",
                "10.30447",
                "10.30448",
                "10.30449",
                "10.50505",
                "10.30443"]

# check if prefixes are in 'doi'
# just playing with type annotation here
def get_strings_in_column(
    df: DataFrame,
    column: str,
    search_strings: List[str],
    case: bool = False,
    regex: bool = False) -> Series:
    pattern: str = '|'.join(search_strings)
    return df[df[column].str.contains(
        pattern,
        case=case,
        regex=regex,
        na=False
    )]

    # If you want the entire DataFrame rows that match:
mask = df['doi'].str.contains('|'.join(test_prefixes),na=False)
matching_rows: DataFrame = df[mask]

# you can get rid of the Fore formatting options. I just use it for fun.
print(Fore.MAGENTA + f"number of matching rows: {len(matching_rows)}")
print(Style.RESET_ALL) # can be removed if you don't like colorama'
matching_rows


 #If you want just the matching values from the specified column:
matching_values: Series = df[df['doi'].str.contains('|'.join(test_prefixes), na=False)]['doi']

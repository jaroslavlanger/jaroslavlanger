# pandas

*The alpha and omega of work with data.*

`2021 Feb 03, Jaroslav Langer`

## Contents

<!-- TOC GFM -->

* [Documentation](#documentation)
* [First things first](#first-things-first)
    * [Import pandas](#import-pandas)
* [DataFrame and Series](#dataframe-and-series)
    * [Series](#series)
        * [Accessing a series](#accessing-a-series)
    * [DataFrame](#dataframe)
* [Get data into DataFrames](#get-data-into-dataframes)
    * [Get dataframe from csv](#get-dataframe-from-csv)
    * [Write dataframe to csv](#write-dataframe-to-csv)
    * [Dataframe form dictionary](#dataframe-form-dictionary)
    * [Dataframe from list of lists (list per row)](#dataframe-from-list-of-lists-list-per-row)
    * [DataFrame from XML](#dataframe-from-xml)
    * [Srapping web (HTML)](#srapping-web-html)
        * [Using requests library](#using-requests-library)
    * [Dataframe from json](#dataframe-from-json)
* [Accessing the Dataframe](#accessing-the-dataframe)
    * [First look at the Dataframe](#first-look-at-the-dataframe)
        * [Show all columns (if not shown by default)](#show-all-columns-if-not-shown-by-default)
    * [Dataframe properties](#dataframe-properties)
    * [Dataframe functions](#dataframe-functions)
* [Accessing data](#accessing-data)
    * [Accessing columns](#accessing-columns)
    * [Accessing rows](#accessing-rows)
    * [Chained indexing](#chained-indexing)
    * [Returning a view versus a copy - Chained indexing problem](#returning-a-view-versus-a-copy---chained-indexing-problem)
    * [loc - specify rows, and cols at the same time](#loc---specify-rows-and-cols-at-the-same-time)
    * [iloc - accessing rows and columns through indices](#iloc---accessing-rows-and-columns-through-indices)
    * [Filtering rows](#filtering-rows)
    * [Column Functions](#column-functions)
* [Modifying the dataframe](#modifying-the-dataframe)
    * [Dataframe copying and joining](#dataframe-copying-and-joining)
    * [Drop duplicates, replace values, sort axis](#drop-duplicates-replace-values-sort-axis)
    * [Missing values types](#missing-values-types)
    * [Index stuff](#index-stuff)
    * [Work with dataframe columns](#work-with-dataframe-columns)
    * [Columns datatypes](#columns-datatypes)
        * [One-hot encoding](#one-hot-encoding)
    * [Modify values](#modify-values)
        * [Apply](#apply)
        * [Map new values onto old ones](#map-new-values-onto-old-ones)
    * [String methods](#string-methods)
        * [Match (regex)](#match-regex)
        * [Extract (regex)](#extract-regex)
        * [Replace (regex)](#replace-regex)
        * [Contains (regex)](#contains-regex)
    * [Discretize Column Values](#discretize-column-values)
    * [Group by](#group-by)
* [Poltting the data](#poltting-the-data)
    * [Plot the data](#plot-the-data)
* [Computational Tools](#computational-tools)
* [Advanced features](#advanced-features)
    * [MultiIndex](#multiindex)

<!-- /TOC -->

## Documentation

- [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/reference/)

## First things first

### Import pandas

```py
import pandas as pd
import numpy as np
```

## DataFrame and Series

### Series

One-dimensional ndarray with axis labels (including time series).

```py
# Create a series
ser_def = pd.Series(["car", "bus", "train", "plane"])
ser_alpha = pd.Series(["car", "bus", "train", "plane"], index=list('abcd'))
ser_num = pd.Series(["car", "bus", "train", "plane"], index=[4,3,2,1])

# Show series with default index
ser_def
# 0      car
# 1      bus
# 2    train
# 3    plane
# dtype: object

# Get Series values (np.array)
ser_alpha.values        # array(['car', 'bus', 'train', 'plane'], dtype=object)

# Get Series index
ser_alpha.index         # Index(['a', 'b', 'c', 'd'], dtype='object')
```

- [Series](https://pandas.pydata.org/pandas-docs/stable/reference/series.html)

#### Accessing a series

```py
# Access item by index
ser_alpha['a']      # 'car'
# The dot notation is possible if the name is simple
ser_alpha.a         # 'car'

# Access item by position
ser_alpha[0]        # 'car'

# In case the index is numerical, the position access is not possible
ser_num[1]          # 'plane'
ser_num[0]          # KeyError: 0

# The position access is possible trough values
ser_num.values[0]   # 'car

# It is possible to slice the series with a given range
ser_num[0:1]
# 4    car
# dtype: object

# Slice is also possible with enumeration of the inices you want to
ser_num[[4,3]]
# 4    car
# 3    bus
# dtype: object
```

### DataFrame

Two-dimensional, size-mutable, potentially heterogeneous tabular data.

- [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)

## Get data into DataFrames

### Get dataframe from csv

```py
data1 = pd.read_csv('./path/data1.csv')
# Other separator? No problem.
data2 = pd.read_csv('./path/data2.csv', sep=';', decimal=',')
# Specify rows for header of the table
data2 = pd.read_csv('./path/data2.csv',header=[0,1])
# Use different headers - names
candidates = pd.read_csv('./candidates.csv', names=columnsNamesList)
# Don't read index from csv
candidates = pd.read_csv('./candidates.csv', index=False)
```

### Write dataframe to csv

```py
# Write dataframe to csv
df.to_csv('./path/data1_new.csv')
# Write row names (index)
candidates.to_csv('./candidates.csv', index=False)
```

### Dataframe form dictionary

```py
lists = [[1,2,3,4], [2,3,4], [5,2,4,7,8], [5,2]]
lengths = [len(sublist) for sublist in lists]

df_dict = {"lengths": lengths, "lists": lists}
df = pd.DataFrame(df_dict)
```

- [df from dicts and lists](https://pbpython.com/pandas-list-dict.html)

### Dataframe from list of lists (list per row)

```py
from random import choice, randrange, uniform

NAMES =             ['Jason', 'Molly', 'Tina', 'Jake', 'Amy']
SURNAMES =          ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze']
LEN = 100

COLUMNS = ['first_name', 'last_name', 'age', 'score']

df_list = [[
    choice(NAMES), 
    choice(SURNAMES),
    randrange(0, 101, 1),
    round(uniform(0, 10), randrange(0, 4, 1)),
    ])
] for x in range(0,LEN)]

df = pd.DataFrame(df_list, columns=COLUMNS)
```

### DataFrame from XML

```py
for node in xroot: 
    s_name = node.attrib.get("name")
    s_mail = node.find("email").text if node is not None else None
    s_grade = node.find("grade").text if node is not None else None
    s_age = node.find("age").text if node is not None else None
    
    rows.append({"name": s_name, "email": s_mail,
                 "grade": s_grade, "age": s_age})

out_df = pd.DataFrame(rows, columns = df_cols)
```

- [source](https://medium.com/@robertopreste/from-xml-to-pandas-dataframes-9292980b1c1c)

### Srapping web (HTML)

```py
# Some url, example given
url = 'https://www.volby.cz/pls/kv2010/kv1111?xjazyk=CZ&xid=0&xdz=3&xnumnuts=2103&xobec=532053&xstat=0&xvyber=0'

# Straight swth url it works better (resolved encoding automaticaly)
dfs = pd.read_html(url,flavor='html5lib')

# display(len(dfs))
display(dfs[1])
```

#### Using requests library

Method with requests (not recommended for simple tasks)

```py
# Imports
import requests
import html5lib
```

```py
r = requests.get(url)
dfs = pd.read_html(r.text,flavor='html5lib')

# Prepared data for the post request
data = {
    'input_name':   'value',
    'thesis':       'BP',     # Type of thesis options [BP, DP, DR, RI]
    'name':         '%%%',    # The name must have at least three letters in its name
    'number':       '0',
    'keyword':      '',
    'match':        'c',      # c = complete match, n = partial match
    'button_name':  'ActionValue'
}
data_all = pd.DataFrame()
r = requests.post(url, data)

# Important trifle
r.encoding='cp1250'

# header=0 means use row 0 to make the headers
ldf = pd.read_html(r.text,flavor='html5lib', header=0)
df = ldf[0]
```

### Dataframe from json

```py
pd.read_json("./time_spent.json", orient="index")
```

- [types of json structure](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html)

## Accessing the Dataframe

### First look at the Dataframe

```py
# Get first(/last) few lines (5 by default)
df.head()
df.tail()

# Get random row (/ n rows)
df.sample()
df.sample(n=5)

# Get info about column names, types, number of not null items..
df.info()

# Basic statistic info like mean, std, min, max...
df.describe()
```

- [randomly select rows - GeeksforGeeks](https://www.geeksforgeeks.org/how-to-randomly-select-rows-from-pandas-dataframe/)

#### Show all columns (if not shown by default)

```py
pd.set_option("max_columns", None)
display(df.head())
pd.reset_option("max_columns")
```

- [source](https://towardsdatascience.com/how-to-show-all-columns-rows-of-a-pandas-dataframe-c49d4507fcf)

### Dataframe properties

```py
# Tuple of dataframe rows number and columns number
df.shape

# Array with column names
df.columns

# Range index of data
df.index

# Array(/s) from Dataframe
df.values

# Types of columns
df.dtypes

# Information whether the dataframe empty
df.empty
```

### Dataframe functions

```py
# Number of unique values in every column (by default ignores NaN)
df.nunique()

# Sum all the data in every column
df.sum()

# Creates table of same size, every value is represented with boolean isnull NaN -> True
df.isnull() # synonym to `df.isna()`
df.notnull()
# Handy usage of previous functions, see number of NaN (/not NaN) values per column
df.isnull().sum()
df.notnull().sum()
# Get number of not-NA values
df.count()

# Get max(/min) value for every column
df.max() # df.min()
# Get indexes of max(/min) value for every column
df.idxmax() # df.idxmin()

# Correlation matrix
cor_matrix = df.corr()

# Compare if dataframes have same items (column types might be different)
df1.equals(df2)

# Get series where True means a row is duplicated
df.duplicated()
# By default, first occurrence of a row is not duplicate, use False for every duplicated row be marked False
df.duplicated(False)

# Return series where True means all values of specified axis are True (by default axis=0 ~ rows)
df.all()
# Return series where True means at least one value specified axis is True
df.any()

# Is the index unique?
df.index.is_unique()
```

## Accessing data

```py
# Create dataframe with numerical columns and indices
default_df = pd.DataFrame( [list('abc'),list('def'),list('ghi')])

default_df
#    0  1  2
# 0  a  b  c
# 1  d  e  f
# 2  g  h  i

# Create dataframe with letters as column indices
letters_df = pd.DataFrame(
    [list('abc'),list('def'),list('ghi')], columns=list('abc')
)

letters_df
#    a  b  c
# 0  a  b  c
# 1  d  e  f
# 2  g  h  i
```

### Accessing columns

```py
# Single bracket access [value] returns Series of a specified column
letters_df['a']
# 0    a
# 1    d
# 2    g
# Name: 1, dtype: object

# It is also possible to use attribute access of column by its name
letters_df.a

# Double bracket access [[]] returns dataframe slice of specified **columns**
default_df[[0, 2]]
#    0  2
# 0  a  c
# 1  d  f
# 2  g  i

# If column indices are tuples, or in case of multiindex, access with tuple
data[('name', 'age')] # or data['name', 'age']

# Access columns by type
df.select_dtypes(include=['int64', 'float64'])
```

### Accessing rows

```py
# Specify rows like this is not possible, no matter the columns are letters
letters_df[0]   # KeyError: 0

# The slice [range] always returns DataFrame of specified rows never columns
default_df[1:2]
#    0  1  2
# 1  d  e  f

# Rows can be iterated as (index, series of a row with column index)
for index, series in default_df.iterrows():
    print(f'index: {index}, row[1]: {series[1]}')
# index: 0, row[1]: b
# index: 1, row[1]: e
# index: 2, row[1]: h
```

### Chained indexing

As the result of a bracket accessing can be a dataframe or a series, another bracket access can be applied to the result so the brackets are chained.

```py
# First brackets returns series and second returns inidces 0 and 2
letters_df['a'][[0,2]]
# 0    a
# 2    g
# Name: a, dtype: object
```

### Returning a view versus a copy - Chained indexing problem

There is not much a problem as long as the data are accessed for getting not for setting. As it was told with the chained indexing, the first brackets returns an object that can be accessed with another brackets, however it may not be the original data it can be a copy of it, so if we try to change values on result of two two bracket accesses we can not be sure we modify the original object because we can be modifying only its copy. In purpose to eliminate this risk there are two functions that can do column and row indexing at the same time so it is safe to modify the values returned by them.

- [returning-a-view-versus-a-copy (pandas.pydata.org)](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy)

### loc - specify rows, and cols at the same time

Usage: dataFrame.loc[<ROWS RANGE> , <COLUMNS RANGE>]

WARNING: loc slices include the last element, not like python slices!

```py
# LOC takes 2:5 like [2,3,4,5]
data1.loc[2:5, ['Name', 'Age']]
# Same as (the 5 is there correctly, weird)
data1.loc[[2,3,4,5], ['Name', 'Age']]
# Access row 235426
df.loc[235426]
# Access rows by list of row numbers
df.loc[[1,13452,3452]]
# Access rows by index
sample = df1.sample(n=5)
df.loc[sample.index]
```

### iloc - accessing rows and columns through indices

Usage: dataFrame.iloc[<ROWS INDEX RANGE> , <COLUMNS INDEX RANGE>]

```py
# ILOC takes 2:5 like [2,3,4]
data1.iloc[2:5, [3,5]]
# Same as
data1.iloc[[2,3,4], [3,5]]
# i stands for integer (takes bool as well [booleans].values)
# iloc with booleans (take arrays)
data1.iloc[(data1['Age'] < 30).values, [3,5]]
```
- [usages from here](https://thispointer.com/select-rows-columns-by-name-or-index-in-dataframe-using-loc-iloc-python-pandas/)
- [loc iloc source](https://www.pythonprogramming.in/what-is-difference-between-iloc-and-loc-in-pandas.html)

### Filtering rows

```py
# Create filter -> df of True/False
filter = data1['Age'] > 30
# Check if value is in list of values
filter = data1['Age'].isin([30,31,32])
# Applying filter, returns rows where the filter row is True
data1[filter]
# Applying array filters only True will be returned
data1['Age'][-3:][[True, False, True]]
# Same as
data1['Age'][filter.values]

# Filter negation
data1[~filter]
# Combining more filters
# Filter1 and filter2
data1[filter1 & filter2]
# Filter1 or filter2
data1[filter1 | filter2]
```

### Column Functions

```py
# List of unique values (includes nan)
df.name.unique()

# Counts unique values (excluding nan)
df.name.nunique()
# Include NaN as a value
df[GN].nunique(False) == (df[GN].nunique() + 1) = len(df[GN].unique()) # True

# Count values
df[col].value_counts()

df.name.nsmallest(3)
df.name.nlargest(3)

# Statistical information
df["score"].mean()
df["score"].median()
df["score"].mode()
df["score"].var()
df["score"].quantile(0.25)
```

## Modifying the dataframe

### Dataframe copying and joining

```py
# First to deep copy the data (important)
df = df_original.copy()

# Concatenate rows of multiple DataFrames
df = pd.concat([df_1,df_2])
# Ignore current indices
df = pd.concat([df_1,df_2], ignore_index=True)
# Concatenate columns of more dataframes
df = df = pd.concat([df_1, df_2], axis=1)

# SQL-like join, how=inner is the default option
comparison_df = computed_df.merge(correct_df, how='left', on=['dataset', 'idx', 'n'])
```

* [pd.concat (Pandas documentation)](https://pandas.pydata.org/docs/reference/api/pandas.concat.html#pandas.concat)
* [merge (pandas.pydata.org)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html#pandas.DataFrame.merge)

### Drop duplicates, replace values, sort axis

```py
# Drop duplicated rows
df = df.drop_duplicates(keep='first')
# Drop rows with the same 'dataset', 'n' and 'idx' values
df = df.drop_duplicates(subset=['dataset', 'n', 'idx'])

# Replace values
df = df.replace('?', np.nan)

# Sort rows or columns # only kind='mergesort' is stable
df.sort_values(by='date', axis=0, ascending=True, inplace=True, kind='quicksort')
```

* [drop_duplicates (pandas.pydata.org)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html)

### Missing values types

There are multiple ways the missing values may be represented. Now do not consider values that are missing by the values logic (e.g. string "?") let's talk only values that are missing by its type.

```py
type('')            # <class 'str'>

type(None)          # <class 'NoneType'>

type(float('nan'))  # <class 'float'>

type(np.nan)        # <class 'float'>

type(pd.NA)         # <class 'pandas._libs.missing.NAType'>
```

Fill missing values, drop rows (/columns) with missing values.

```py
df = pd.DataFrame([
        ['?', '?'],
        ['', ''],
        ['None', None],
        ["float('nan')", float('nan')],
        ['np.nan', np.nan],
        ['pd.NA', pd.NA],
])

print(df)
#               0     1
# 0             ?     ?
# 1                    
# 2          None  None
# 3  float('nan')   NaN
# 4        np.nan   NaN
# 5         pd.NA  <NA>

print(df.fillna('XXX'))
#               0    1
# 0             ?    ?
# 1                   
# 2          None  XXX
# 3  float('nan')  XXX
# 4        np.nan  XXX
# 5         pd.NA  XXX

print(df.dropna())
#    0  1
# 0  ?  ?
# 1      
```

* [fillna (pandas.pydata.org)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html)
* [dropna (pandas.pydata.org)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html)

### Index stuff

```py
# Set index from column
df.set_index('column_name')
# Check if indices are unique
df.set_index('column_name', verify_integrity=True)

# Updating the index
df.index = range(df.shape[0])

# Make column from index and set index to default
df.reset_index()

# Sort dataframe by index
df = df.sort_index(ascending=False, ignore_index=True)

# Remove duplicated indices
df = df[~df3.index.duplicated(keep='first')]

# Shift index values
df.index = df.index - 2     # shrink index values by 2

# Shift values by given axis
df = df.shift(-1) # shift rows one up (lose first row, get last row empty)

# Get common columns for two dataframes
common_cols = df_1.index.intersection(df_2.index)

# See what columns miss in the other dataframe
add = train_X.columns.difference(test_X.columns) # Missing in test_X, needs to be added to test_X
drop = test_X.columns.difference(train_X.columns) # Missing in train_X, needs to be dropped from test_X
```

- [index](https://pandas.pydata.org/pandas-docs/stable/reference/indexing.html)
- [reset_index](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html)
- [shift (pandas docs)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shift.html)
- [remove duplicated indices](https://stackoverflow.com/questions/13035764/remove-rows-with-duplicate-indices-pandas-dataframe-and-timeseries)

### Work with dataframe columns

```py
# Drop columns
df_tmp = df_tmp.drop(['FootSize',df.columns[0]], axis=1)
df_tmp = df_tmp.drop(drop_cols, axis=1, errors='ignore') # ignore when columns are not present

# Rename columns
df.columns = [COLNAME1, COLNAME1, COLNAME1]
# Rename specific columns
df = df.rename(columns = {'BirthYear': 'Age'})
# Rename columns with numbers from range
df.columns = range(12)

# Add multiple columns
df[['nans', 'zeros']] = pd.DataFrame([[np.nan, 0]], index=df.index)
# Add column (colNumber, name(multiindex here), columnData, allowDuplicates)
df.insert(2, ("Age","Age"), [21, 23, 24, 21], True)
# Better example
yearColumn = [year for x in range(candidates_tmp.shape[0])]
candidates_tmp.insert(0, ("Rok","Rok"), yearColumn, False)

# Reorder columns
df = df[[3, 4, 0, 1, 2, 5, 6, 7, 8, 9]]
# Or
df = df.reindex(columns=['mean',0,1,2,3,4])
# Sort order of columns
df = df.reindex(sorted(df.columns), axis=1)

# Add multiple columns (all columns from another dataframe)
extracted_columns = df[feature].str.extract(extract_pattern)
df = df.join(extracted_columns)
```

- [insert (pandas.pydata.org)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.insert.html)
- [Join](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html)
- [add multiple columns 8 ways (stackoverflow)](https://stackoverflow.com/questions/39050539/how-to-add-multiple-columns-to-pandas-dataframe-in-one-assignment)

### Columns datatypes

```py
# convert column "a" of a DataFrame to number type
df["a"] = pd.to_numeric(df["a"])

# Change columns type to datetime
df[df.columns[0]] = pd.to_datetime(df.columns[0], format='%d.%m.%Y')
# Convert column to timedelta
df.cpu_time = pd.to_timedelta(df.cpu_time)
df.wall_time = df.wall_time.apply(lambda x: pd.to_timedelta(x).total_seconds())

# Using apply (conversion to string)
df["column"] = df["column"].apply(str)

# Astype
df[NUM] = df[NUM].astype('float64')
df[feature] = df[feature].astype(bool)
# Categories
data['embarked'] = data[['embarked']].astype('category').apply(lambda x: x.cat.codes)
# Change to categories and replace values with category codes
df[feature] = df[feature].astype('category').cat.codes
# Ordinal categories # if there is missing category for a value, it is encoded with `-1`
df[feature] = df[feature].astype(pd.CategoricalDtype(categories=['b', 'a'], ordered=True)).cat.codes
# Days from datetime
rfm[RECENCY] = rfm[RECENCY].astype('timedelta64[D]')
```

- [CategoricalDtype](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.CategoricalDtype.html)
- [python date time formats](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)

#### One-hot encoding

```py
pd.get_dummies(train_x[features], dtype=bool)
```

- [get_dummies](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html)

### Modify values

```py
# Unlike arrays, with df doesn't work changing values of slices
df['Age'][0:10] = 10
# Change value of slice
df.loc[0:10, ['Age']] = 0

# Change all data of one column
data2_tmp['Age'] = 1912 - data2_tmp['Age']
```

#### Apply

For more complicated changes (works either for rows or columns).
Called with dataframe default `axis=0` i.e. iterates over columns `axis=1` iterates over rows.

```py
data['Sex'] = data['Sex'].apply(lambda x: 1 if x == 'female' else 0)

# Default axis for DataFrame.apply is axis=0 (goes through lines)
# to access columns use axis=1
candidates[DEGREE] = candidates[[DEGREE, DEGREE_TMP]].apply(lambda x:
    np.nan if (pd.isnull(x[0]) & pd.isnull(x[1])) else
        x[0] if pd.isnull(x[1]) else
            x[1] if pd.isnull(x[0]) else x[0]+x[1], axis=1)

# Apply with function called in lambda
df['col_3'] = df.apply(lambda x: f(x.col_1, x.col_2), axis=1)
```

- [link to lambda with function](https://stackoverflow.com/questions/13331698/how-to-apply-a-function-to-two-columns-of-pandas-dataframe)
- [apply](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html)

#### Map new values onto old ones

```py
# Substitute 'content_id' values with 'tags' by 'content_id'
test_df['content_id'] = test_df['content_id']\
    .map(questions_df.set_index('content_id')['tags'])
```

- [replace column values in one dataframe by values of another dataframe (stackoverflow)](https://stackoverflow.com/questions/36413993/replace-column-values-in-one-dataframe-by-values-of-another-dataframe)
- [Series.map (pydata.pydata.org)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html)

### String methods

Values that are not transformable to string results in NaN, or raise an error.

```py
df["column"].str.len()

df["column"].str.lower()

# Strip 
df["column"] = df["column"].str.strip()

# String values transformable to numbers are True, nontransformable False, and not string result in Nan
df["column"].str.isnumeric()
```

- [strip](https://www.geeksforgeeks.org/python-pandas-series-str-strip-lstrip-and-rstrip/)

#### Match (regex)

```py
numeral_filter = df['ticket'].str.match(r'(\A[0-9]+\Z)', case=False)==True
df['ticket'] = df['ticket'].apply(lambda x: np.nan if x == '' else x) 
display(df[numeral_filter].shape[0])
display(df[~numeral_filter])

Series.str.match(pattern, case=True, flags=0, na=nan)
```

- [pandas match](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.match.html)

#### Extract (regex)

```py
s.str.extract(r'(?P<letter>[ab])(?P<digit>\d)')
```

Output:

```out
  letter digit
0      a     1
1      b     2
2    NaN   NaN
```

- [pandas extract](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.extract.html)

```py
degreeNP = r'DiS|Dipl\.um.'
degreeR = r'Bc|BBA'
degreeT = r'Ing|Mgr|MUDr|PaedDr|JUDr|Dr|RNDr|MVDr|PhDr|RSDr|PhMr|MgA|MBA|Prim'
degreeV = r'Ph\.?D|Doc|Prof'
postNominalPattern = r'\s({NP}|{R}|{T}|{V})(\.|\s|\Z).*'.format(NP=degreeNP, R=degreeR, T=degreeT, V=degreeV)

postDegreePattern = r'.*(?P<{columnName}>\s({NP}|{R}|{T}|{V})(\.|\s|\Z).*)'\
    .format(columnName=DEGREE_TMP, NP=degreeNP, R=degreeR, T=degreeT, V=degreeV)

columns = candidates[NAME_SURNAME].str.extract(postDegreePattern, flags=re.IGNORECASE)
```

#### Replace (regex)

```py
# This example deletes anything (specified by `postNominalPattern` regex) after the name and surname
df[NAME_SURNAME] = df[NAME_SURNAME].str.replace(postNominalPattern, '', flags=re.IGNORECASE)
```

- [pandas replace](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.replace.html)
- [How to use Regex in Pandas](https://kanoki.org/2019/11/12/how-to-use-regex-in-pandas/)

#### Contains (regex)

```py
# Number of strings that contains regex r'X\.\d+' e.g. "x.723"
df[feature].str.contains(r"X\.\d+", case=False).sum()
```

- [contains (pandas documentation)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.contains.html)

### Discretize Column Values


```py
# Bin values into discrete intervals.
feature = "age"
interval_num = 10
bin_labels = list(ranger(interval_num))

# Equal width intervals
pd.cut(df[feature], interval_num, labels=bin_labels)
# Equal depth (frequency) intervals
pd.qcut(df[feature], interval_num, labels=bin_labels)
```

- [cut](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.cut.html)
- [qcut](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.qcut.html)

### Group by

Returns DataFrameGroupBy object. Works similarly as sql groupby.

```py
# Get 5 students with largest number of unique questions.
data.groupby('student')['question'].nunique().nlargest(5)

# Get number of thesis with the same name sorted by number of occurrences.
data[data['year'] > 2000].groupby(['theses_name']).size().sort_values(ascending=False)

# Get sample of each category
sample = df.groupby("category").sample(n=100)

# Mean
df = df.groupby(["method", "n"]).mean()

# Aggregate
df = df.agg(['mean', 'max'])

# Mode
mediumModes = df.groupby(DEP)[MED].apply(lambda x: x.mode())
# Or
mostCommonMediumForEveryDepartment = {}
for dep, group in df[[DEP, MED]].groupby(DEP):
    sizes = group.groupby("Medium").size()
    mostCommonMediumForEveryDepartment[dep] = sizes[sizes == sizes.max()].index.values[0]
```

- [groupby](https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html)
- [groupby.sample](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.DataFrameGroupBy.sample.html)
- [.agg()](https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.core.groupby.DataFrameGroupBy.agg.html)
- [pivot table](https://tryolabs.com/blog/2017/03/16/pandas-seaborn-a-guide-to-handle-visualize-data-elegantly/)

## Poltting the data

### Plot the data

```py
# Basic plot
data.plot()

# figsize=(10,10) size of figure in inches
data.plot(figsize=(10,10))

# Specified type of the graph
data.Age.plot(kind='bar')
# Properties (stacked, line width, figsize)
df.plot(kind='bar', stacked=True, figsize=(18, 15), width=1)
# Horizontal bar with specified colormap
candidates_by_party.plot(kind='barh', colormap=myColors)

# Histogram (bins = number of piles)
data.Age.plot(kind='hist', bins=50)
# Same as
data.Age.hist(color='green', bins=50)

# Scatter
survived.plot.scatter(x='Age', y='Pclass', color='Green', label='Survived')

# Plot one graph (graph2) on another (graph1)
graph1 = not_survived.Age.hist()
data2.Age.plot.hist(ax = graph1)
```

- [area link ](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.area.html)
- [area plot](https://stackoverflow.com/questions/55214249/how-to-create-an-area-plot-in-seaborn)

## Computational Tools

[Computational tools Pandas User Guide](https://pandas-docs.github.io/pandas-docs-travis/user_guide/computation.html)

```py
# Compute percent change over a given number of periods (1 by default).
series.pct_change()

# Rolling window, multiple functions may be applied such as mean, max, var, etc.
series.rolling(window=7).mean()

# Extending Exponentially Weighted Window calculations.
series.ewm(alpha=0.9, adjust=False).mean()
```

## Advanced features

### MultiIndex

Way how to better structure data in 2D

```py
# Create MultiIndex #
df.columns = pd.MultiIndex.from_tuples([
    ('n',  ''),
    ('step', 'first'),
    ('step', 'second'),
])
# Compare two MultiIndices #
len(df.columns.difference(df_2.columns).values) > 0

# Rename MultiIndex columns
df = df.rename(columns={'first': 0, 'second': 1}, level=1)

# Flatten the MultiIndex into Index of tuples
df.columns.to_flat_index()

# Drop level from multiindex
df.columns.droplevel(1)

# Create columns from multiindex level
df.reset_index()        # removes all levels
df.reset_index(level=2) # removes only the second level

# Stack level from columns to index
df.stack()  # stacks the deepest column level into index
df.stack(0) # stacks the outher column level into index

# Create columns from index level
df.unstack()        # Creates columns from the deepest index level
df.unstack(level=0) # Creates columns from the most outher index level

# From multiple columns one column with multiple rows
df = pd.melt(df, id_vars=["data_name", 'model_name'],
        var_name='score', value_name='score_value')
```

* [MultiIndex / advanced indexing (pandas.pydata.org)](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html)
* [droplevel (pandas.pydata.org)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.MultiIndex.droplevel.html)
* [reset_index (pandas)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html)
* [unstack](https://stackoverflow.com/questions/26255671/pandas-column-values-to-columns)
* [melt](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html)
* [melt (stackoverflow)](https://stackoverflow.com/questions/50098113/convert-columns-into-multiple-rows-in-pandas-dataframe)


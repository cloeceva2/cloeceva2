"""
Pandas walkthrough
"""

from typing import Any

# omg so much documentation...
# https://pandas.pydata.org/docs/reference/index.html
import pandas as pd

###############
# Constants
###############

DATA_FNAME: str = "L10_coffee.csv"
DATA: dict[str, Any] = {
    'roaster': ['dunkin', 'onyx', 'pavement'],
    'name': ['original blend', 'ethiopia bochesa natural', 'Rathskeller'],
    'grams': [2040, 283, 20],
    'price': [47.82, 27, 1.05]
}

###############

def get_data_csv() -> pd.DataFrame:
    """
    Gets sample data from a CSV

    Returns
    =======
    pd.DataFrame
        ☕️ data

    Raises
    ======
    FileNotFoundError
        Cannot find DATA_FNAME
    """

    return pd.read_csv(DATA_FNAME)

def get_data_literal() -> pd.DataFrame:
    """
    Gets sample data from Python code

    Returns
    =======
    pd.DataFrame
        ☕️ data
    """

    return pd.DataFrame(DATA)


def data_structure() -> pd.DataFrame:
    """
    Looks at the data big-picture
    """

    csv_df: pd.DataFrame = get_data_csv()
    python_df: pd.DataFrame = get_data_literal()

    # seeing what the csv produces in code :)
    print(f"DFs are same: { csv_df.equals(python_df) }")

    # shape is table dimensions
    # review: what's the type?
    # (and len(df) is also # rows)
    print(f"Shape (|rows|, |cols|): "
          f"{ csv_df.shape } and ({ len(csv_df) }, { len(csv_df.columns) }) vs "
          f"({ len(DATA[list(DATA.keys())[0]]) }, { len(DATA.keys()) })")

    # can also access column info
    print("Columns... ")
    for c in DATA:
        print(f"  { c } is a column? { c in csv_df.columns }")
    print()

    # and then some great stats 🤓
    print(csv_df.describe())
    print()
    print(f"Max size: { csv_df['grams'].max() }")
    print()

    return csv_df


def access_data(df: pd.DataFrame) -> bool:
    """
    Examples of accessing/seeing data
    """

    # pretty table :)
    print(type(df))
    print(df)
    print()

    # can loop row-by-row
    for idx,row in df.iterrows():
        print(idx, type(row))
        print(row)
        print()

    # and easy to see top-k/bottom-k rows
    print(type(df.head()))
    print(df.head(2))
    print()
    print(df.tail(1))
    print()

    # can also access particular rows (via iloc)
    print(type(df.iloc[1]))
    print(df.iloc[1])
    print()

    # and columns (via [])
    print(type(df['roaster']))
    print(df['roaster'])
    print()

    # subsets via filtering
    print(df[df['roaster'] != 'dunkin'])
    print()
    print(df[15 * df['price'] / df['grams'] < 1])
    print()

    # sorting
    print(df.sort_values(by="roaster", ascending=False))
    print()

    # reminder of Python
    print(sorted(DATA['roaster'], reverse=True))
    print()


def manipulate_data(df: pd.DataFrame) -> bool:
    # can always make a copy
    df_expanded: pd.DataFrame = df.copy()

    # there are multiple ways to add rows, such as...
    df_expanded = pd.concat([df_expanded, pd.DataFrame({
        'roaster': ['onyx'],
        'name': ['ethiopia keramo anaerobic natural'],
        'grams': [283],
        'price': [38]
    })], ignore_index=True)
    print(df_expanded)
    print()

    # and then detect distinct
    # (similar to set of values)
    print(df_expanded['roaster'].unique())
    print()

    # add a computed column
    df_expanded['cup'] = 15 * df['price'] / df['grams']
    print(df_expanded)
    print()

    # oh no, seems there's something amiss!!
    print(df_expanded[df_expanded['cup'].isna()])
    print()

    # could remove...
    print(df_expanded.dropna())
    print()

    # but let's fix this up...
    df_expanded['cup'] = 15 * df_expanded['price'] / df_expanded['grams']
    print(df_expanded)
    print()

    # detecting local brands
    print(df_expanded[df_expanded['roaster'].isin([
        'dunkin', 'pavement', 'gracenote', 'george howell', 'barismo', 'render'
    ])])
    print()

    # wouldn't it be easier if we added location info?
    df_expanded = pd.merge(df_expanded, pd.DataFrame({
        'roaster': ['dunkin', 'pavement', 'onyx', 'red rooster'],
        'state': ['MA', 'MA', 'AR', 'VA']
    }))
    print(df_expanded)
    print()

    # note: to get back red rooster, we'd specify a "how" parameter
    # ... but that has consequences b/c we have no associated coffees :(
    print(pd.merge(df, pd.DataFrame({
        'roaster': ['dunkin', 'pavement', 'onyx', 'red rooster'],
        'state': ['MA', 'MA', 'AR', 'VA']
    }), how="outer"))

###############

def main() -> None:
    """getting the app going!"""
    df: pd.DataFrame = data_structure()
    access_data(df)
    manipulate_data(df)

if __name__ == "__main__":
    main()

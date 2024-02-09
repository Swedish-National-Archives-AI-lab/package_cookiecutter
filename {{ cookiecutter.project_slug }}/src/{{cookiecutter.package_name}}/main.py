import pandas as pd
from typing import Dict


def aggregate_mean(df :pd.DataFrame, column:str) -> Dict[str,float]:
    """Computes and returns the mean value of a column

    Args:
        df (DataFrame): A pandas dataframe
        column (str): Column name from the dataframe

    Returns:
        Mean value of each column as a dict.
    """
    return df.groupby("class")[column].mean().to_dict()


if __name__ == "__main__":
    df = pd.DataFrame(
        [[0, 2, 7, 4, 8], [1, 7, 6, 3, 7], [1, 1, "None", 8, 9], [0, 2, 3, "None", 6], [0, 5, 1, 4, 9]],
        columns=[f"feature_{i}" if i != 0 else "class" for i in range(5)],
    )

    mean_dict = aggregate_mean(df)
    print(mean_dict)
import pandas as pd

df_empty = pd.DataFrame({})
df_1c = pd.DataFrame({'a': [1, 2, 3]})
df_dup_column_names1 = pd.concat((pd.DataFrame({'a': [1,2,3]}), pd.DataFrame({'a': ['x', 'y', 'z']})), axis=1)
df_dup_column_names2 = pd.concat((pd.DataFrame({'a': [9,2,3]}), pd.DataFrame({'a': ['x', 'y', 'z']})), axis=1)


def report_differences(df1, df2):
    if df1.equals(df2):
        return

    cols1 = set(df1.columns)
    assert len(cols1) == len(df1.columns), "Assumes no dup columns"
    cols2 = set(df2.columns)
    assert len(cols2) == len(df2.columns), "Assumes no dup columns"
    if cols1 != cols2:
        print("Columns are different!")
        diffs_cols1_to_cols2 = cols1.difference(cols2)
        if len(diffs_cols1_to_cols2):
            print("These columns are only in df1, not df2:", diffs_cols1_to_cols2)
        diffs_cols2_to_cols1 = cols2.difference(cols1)
        if len(diffs_cols2_to_cols1):
            print("These columns are only in df2, not df1:", diffs_cols2_to_cols1)


if __name__ == "__main__":
    print("df_empty, df_empty")
    report_differences(df_empty, df_empty)
    print("----")
    print("df_empty, df_1c2")
    report_differences(df_empty, df_1c)
    print("----")
    print("df_1c2, df_empty")
    report_differences(df_1c, df_empty)


    # check that the duplicate column name checker works
    #print("----")
    #print("df_dup_column_names both")
    #report_differences(df_dup_column_names1, df_dup_column_names2)

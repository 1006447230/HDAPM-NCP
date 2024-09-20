import pandas as pd

ancestors_df = pd.read_csv('DAG2-2_NEW1102.csv', header=None,keep_default_na=False)
s_values_df = pd.read_csv('s_value.csv', header=0)
total_s_values_df = pd.read_csv('total_s.csv', header=0)
ancestors_df.rename(columns={'0':'leaf'},inplace=True)
s_values_df.columns = ['leaf', 'ancestor', 's_value']
total_s_values_df.columns = ['leaf', 'total_s_value']
result_df = pd.DataFrame(columns=['leaf1', 'leaf2', 'result'])
for i in range(len(ancestors_df)):
    for j in range(i+1,len(ancestors_df)):
        common_ancestor = list(set(ancestors_df.iloc[i, 1:]).intersection(set(ancestors_df.iloc[j, 1:])))
        if len(common_ancestor) == 0:
            continue
        sum_s_value = 0
        for ancestor in common_ancestor:
            s_value_i = s_values_df.loc[(s_values_df['leaf'] == ancestors_df.iloc[i, 0]) & (s_values_df['ancestor'] == ancestor), 's_value']
            s_value_j = s_values_df.loc[(s_values_df['leaf'] == ancestors_df.iloc[j, 0]) & (s_values_df['ancestor'] == ancestor), 's_value']
            if not s_value_i.empty:
               sum_s_value += s_value_i.item()
            if not s_value_j.empty:
                sum_s_value += s_value_j.item()
        total_s_value_i = total_s_values_df.loc[(total_s_values_df['leaf'] == ancestors_df.iloc[i, 0]), 'total_s_value']
        total_s_value_j = total_s_values_df.loc[(total_s_values_df['leaf'] == ancestors_df.iloc[j, 0]), 'total_s_value']

        if not total_s_value_i.empty and not total_s_value_j.empty:
            total_s_value = total_s_value_i.item() + total_s_value_j.item()
            result = sum_s_value / total_s_value
            result_df.loc[len(result_df)] = [ancestors_df.iloc[i, 0], ancestors_df.iloc[j, 0], result]



result_df.to_csv('similarity_scores(select).csv', index=False)

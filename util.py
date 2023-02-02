def reduce_mem_usage(df):
    start_mem = df.memory_usage().sum() / 1024**2
    print('Memory usage of dataframe is {:.2f} MB'.format(start_mem))
    
    for col in df.columns:
        col_type = df[col].dtype
        
        if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)  
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
        else:
            pass

    end_mem = df.memory_usage().sum() / 1024**2
    print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
    print('Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))
    
    return df


# ファイルの読み込み
application_train = pd.read_csv("./home-credit-default-risk/application_train.csv")
application_train = reduce_mem_usage(application_train) # メモリ削減
print(f'{application_train.shape[0]:,} x {application_train.shape[1]:,}')
display(application_train.head(3))



print(list(df.select_dtypes(include='number').columns))
print(list(df.select_dtypes(include=np.number).columns))
print(list(df.select_dtypes(exclude='number').columns))
print(list(df.select_dtypes(include='category').columns))
print(df.select_dtypes(include='number').columns.to_list())


import warnings
warnings.filterwarnings('ignore')


# 各特徴量のユニーク値の数
for col in traindf.columns:
	print(col + ":" + str(len(traindf[col].unique())))


# 各特徴量のユニーク値の数
for col in traindf.columns:
	print(col + ":" + str(len(traindf[col].unique())))

df_train.nunique().to_frame()



# 特徴量毎のcountplot

skip_cols = ['ncodpers', 'renta'] # 出力に時間がかかりすぎる2つの変数をskip

for col in df_train.columns:

    if col in skip_cols:
        continue
        
    print('='*50)
    print('col : ', col)
    
    f, ax = plt.subplots(figsize=(25, 5))
    sns.countplot(x=col, data=df_train, alpha=0.5)
    plt.show()



df_corr = df_X.corr()  # 相関係数
# df_corr

plt.figure(figsize=(25, 10))
sns.heatmap(df_corr, vmax=1, vmin=-1, center=0, annot=True, fmt=".2f", cmap='jet')
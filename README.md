
. ~/anaconda3/bin/activate dataframes_alike

## Real problems

### one dataframe has different columns to the other

### series with the same name have different dtypes

### one series has NaNs, the other doesn't

### concat dataframes to add new columns but you didn't update your index

pca = PCA(n_components=2)
transformed = pca.fit_transform(X_train)
transformed.shape, X_train.shape
type(transformed)
df_transformed = pd.DataFrame(transformed,
                              columns=["pca_{}".format(n) for n in range(transformed.shape[1])],
                              index=X_train.index)

X_train_joined = pd.concat((X_train, df_transformed), axis=1)
X_train_joined.head()
note that head will show NaNs if the index wasn't set above as the indices in X_train are different to those in transformed (not sequential starting at 1)

also is axis=0 (default) then the items are appended, so the shapes are different

## Aspirations

* assert `alike` rather than only report differences

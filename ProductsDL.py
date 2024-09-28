import pandas as pd

data_file_name="products.csv"
def add_product(pid,name,description,price,image,rating):
      df=pd.read_csv(data_file_name)
      product=[pid,name,description,price,image,rating]
      last_location=len(df.index)
      df.loc[last_location]=product
      df.to_csv(data_file_name,index=False)
def update_rating(pid,rating):
      df=pd.read_csv(data_file_name)
      condtion=df["pid"]==pid
      idx=df[condtion].index
      df.loc[idx,'rating']=rating
      df.to_csv(data_file_name,index=False)
def delete_product(pid):
     df=pd.read_csv(data_file_name)
     condtion=df["pid"]==pid
     idx=df[condtion].index
     df=df.drop(idx)
     df.to_csv(data_file_name,index=False)
     
def get_all_products():
    df=pd.read_csv(data_file_name)
    return df
def get_product(pid):
    df=pd.read_csv(data_file_name)
    condtion=df["pid"]==pid
    return df [condtion]
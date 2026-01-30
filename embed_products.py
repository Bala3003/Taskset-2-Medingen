import pandas as pd
import json
import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("sampledata/sampledata.csv")

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(df["product_name"]).toarray()

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="demotask"
)

cursor = con.cursor()

for i, row in df.iterrows():
    vector_json = json.dumps(vectors[i].tolist())
    cursor.execute(
        """
        INSERT INTO products_vectors (product_id, product_name, vector)
        VALUES (%s, %s, %s)
        """,
        (int(row["product_id"]), row["product_name"], vector_json)
    )

con.commit()
cursor.close()
con.close()

print("records inserted")

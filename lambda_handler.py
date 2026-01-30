import json
import numpy as np
import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def lambda_handler(event, context):
    query = event.get("query")

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="demotask"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT product_id, product_name, vector FROM products_vectors")
    rows = cursor.fetchall()

    product_vectors = []
    product_names = []

    for r in rows:
        product_names.append(r[1])
        product_vectors.append(json.loads(r[2]))
        
    vectorizer = TfidfVectorizer()
    vectorizer.fit(product_names)

    query_vector = vectorizer.transform([query]).toarray()
    similarities = cosine_similarity(query_vector, product_vectors)[0]

    top_indices = similarities.argsort()[-5:][::-1]

    results = [
        {
            "product_name": product_names[i],
            "score": float(similarities[i])
        }
        for i in top_indices
    ]

    return {
        "statusCode": 200,
        "body": results
    }


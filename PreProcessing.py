from google.cloud import bigquery


def Preprocessing(query):
    
    new_list=[]
    rows=[]
    query_job = client.query(query)
    
    for row1 in query_job:
        rows.append(row1[0])
    
    for index, row in enumerate(rows):
        temp=rows.copy()
        temp.remove(row)
        
        if new_list == [] and row.lower() not in str(temp).lower():
            new_list.append(row)
            continue
            
        if row.lower() in str(temp).lower():
            continue
        else:
            new_list.append(row)
            
    return new_list


if __name__=="__main__":
    
    client = bigquery.Client()
    query = """
    SELECT c  FROM `springer-nature-analytics.DS_dimensions.publications_full_refresh` 
    LEFT JOIN UNNEST(concepts) c
    WHERE doi = '10.1038/nature14539'"""
    
    New_list=Preprocessing(query)
    print(New_list)
    
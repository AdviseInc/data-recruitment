def transaction_count(con):
    
    query =  """
        select count(*) from NHS.EXPENDITURE
        """
    
    cur = con.cursor()
    cur.execute(query)
    r = cur.fetchone()[0]

    with open('transaction_count.csv', 'w') as f:
        f.write(f'{r}')


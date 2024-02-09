def get_table_data(table):
    data = []
    for child in table.get_children():
        data.append(table.item(child)['values'])
    return data

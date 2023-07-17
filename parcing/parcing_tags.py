def update_labels(client, form):
    n190_195_list = client.read_integer(file_table=29, start=0, total_int=6)
    n190_195_array = list(map(int, n190_195_list))

    form.label_67.setText(str(n190_195_array[0]/10))
    form.label_68.setText(str(n190_195_array[1]/10))
    form.label_69.setText(str(n190_195_array[2]/10))
    form.label_72.setText(str(n190_195_array[3]/10))
    form.label_70.setText(str(n190_195_array[4]/10))
    form.label_71.setText(str(n190_195_array[5]/10))
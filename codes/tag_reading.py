def update_label_67_72(client, form):
    n190_195_list = client.read_integer(file_table=29, start=190, total_int=6)
    n190_195_array = list(map(int, n190_195_list))

    form.label_67.setText(str(n190_195_array[0]/10))

# def update_label_67(client, form):
#     form.label_67.setText(str(int(client.read_integer(file_table=29, start=190, total_int=1)[0])/10))

def update_label_68(client, form):
    form.label_68.setText(str(client.read_integer(file_table=29, start=191, total_int=1)[0]))

def update_label_69(client, form):
    form.label_69.setText(str(client.read_integer(file_table=29, start=192, total_int=1)[0]))

def update_label_72(client, form):
    form.label_72.setText(str(client.read_integer(file_table=29, start=193, total_int=1)[0]))

def update_label_70(client, form):
    form.label_70.setText(str(client.read_integer(file_table=29, start=194, total_int=1)[0]))

def update_label_71(client, form):
    form.label_71.setText(str(client.read_integer(file_table=29, start=195, total_int=1)[0]))
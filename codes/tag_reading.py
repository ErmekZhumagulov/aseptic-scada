def update_label_407(client, form):
    form.label_407.setText(str(client.read_integer(start=1, total_int=1)[0]))

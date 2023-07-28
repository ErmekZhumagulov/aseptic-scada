def update_labels(client, form):
    try:
        client.wait_no_pending_command()
        n190_195_list = client.read_integer(file_table=29, start=190, total_int=6)
        n190_195_array = list(map(int, n190_195_list))
        module141_c = n190_195_array[0]/10
        module141_m3 = n190_195_array[1]/100
        module141_ms = n190_195_array[2]/10
        module142_c = n190_195_array[3]/10
        module142_m3 = n190_195_array[4]/100
        module142_ms = n190_195_array[5]/10
        module141_tc1_2 = client.read_integer(file_table=29, start=160, total_int=1)
        module141_tc1_2_int = int(module141_tc1_2[0])/10

        form.label_67.setText(str(module141_c))
        form.label_68.setText(str(module141_m3))
        form.label_69.setText(str(module141_ms))
        form.label_72.setText(str(module142_c))
        form.label_70.setText(str(module142_m3))
        form.label_71.setText(str(module142_ms))

        form.label_85.setText(str(module141_m3))
        form.label_86.setText(str(module141_ms))
        form.label_87.setText(str(module141_c))

        form.label_380.setText(str(module142_m3))
        form.label_374.setText(str(module142_ms))
        form.label_368.setText(str(module142_c))

        form.label_412.setText(str(module141_ms))
        form.label_418.setText(str(module141_c))
        form.label_425.setText(str(module141_m3))
        form.label_431.setText(str(module141_tc1_2_int))

        form.label_479.setText(str(module142_ms))
        form.label_492.setText(str(module142_c))
        form.label_495.setText(str(module142_m3))
        form.label_522.setText(str(module141_tc1_2_int))
    except Exception as e:
        print ("[WARNING] An error occurred while reading PLC data")
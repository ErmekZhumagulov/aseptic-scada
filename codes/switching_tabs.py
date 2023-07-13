def switch_logic(form):
    def on_pushButton_clicked_2():
        # Custom slot implementation
        form.tabWidget.setCurrentIndex(2)
    form.pushButton_2.clicked.connect(on_pushButton_clicked_2)

    def on_pushButton_clicked_3():
        # Custom slot implementation
        form.tabWidget.setCurrentIndex(3)
    form.pushButton_3.clicked.connect(on_pushButton_clicked_3)

    def on_pushButton_clicked_4():
        # Custom slot implementation
        form.tabWidget.setCurrentIndex(4)
    form.pushButton_4.clicked.connect(on_pushButton_clicked_4)

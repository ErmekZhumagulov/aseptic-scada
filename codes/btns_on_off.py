#set texts to labels
def update_labels(labels):
    for label in labels:
        random_number = random.uniform(0.00, 100.00)
        random_string = "{:.2f}".format(random_number)
        label.setText(random_string)

#-----------------------------------------------------------------------------------------------------------------------

# switch light randomizer
def generate_random_number():
    array = [
        form.pushButton_25, form.pushButton_26, form.pushButton_27, form.pushButton_28, form.pushButton_29,
        form.pushButton_30, form.pushButton_31, form.pushButton_32, form.pushButton_33, form.pushButton_34,
        form.pushButton_35, form.pushButton_36, form.pushButton_37, form.pushButton_38, form.pushButton_39,
        form.pushButton_40, form.pushButton_41, form.pushButton_42, form.pushButton_43, form.pushButton_44,
        form.pushButton_45, form.pushButton_46, form.pushButton_47, form.pushButton_48, form.pushButton_49,
        form.pushButton_50, form.pushButton_51, form.pushButton_52, form.pushButton_53, form.pushButton_54,
        form.pushButton_55, form.pushButton_56
    ]
    for button in array:
        random_number = random.randint(0, 1)
        value = random_number
        button.setProperty("value", value)
        button.style().polish(button)

        # Apply the style sheet to change the background color based on the value
        button.setStyleSheet('''
            QPushButton {
                /* Default background color */
                background-color: red; /* or any other default color */
                border: 1px solid black
            }
            QPushButton[value="0"] {
                /* Background color when value is 0 */
                background-color: #d6d6d6;
                border: 1px solid black
            }
            QPushButton[value="1"] {
                /* Background color when value is 1 */
                background-color: green;
                border: 1px solid black
            }
        ''')

# Create a QTimer to trigger the generation of random numbers every 2 seconds
timer = QTimer()
timer.timeout.connect(generate_random_number)
# Connect the timeout signal of the timer to a lambda function that calls update_labels with the array of labels
timer.timeout.connect(lambda: update_labels([form.label_368,form.label_374, form.label_380, form.label_85, form.label_86, form.label_87, form.label_67, form.label_68, form.label_69, form.label_70, form.label_71, form.label_72]))
timer.start(1000)
class LabelToggler:
    def __init__(self, labels):
        self.labels = labels

    def toggle_label_visibility(self):
        for label in self.labels:
            label.setVisible(not label.isVisible())
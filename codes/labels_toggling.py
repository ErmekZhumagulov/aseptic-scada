def switch_logic(form):
    def toggle_label_visibility():
        labels = [
            form.label_249, form.label_250, form.label_243, form.label_242, form.label_240, form.label_241,
            form.label_244, form.label_245, form.label_271, form.label_272, form.label_273, form.label_274,
            form.label_301, form.label_262, form.label_263, form.label_265, form.label_266, form.label_267,
            form.label_270, form.label_276, form.label_277, form.label_278, form.label_279, form.label_291,
            form.label_292, form.label_294, form.label_295, form.label_275, form.label_289, form.label_290,
            form.label_280, form.label_285, form.label_286, form.label_288, form.label_287, form.label_281,
            form.label_282, form.label_283, form.label_284, form.label_300, form.label_297, form.label_298,
            form.label_310, form.label_299, form.label_304, form.label_309, form.label_305, form.label_306,
            form.label_311, form.label_320, form.label_318, form.label_317, form.label_322, form.label_321,
            form.label_315, form.label_324, form.label_323, form.label_319
        ]

        for label in labels:
            label.setVisible(not label.isVisible())

    form.pushButton.clicked.connect(toggle_label_visibility)

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza(self, e):
        distanza = self._view.txt_distanza.value
        try:
            float(distanza)
        except ValueError:
            self._view.create_alert("Inserisci solo valori numerici.")
            self._view.update_page()
            return
        self._model.buildGraph(float(distanza))
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo creato!"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {self._model.getNumNodes()}."))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {self._model.getNumEdges()}."))
        dettagli = self._model.getDettagli()
        for d in dettagli:
            self._view.txt_result.controls.append(ft.Text(d))
        self._view.update_page()

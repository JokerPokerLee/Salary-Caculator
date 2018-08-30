from Model import Model
from View import View
from Controller import Controller

if __name__ == '__main__':
    model = Model()
    view = View()
    controller = Controller()
    model.register_view(view)
    view.register_model(model)
    view.register_controller(controller)
    controller.register_model(model)
    controller.register_view(view)
    view.build_ui()
    view.main_loop()
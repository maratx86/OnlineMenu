class BaseView:

    def __init__(self, title):
        self.title = title
        self.img = None
        self.__text_buttons = []

    def add_button(self, text, onclick):
        self.__text_buttons.append({
            'text': text, 'onclick': onclick,
        })

    @property
    def text_buttons(self):
        return self.__text_buttons


class RestaurantView(BaseView):
    def __init__(self, *args, **kwargs):
        super().__init__(None, *args, **kwargs)


class RestaurantMenuView(BaseView):
    def __init__(self, title, *args, **kwargs):
        super().__init__(title, *args, **kwargs)


class RestaurantMenuPositionView(BaseView):
    def __init__(self, title, pm, *args, **kwargs):
        super().__init__(title, *args, **kwargs)
        self.position_menu = pm

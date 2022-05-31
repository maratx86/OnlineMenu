from flask import url_for

import app.storage.database.models


class SectionResult:
    def __init__(self, obj):
        self.__obj = obj
        self.title = obj.title
        if isinstance(obj, app.storage.database.models.Restaurant):
            self.link = url_for('r.index', restaurant_id=obj.id)
        elif isinstance(obj, app.storage.database.models.Position):
            self.link = url_for('r.position', restaurant_id=obj.restaurant_id, position_id=obj.id)
        elif isinstance(obj, app.storage.database.models.Menu):
            self.link = url_for('r.menu', restaurant_id=obj.restaurant_id, menu_id=obj.id)
        else:
            self.link = '/be/'
        pass


class SectionResults:
    def __init__(self, objs):
        self.__objs = objs
        pass

    def __next__(self):
        for obj in self.__objs:
            yield SectionResult(obj)

    def __iter__(self):
        for i in range(len(self.__objs)):
            yield SectionResult(self.__objs[i])


class QuerySection:
    def __init__(self, title, count, objs):
        self.title = title
        self.count = count
        self.__objs = objs
        self.__results = SectionResults(objs)

    @property
    def results(self):
        return self.__results


class QueryResults:
    def __init__(self, *args, **argv):
        self.__text = args[0] if len(args) else None
        self.__sections = []
        self.__has_any_result = False
        pass

    def add_section(self, title, count, objs):
        if objs:
            self.__sections.append(QuerySection(title, count, objs))
            self.__has_any_result = True

    @property
    def sections(self):
        return self.__sections

    @property
    def text(self):
        return self.__text

    @text.setter
    def text_setter(self, text):
        if self.__text:
            raise AssertionError('You cannot change text')
        self.__text = text

    @property
    def has_results(self):
        return self.__has_any_result

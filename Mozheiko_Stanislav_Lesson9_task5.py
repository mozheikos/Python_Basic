class Stationery:
    message = 'Запуск отрисовки'

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(self.message)


class Pen(Stationery):
    message = 'взяли ручку и пишем'


class Pencil(Stationery):
    message = 'карандаш. карандашом чертим'


class Handle(Stationery):
    message = 'маркером разрисовываем лицо спящей жены'


pen = Pen('ручка')
pencil = Pencil('карандаш')
marker = Handle('маркер')

pen.draw()
pencil.draw()
marker.draw()

import sys
import interface
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QStandardItemModel, QStandardItem
from PyQt5.QtGui import QFont, QColor, QIcon, QPainter
from PyQt5.QtChart import QChart, QPieSeries


class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):  #(32, 56, 100)):
        super().__init__()

        fnt = QFont('DengXian', font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)


class AppDemo(QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
# разбираюсь с деревом
        self.categories_txt.setHeaderHidden(True)

        self.treeModel = QStandardItemModel()
        self.rootNode = self.treeModel.invisibleRootItem()
        self.categories_txt.setModel(self.treeModel)
        self.categories_txt.doubleClicked.connect(self.category_changed)

        self.current_demand = 'is not null'
        self.current_category = 'is not null'
        self.set_demands()
        self.set_categories()
# разбираюсь с таблицей похожих дел
        self.listModel = QStandardItemModel()
        self.similar_case_txt.setModel(self.listModel)
        self.similar_case_txt.doubleClicked.connect(self.open_doc)
# разбираюсь с анализом
        self.analys_txt_model = QStandardItemModel()
        self.analys_txt.setModel(self.analys_txt_model)
        self.analys_txt.setFont(QFont("DengXian", 11))
#разбираюсь с графой требований
        self.requires_box.addItems(self.demands)
        self.requires_box.currentTextChanged.connect(self.demand_changed)
        self.requires_box.setView(self.requires_drop_down)

    def category_changed(self, val):
        if val.data() == 'Не выбрано':
            self.current_category = 'is not null'
        else:
            self.current_category = "= '" + val.data() + "'"

        self.set_demands()
        self.get_data()

    def demand_changed(self, val):
        if val == 'Не выбрано':
            self.current_demand = 'is not null'
        else:
            self.current_demand = "= '" + val + "'"

        self.set_categories()
        self.get_data()

    def get_data(self):
        global q
        self.listModel.clear()
        self.listModel.setColumnCount(3)
        self.listModel.setHorizontalHeaderLabels(['Номер дела', 'Инстанции', 'Решение'])
        self.similar_case_txt.horizontalHeader().resizeSection(0, 800)
        self.similar_case_txt.horizontalHeader().resizeSection(1, 100)
        self.similar_case_txt.horizontalHeader().resizeSection(2, 85)

        check_demands = 'and demand ' + self.current_demand

        q.exec(f'''select number, solution, count_inst from smalltable
                   where (category1 {self.current_category}
                   or category2 {self.current_category}) ''' + check_demands + ';')

        while q.next():
            decision_icon = QStandardItem()
            if q.value(1) == "Удовлетворено":
                decision_icon = QStandardItem(QIcon("icons/judgment_icon_violet"), '')
            elif q.value(1) == "Не удовлетворено":
                decision_icon = QStandardItem(QIcon("icons/judgment_icon_orange"), '')
            elif q.value(1) == "Частично удовлетворено":
                decision_icon = QStandardItem(QIcon("icons/judgment_icon_yellow"), '')

            # print(q.value(2), type(q.value(2)))
            if q.value(2) == 1:
                count_inst_icon = QStandardItem(QIcon("icons/dots_1"), '')
            elif q.value(2) == 2:
                count_inst_icon = QStandardItem(QIcon("icons/dots_2"), '')
            elif q.value(2) == 3:
                count_inst_icon = QStandardItem(QIcon("icons/dots_3"), '')
            elif q.value(2) == 4:
                count_inst_icon = QStandardItem(QIcon("icons/dots_4"), '')
            elif q.value(2) == 5:
                count_inst_icon = QStandardItem(QIcon("icons/dots5"), '')

            self.listModel.appendRow([StandardItem(q.value(0), 12),
                                      count_inst_icon,
                                      decision_icon])

        q.exec(f'''select count(number) from smalltable where (category1 {self.current_category}
                           or category2 {self.current_category}) ''' + check_demands + ';')

        if q.next():
            self.analys_sum.setFont(QFont("DengXian", 10))
            self.analys_sum.setText(f"В категории: {self.current_category}\n\n"
                                    f"По требованию: {self.current_demand}\n\n"
                                    f"Найдено дел: {q.value(0)}")

        q.exec(f'''select count(number) from smalltable
                           where (category1 {self.current_category} or category2 {self.current_category})
                           and solution = 'Удовлетворено' ''' + check_demands + ';')

        counters = []
        if q.next():
            counters.append(q.value(0))

        q.exec(f'''select count(number) from smalltable
                           where (category1 {self.current_category} or category2 {self.current_category})
                           and solution = 'Не удовлетворено' ''' + check_demands + ';')

        if q.next():
            counters.append(q.value(0))

        q.exec(f'''select count(number) from smalltable
                           where (category1 {self.current_category} or category2 {self.current_category})
                           and solution = 'Частично удовлетворено' ''' + check_demands + ';')

        if q.next():
            counters.append(q.value(0))

        series = QPieSeries()
        series.setHoleSize(0.4)

        statistic = [(f"Удовлетворено: {counters[0]}", counters[0]),
                     (f"Не удовлетворено: {counters[1]}", counters[1]),
                     (f"Частично удовлетворено: {counters[2]}", counters[2])]

        icons = ['icons/violet_icon', 'icons/orange_icon', 'icons/yellow_icon']
        colors = [QColor(90, 69, 165), QColor(197, 90, 17), QColor(255, 217, 102)]
        self.analys_txt_model.clear()
        self.analys_txt_model.appendRow(StandardItem("Из них:\n", 10))
        for i in range(len(statistic)):
            row = QStandardItem(QIcon(icons[i]), statistic[i][0])
            row.setFont(QFont("DengXian", 10))
            self.analys_txt_model.appendRow(row)
            a = series.append(statistic[i][0], statistic[i][1])
            a.setBrush(colors[i])

        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.AllAnimations)

        chart.legend().setVisible(False)

        self.analys_pic.setChart(chart)
        self.analys_pic.setRenderHint(QPainter.Antialiasing)

    def open_doc(self, val):
        global q
        q.exec(f'''select acts from smalltable where "number" = '{val.data()}';''')

        text = ''
        while q.next():
            text = q.value(0)
        self.w = interface.AnotherWindow(text)
        self.w.setWindowTitle(val.data())
        self.w.show()

    def set_demands(self):
        global q
        q.exec(f"select distinct demand from smalltable where category1 {self.current_category} "
               f"or category2 {self.current_category};")
        self.demands = ['Не выбрано']
        while q.next():
            self.demands.append(q.value(0))
        self.requires_box.clear()
        self.requires_box.addItems(self.demands)

    def set_categories(self):
        global q
        q.exec(f"select c_name from categories "
               f"order by c_id;")
        categories = []

        while q.next():
            categories.append(q.value(0))

        zero_level = []
        for i in categories:
            zero_level.append(StandardItem(i, 14, set_bold=True))

        first_level = self.set_subcategories(2)
        first_level_ = self.set_subcategories(3)

        for i in first_level:
            zero_level[1].appendRow(i)
        for i in first_level_:
            zero_level[2].appendRow(i)
        for i in zero_level:
            self.rootNode.appendRow(i)

        self.categories_txt.expandAll()

    def set_subcategories(self, parent_category):
        global q
        self.rootNode.removeRows(0, self.rootNode.rowCount())

        q.exec(f"select distinct category2 from smalltable "
               f"where demand {self.current_demand} "
               f"and cat1_id = {parent_category};")

        level = []
        while q.next():
            level.append(StandardItem(q.value(0), 12, set_bold=True))

        return level  # возвращает список StandardItem

    def set_subcategories1(self, parent_category):
        global q

        q.exec(f"select distinct category2 from smalltable "
               f"where demand {self.current_demand} "
               f"and cat1_id = {parent_category};")

        level = []
        while q.next():
            level.append(q.value(0))
        return level


if __name__ == '__main__':
    db = QSqlDatabase("QPSQL")
    db.setHostName("localhost")
    db.setDatabaseName("test_data")
    db.setUserName("postgres")
    db.setPassword("513230")

    print(db.open(), db.lastError().text())

    q = QSqlQuery(db)

    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()

    sys.exit(app.exec_())

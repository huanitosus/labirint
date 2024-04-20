from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QPushButton, QApplication, QWidget, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QGroupBox
from random import shuffle, randint

class Question():
    def __init__(self, quesstion, right_answer, wrong1, wrong2, wrong3):
        self.quesstion = quesstion
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Кто сделал майнкрафт?', 'Маркус Персон', 'Стив Джемс', 'Михалыч со второго падика', 'Илон Маск'))
question_list.append(Question('В каком году состаялся релиз майнкрафта?', '2011', '2077', '2009', '7/8'))
question_list.append(Question('Как называлась самая ранняя, сохранившаяся версия майнкрафта?', 'rd - 132211', 'rd - 695678', 'dr - 222111', 'rd - 161338'))
question_list.append(Question('На какой версии kriper2004 снял свой знаминитый ролик длинельностью - 94:31:57?', 'alfa - 1.2.6', 'alfa - 1.2.7/8', 'alba 1.2.3.4.5', 'rd alfa bata 33333333333333333'))
question_list.append(Question('Можно ли поджечь костёр книгой на заговор огня?', 'да', 'нет', 'ты идиот?', 'ты идиот...'))
question_list.append(Question('Можно ли затушить костёр снежком?', 'да', 'нет', 'откуда мне знать?', 'тен'))
question_list.append(Question('Получает ли игрок урон от снежка?', 'нет', 'да', 'да', 'тен'))
question_list.append(Question('Правда ли, что при попадании молнии в черепаху, та превратится в деревянную миску?', 'да', 'нет', 'нет', 'app = QApplication([])'))
question_list.append(Question('Можно ли одуванчиками размножать кроликов?', 'да', 'нет', 'нет', 'нетнетнетнетнетнетнетнетнетнетнетнет'))
question_list.append(Question('Можно ли получть слизь в панды?', 'да', 'нет', 'нет', 'нет'))

app = QApplication([])
main_win = QWidget()
main_win.resize(700, 500)
main_win.setWindowTitle('wocfvsa')

bt_jk = QPushButton('Ответить')
qw = QLabel('Какой национальности не существует?')

RadioGroupBox = QGroupBox('варианты ответов')

rbt1 = QRadioButton('энцы')
rbt2 = QRadioButton('Смурфы')
rbt3 = QRadioButton('чумышцы')
rbt4 = QRadioButton('алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbt1)
RadioGroup.addButton(rbt2)
RadioGroup.addButton(rbt3)
RadioGroup.addButton(rbt4)

layout_ans1 = QVBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans2.addWidget(rbt1)
layout_ans2.addWidget(rbt2)
layout_ans3.addWidget(rbt3)
layout_ans3.addWidget(rbt4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Рзультаты теста')
lp_result = QLabel('прав ты или неоч')
lp_correct= QLabel('ответ')
layout_ans4= QVBoxLayout()
layout_ans4.addWidget(lp_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_ans4.addWidget(lp_correct, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(layout_ans4)
AnsGroupBox.hide()

layout_line = QVBoxLayout()
layout_line.addWidget(qw, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line.addWidget(RadioGroupBox)
layout_line.addWidget(AnsGroupBox)
layout_line.addWidget(bt_jk, stretch=2)
main_win.setLayout(layout_line)

def Show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    bt_jk.setText('Продолжить')

def Show_qastion():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    bt_jk.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbt1.setChecked(False)
    rbt2.setChecked(False)
    rbt3.setChecked(False)
    rbt4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbt1, rbt2, rbt3, rbt4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    qw.setText(q.quesstion)
    lp_correct.setText(q.right_answer)
    Show_qastion()

def show_correct(res):
    lp_result.setText(res)
    Show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('правильно')
        main_win.score += 1
        print('Статистика\п Всего вопросов - ', main_win.total, '\п Количество правильных ответов', main_win.score)
        print('Рейтинг: ', main_win.score/main_win.total*100,'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('неверно')
            print('Рейтинг: ', main_win.score/main_win.total*100,'%')

def next_quesstion():
    main_win. total += 1
    print('Статистика\п Всего вопросов - ', main_win.total, '\п Количество правильных ответов', main_win.score)
    nu_ok = randint(0,len(question_list) - 1)
    q = question_list[nu_ok]
    ask(q)




def click_jk():
    if bt_jk.text() == 'Ответить':
        check_answer()
    else:
        next_quesstion()

main_win.total = 0
main_win.score = 0
main_win.nu_ok = -1
bt_jk.clicked.connect(click_jk)
next_quesstion()




main_win.show()
app.exec_()
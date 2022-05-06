#создай приложение для запоминания информации
#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint, shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list =[]
questions_list.append(Question('Сколько длилась столетняя война', "116", "45", "100", "963"))
questions_list.append(Question('сколько длилась война белой и красной розы', "30", "60", "10", "1"))
questions_list.append(Question('сколько длилась северная война', "21", "5", "32", "7"))
questions_list.append(Question('сколько длилась вторая мировая война', "6", "5", "3", "7"))
questions_list.append(Question('Когда крестили Русь?', "в 988", "в 102", "в 300", "в 700"))
questions_list.append(Question('Когда создали глаголицу', "в 863", "в 505", "в 396", "в 785"))
questions_list.append(Question('Кто создал глаголицу?', "Киррилл и Мефодий", "Мефодий", "Киррилл", "я не знаю:("))
questions_list.append(Question('Кто крестил Русь?', "Владимир Мономах", "Кирилл", "кто-то", "я не знаю:("))


#создание приложения и главного окна
app = QApplication([])
window = QWidget()
window.resize(400,200)
window.setWindowTitle("Memory Card:з")


#создание виджетов главного окна
label1 = QLabel("Сколько длилась столетняя война?") 
RGB = QGroupBox('Варианты ответов:')
rbtn1 = QRadioButton('100')
rbtn2 = QRadioButton('45')
rbtn3 = QRadioButton('116')
rbtn4 = QRadioButton('963')
button = QPushButton("Ответить")
#расположение виджетов по лэйаутам
line1 = QHBoxLayout()
line2 = QVBoxLayout()
line3 = QVBoxLayout()
line1.addWidget(label1, alignment=Qt.AlignCenter)
line2.addWidget(rbtn1, alignment=Qt.AlignCenter)
line2.addWidget(rbtn2, alignment=Qt.AlignCenter)
line3.addWidget(rbtn3, alignment=Qt.AlignCenter)
line3.addWidget(rbtn4, alignment=Qt.AlignCenter)

line1.addLayout(line2)
line1.addLayout(line3)
RGB.setLayout(line1)
#line1.addWidget(button)
#ппанель с результатом ответа
AnsGB = QGroupBox('Результат теста')
result = QLabel('Прав ты или нет?')
correct = QLabel('Ответ будет тут')
Layout_res = QVBoxLayout()
Layout_res.addWidget(result, alignment=(Qt.AlignLeft | Qt.AlignTop))
Layout_res.addWidget(correct,alignment= Qt.AlignHCenter, stretch=2)
AnsGB.setLayout(Layout_res)

#обработка нажатий на переключатели
H1 =QHBoxLayout()
H2 =QHBoxLayout()
H3 =QHBoxLayout()
H1.addWidget(label1)
H2.addWidget(RGB)
H2.addWidget(AnsGB)
AnsGB.hide()
H3.addWidget(button)
general_line = QVBoxLayout()
general_line.addLayout(H1)
general_line.addLayout(H2)
general_line.addLayout(H3)
window.setLayout(general_line)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

window_end = QMessageBox()

#Обработка нажатия на кнопку "Ответить"
def end():
    window_end.setText('Вопросы на сегодня закончились! \nБлагодарим за участие')
    window_end.exec_()
def show_result():
    RGB.hide()
    AnsGB.show()
    button.setText("Следующий вопрос")

def show_question():
    RGB.show()
    AnsGB.hide()
    button.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

answers =[rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    label1.setText(q.question)
    correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    result.setText(res)
    show_result()
def chek_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')
def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
    if len(questions_list)>0:
        cur_question = randint(0,len(questions_list)-1)
        q = questions_list[cur_question]
        ask(q)
        questions_list.remove(q)
    else:
        end()
        

    

#отображение окна приложения 
def click_Ok():
    if button.text()=='Ответить':
        chek_answer()
    else:
        next_question()

button.clicked.connect(click_Ok)
window.score = 0
window.total = 0
next_question()





window.show()
app.exec_()
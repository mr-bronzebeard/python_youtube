# -*- coding: utf8 -*-
import sys
from urllib import request

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

import api_youtube as api
from my_app_gui import Ui_MainWindow


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # noinspection PyCallByClass
        reply = QMessageBox.question(self, "Подтвердите действие", "Требуется авторизация. Вы согласны продолжить "
                                                                   "работу?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.initUI()
        else:
            sys.exit(0)

    def initUI(self):
        # получаем токен авторизации
        api.get_token_json()

        # получаем информацию о своём канале
        channel = api.my_channel()

        # загрухка аватарки
        data = request.urlopen(channel['snippet']['thumbnails']['medium']['url']).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        self.ui.label_avatar.setPixmap(pixmap)

        # загрузка имение
        snippet = channel['snippet']
        self.ui.label_name.setText(snippet['title'])

        # загрузка логина
        id_channel = channel['id']
        login_str = '''<a href="https://www.youtube.com/channel/''' \
                    + id_channel + '''">''' \
                    + snippet['customUrl'] \
                    + '''</a> '''
        self.ui.label_login.setOpenExternalLinks(True)
        self.ui.label_login.setText(login_str)

        # загрузка статистики
        statistic = channel['statistics']
        self.ui.textBrowser_statistic.append("Просмотров на Вашем канале: " + statistic['viewCount'] + ".")
        self.ui.textBrowser_statistic.append("Комментариев на Вашем канале: " + statistic['commentCount'] + '.')
        self.ui.textBrowser_statistic.append("На Вашем канале " + statistic['subscriberCount'] + " подписчиков(-а).")
        self.ui.textBrowser_statistic.append("На Вашем канале загружено " + statistic['videoCount'] + " видеозаписи.")

        # очищаем список результатов и строку для поиска
        self.ui.pushButton_clear.clicked.connect(self.clear_widget)

        # активируем поиск
        self.ui.pushButton_search.clicked.connect(self.run_search)

        self.ui.textBrowser_test_search_result.setOpenExternalLinks(True)

        # self.web = QWebEngineView(self.ui.verticalLayoutWidget_2)
        # self.web.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        # self.ui.verticalLayout_2.addWidget(self.web)


    def clear_widget(self):
        self.ui.lineEdit_search.clear()
        self.ui.textBrowser_test_search_result.clear()
        self.ui.lineEdit_search.setPlaceholderText("Введите запрос для поиска")
        self.ui.textBrowser_test_search_result.setPlaceholderText("Здесь будут результаты поиска")

    def run_search(self):

        self.ui.textBrowser_test_search_result.setText("")

        options = self.ui.lineEdit_search.text()
        response = api.search(options)

        videos = []

        for search_result in response.get('items', []):
            if search_result['id']['kind'] == 'youtube#channel':
                self.ui.textBrowser_test_search_result.append("Канал(-ы):\tId:\t" + search_result['id']['channelId'])
                self.ui.textBrowser_test_search_result.append(
                    "\tНазвание канала:\t" + search_result['snippet']['title'])
                self.ui.textBrowser_test_search_result.append(
                    "\tОписание канала:\t" + search_result['snippet']['description'])
                self.ui.textBrowser_test_search_result.append(
                    '<a href="https://www.youtube.com/channel/' + search_result['id'][
                        'channelId'] + '">Перейти на калан (откроется в браузере)</a>')
                self.ui.textBrowser_test_search_result.append("")
            elif search_result['id']['kind'] == 'youtube#video':
                response_rating = api.get_rating_by_group_id_videos(search_result['id']['videoId'])
                res = response_rating['items'][0]['statistics']
                self.ui.textBrowser_test_search_result.append("Видео:\tId:\t" + search_result['id']['videoId'])
                self.ui.textBrowser_test_search_result.append("\tНазвание видео:\t" + search_result['snippet']['title'])
                self.ui.textBrowser_test_search_result.append(
                    "\tОписание видео:\t" + search_result['snippet']['description'])
                self.ui.textBrowser_test_search_result.append(
                    "\tПросмотров: " + res['viewCount'] + ". Лайков: " + res[
                        'likeCount'] + ". Дизлайков: " + res['dislikeCount'] + ".")
                self.ui.textBrowser_test_search_result.append(
                    '<a href="https://www.youtube.com/watch?v=' + search_result['id'][
                        'videoId'] + '">Просмотреть видео (откроется в браузере)</a>')
                self.ui.textBrowser_test_search_result.append("")
                videos.append(response_rating['items'][0]['player']['embedHtml'])
                # self.ui.textBrowser_test.append(response_rating['items'][0]['player']['embedHtml'])
                # print("DEBUG", response_rating['items'][0]['player']['embedHtml'])

        # print("DEBUG videos: ", videos)
        # html = []
        # html = """<!DOCTYPE html><html><head><meta charset="utf-8"></head><body>"""
        # for v in videos:
        #     html += """<div>""" + v + """</div>"""
        # html += '''<div>''' + videos[0] + '''</div>'''
        # html += """</body></html>"""

        # html = "<div>" + videos[0] + "</div>"

        # baseUrl = "local"
        # self.web.setHtml(html, QUrl(baseUrl))
        # print("DEBUG!!!", html)
        # for v in videos:
        #     self.ui.textBrowser_test.setHtml(v)
        #     print("DEBUG v: ", v)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())

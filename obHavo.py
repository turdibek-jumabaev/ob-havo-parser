from re import I
import requests
from bs4 import BeautifulSoup as bs


class Weather:
    def __init__(self, city):
        self.city = city
        self.url = f'https://sinoptik.ua/погода-{city}'
        self.t = requests.get(self.url)
        self.html_t = bs(self.t.content, 'html.parser')

    def get_weather(self):
        for el in self.html_t.select("#content"):
            min = el.select(".temperature .min")[0].text
            max = el.select(".temperature .max")[0].text
            t_min = min[4:]
            t_max = max[5:]
            print(f'Температура в {self.city} от {t_min} до {t_max}')

    def today(self, day: bool = False, month: bool = False, min_temp: bool = False, max_temp: bool = False, date: bool = False):
        if max_temp:
            for el in self.html_t.select("#content"):
                max = el.select(".temperature .max")[0].text
                t_max = max[5:]
                return t_max

        if min_temp:
            for el in self.html_t.select("#content"):
                min = el.select(".temperature .min")[0].text
                t_min = min[4:]
                return t_min

        if month:
            for el in self.html_t.select("#content"):
                month = el.select(".month")[0].text
                return month

        if day:
            for el in self.html_t.select("#content"):
                day = el.select(".day-link")[0].text
                return day

        if date:
            for el in self.html_t.select("#content"):
                date = el.select(".date")[0].text
                return date

        else:
            for el in self.html_t.select("#content"):
                day = el.select(".day-link")[0].text
                month = el.select(".month")[0].text
                date = el.select(".date")[0].text
                min = el.select(".temperature .min")[0].text
                max = el.select(".temperature .max")[0].text
                t_min = min[4:]
                t_max = max[5:]
                return f'Сегодня, во {day}, {date} {month}, в {self.city} температура воздуха составит от {t_min} до {t_max}.'

    def tomorrow(self, day: bool = False, month: bool = False, min_temp: bool = False, max_temp: bool = False, date: bool = False):
        result = dict()
        if day:
            for el in self.html_t.select("#content"):
                day = el.select(".day-link")[1].text
                result['day'] = day

        if month:
            for el in self.html_t.select("#content"):
                month = el.select(".month")[1].text
                result['month'] = month

        if date:
            for el in self.html_t.select("#content"):
                date = el.select(".date")[1].text
                result['date'] = date

        if min_temp:
            for el in self.html_t.select("#content"):
                min = el.select(".temperature .min")[1].text
                t_min = min[4:]
                result['min'] = t_min

        if max_temp:
            for el in self.html_t.select("#content"):
                max = el.select(".temperature .max")[1].text
                t_max = max[5:]
                result['max'] = t_max

        else:
            for el in self.html_t.select("#content"):
                day = el.select(".day-link")[1].text
                month = el.select(".month")[1].text
                date = el.select(".date")[1].text
                min = el.select(".temperature .min")[1].text
                max = el.select(".temperature .max")[1].text
                t_min = min[4:]
                t_max = max[5:]
                return f'Завтра, во {day}, {date} {month}, в {self.city} температура воздуха составит от {t_min} до {t_max}.'

        return result


ac = Weather('ташкент')
print(ac.tomorrow(min_temp=True, max_temp=True))

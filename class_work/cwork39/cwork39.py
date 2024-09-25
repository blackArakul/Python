# from jinja2 import Template
#
# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Renault', 'price': 44300},
#     {'model': 'Wolksvagen', 'price': 21300}
# ]
#

# tp1 = "{{ (cs | min(attribute='price')).model }}"
# tp1 = "{{ cs | random }}"  #
# tp1 = "{{ cs | replace('model', 'brand') }}"  # Смена ключа
# tm = Template(tp1)
# msg = tm.render(cs=cars)
#
# print(msg)


#
# macro определение (функция в шаблонизаторе)


# html = '''
# {% macro get_input(name, value='', type='text', size=20) %}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value }}" size="{{ size }}">
# {% endmacro %}
#
# <p>{{ get_input('username') }}</p>
# <p>{{ get_input('email') }}</p>
# <p>{{ get_input('password', type='passwrod') }}</p>
# '''
#
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)


#


from jinja2 import Environment, FileSystemLoader


# persons = [
#     {"name": "Алексей", "year": 18, "weight": 78.5},
#     {"name": "Никита", "year": 28, "weight": 82.3},
#     {"name": "", "year": 33, "weight": 94.0}
# ]
#
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('main.html')
# msg = tm.render(users=persons, title="About Jinja2")
#
# print(msg)


#


# subs = ["Культура", "Наука", "Политика", "Спорт"]
#
#
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('about.html')
# msg = tm.render(list_table=subs)
#
# print(msg)


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('dz.html')
msg = tm.render()

print(msg)


















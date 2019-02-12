# Домашнее задание к лекции 2.3 «Database. PostgreSQL»

1. Напишите следующие функции для работы с таблицами:

```
def create_db(): # создает таблицы
    pass

def get_students(course_id): # возвращает студентов определенного курса
    pass

def add_students(course_id, students): # создает студентов и 
                                       # записывает их на курс
    pass


def add_student(student): # просто создает студента
    pass

def get_student(student_id):
    pass
```

Объекты "Студент" передаются в функцию в виде словаря. Вызов функции `add_students` должен выполнять создание всех сущностей в транзакции.

Схемы:
```
Student:
 id     | integer                  | not null
 name   | character varying(100)   | not null
 gpa    | numeric(10,2)            |
 birth  | timestamp with time zone |

Course:
 id     | integer                  | not null
 name   | character varying(100)   | not null
```

---
Домашнее задание сдается ссылкой на репозиторий [BitBucket](https://bitbucket.org/) или [GitHub](https://github.com/)

Не сможем проверить или помочь, если вы пришлете:
* архивы;
* скриншоты кода;
* теоретический рассказ о возникших проблемах.    
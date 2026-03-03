from datetime import date, datetime, timedelta
from textwrap import dedent

from sqlalchemy import Column, Date, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=date.today())


engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base.metadata.create_all(engine)
Session = sessionmaker(engine)


def list_tasks(deadline):
    with Session() as session:
        tasks = session.query(Task).filter(Task.deadline == deadline).all()
        if tasks:
            for i, t in enumerate(tasks, 1):
                print(f'{i}. {t.task}')
        else:
            print('Nothing to do!')


def list_missed_tasks():
    with Session() as session:
        tasks = session.query(Task).filter(Task.deadline < date.today()).all()
        if tasks:
            _display_tasks(tasks)
        else:
            print('All tasks have been completed!')


def list_all_tasks():
    with Session() as session:
        tasks = session.query(Task).order_by(Task.deadline).all()
        if tasks:
            _display_tasks(tasks)
        else:
            print('Nothing to do!')


def add_task():
    with Session() as session:
        task = input('\nEnter a task\n')
        deadline = input('Enter a deadline\n')
        deadline = datetime.strptime(deadline, '%Y-%m-%d').date()
        session.add(Task(task=task, deadline=deadline))
        session.commit()
        print('The task has been added!')


def delete_task():
    print('\nChoose the number of the task you want to delete:')
    with Session() as session:
        tasks = session.query(Task).order_by(Task.deadline).all()
        if tasks:
            _display_tasks(tasks)
            to_delete = int(input())
            session.delete(tasks[to_delete - 1])
            session.commit()
            print('The task has been deleted!')
        else:
            print('Nothing to delete')


def _display_tasks(tasks):
    for i, t in enumerate(tasks, 1):
        print(f'{i}. {t.task}. {t.deadline.strftime("%-d %b")}')


def main_menu():
    while True:
        print(
            dedent("""\
        
            1) Today's tasks
            2) Week's tasks
            3) All tasks
            4) Missed tasks
            5) Add a task
            6) Delete a task
            0) Exit""")
        )
        match input():
            case '1':
                today = date.today()
                print(today.strftime('\nToday %-d %b:'))
                list_tasks(today)
            case '2':
                for weekday in (date.today() + timedelta(days=offset) for offset in range(7)):
                    print(weekday.strftime('\n%A %-d %b:'))
                    list_tasks(weekday)
            case '3':
                print('\nAll tasks:')
                list_all_tasks()
            case '4':
                print('\nMissed tasks:')
                list_missed_tasks()
            case '5':
                add_task()
            case '6':
                delete_task()
            case '0':
                print('\nBye!')
                return


main_menu()

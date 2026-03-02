from datetime import date, datetime, timedelta

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
        rows = session.query(Task).filter(Task.deadline == deadline).all()
        if rows:
            for i, row in enumerate(rows, 1):
                print(f'{i}. {row.task}')
        else:
            print('Nothing to do!')


def list_all_tasks():
    with Session() as session:
        rows = session.query(Task).order_by(Task.deadline).all()
        if rows:
            for i, row in enumerate(rows, 1):
                print(f'{i}. {row.task}. {row.deadline.strftime("%-d %b")}')
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


def main_menu():
    while True:
        print("\n1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Add a task\n0) Exit")
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
                add_task()
            case '0':
                print('\nBye!')
                return


main_menu()

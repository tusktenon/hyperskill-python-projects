from datetime import datetime

from sqlalchemy import Column, Date, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())


engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base.metadata.create_all(engine)
Session = sessionmaker(engine)


def list_tasks():
    print('\nToday:')
    with Session() as session:
        rows = session.query(Task).all()
        if rows:
            for i, row in enumerate(rows, 1):
                print(f'{i}. {row.task}')
        else:
            print('Nothing to do!')


def add_task():
    with Session() as session:
        print('\nEnter a task')
        session.add(Task(task=input()))
        session.commit()
        print('The task has been added!')


def main_menu():
    while True:
        print("\n1) Today's tasks\n2) Add a task\n0) Exit")
        match input():
            case '1':
                list_tasks()
            case '2':
                add_task()
            case '0':
                print('\nBye!')
                return


main_menu()

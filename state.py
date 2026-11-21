from maxapi.context.state_machine import State, StatesGroup


class ProcessExcel(StatesGroup):

    waiting_first_file = State()  # Ожидание первого файла
    waiting_second_file = State()  # Ожидание второго файла
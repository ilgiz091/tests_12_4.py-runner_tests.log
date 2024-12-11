import logging
from rt_with_exceptions import Runner

class RunnerTest:
    def test_walk(self):
        try:
            print(Runner('Вася', -5))
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            print(Runner(1, 2))
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')
    runner_test = RunnerTest()
    runner_test.test_walk()
    runner_test.test_run()




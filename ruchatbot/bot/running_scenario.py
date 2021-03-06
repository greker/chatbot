from ruchatbot.bot.running_dialog_status import RunningDialogStatus


class RunningScenario(RunningDialogStatus):
    """
    Переменные состояния исполняющегося сценария.
    Экземпляр создается при запуске сценария и удаляется после завршения сценария,
    поэтому накопленная в этой структуре информация о выполнении шагов не будет
    влиять на новый запуск сценария.
    """
    def __init__(self, scenario, current_step_index):
        super(RunningScenario, self).__init__(scenario.get_priority())
        self.scenario = scenario
        self.current_step_index = current_step_index
        self.passed_steps = set()

    def get_insteadof_rules(self):
        return self.scenario.insteadof_rules

    def get_smalltalk_rules(self):
        return self.scenario.smalltalk_rules

    def get_name(self):
        return self.scenario.get_name()

from hstest import StageTest, dynamic_test, TestedProgram, WrongAnswer, CheckResult


class Config:
    SURVIVED_MESSAGE = 'You survived!'
    HANGED_MESSAGE = 'You lost!'

    @staticmethod
    def correct_inputs():
        return [
            'python',
        ]

    @staticmethod
    def incorrect_inputs():
        return [
            'java',
            'pyton',
            'javascript'
        ]

    @classmethod
    def all_inputs(cls):
        return cls.correct_inputs() + cls.incorrect_inputs()


class HangmanTest(StageTest):

    @dynamic_test(data=Config.correct_inputs())
    def test_should_print_survived_message(self, guessed_word):
        survived_message = Config.SURVIVED_MESSAGE

        pr = TestedProgram(self.source_name)
        pr.start()
        output = pr.execute(guessed_word).strip().lower()
        has_survived_message = survived_message.lower() in output

        if not has_survived_message:
            raise WrongAnswer(f'It looks like your output is wrong.\n'
                              f'Input: {guessed_word}\n'
                              f'Correct output: {survived_message}')

        return CheckResult.correct()

    @dynamic_test(data=Config.incorrect_inputs())
    def test_should_print_hanged_message(self, guessed_word):
        hanged_message = Config.HANGED_MESSAGE

        pr = TestedProgram(self.source_name)
        pr.start()
        output = pr.execute(guessed_word).strip().lower()
        has_hanged_message = hanged_message.lower() in output

        if not has_hanged_message:
            raise WrongAnswer(f'It looks like your output is wrong.\n'
                              f'Input: {guessed_word}\n'
                              f'Correct output: {hanged_message}')

        return CheckResult.correct()

    @dynamic_test(data=Config.all_inputs())
    def test_should_not_print_both_messages(self, guessed_word):
        survived_message = Config.SURVIVED_MESSAGE
        hanged_message = Config.HANGED_MESSAGE

        pr = TestedProgram(self.source_name)
        pr.start()
        output = pr.execute(guessed_word).strip().lower()

        has_survived_message = survived_message.lower() in output
        has_hanged_message = hanged_message.lower() in output

        if has_survived_message and has_hanged_message:
            raise WrongAnswer(f'It looks like your output contains both \"{survived_message}\" and \"{hanged_message}\".\n'
                              f'Please, output only one of them.')

        return CheckResult.correct()


if __name__ == '__main__':
    HangmanTest('hangman.hangman').run_tests()

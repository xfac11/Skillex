import click
class Selector:
    def __init__(self, message:str, selections:list):
        self.selection_list = selections
        self.message = message
    
    def select(self, test_input=None):
        index = 1
        for selection in self.selection_list:
            click.echo(f"{index}. {selection}")
            index += 1
        if test_input:
            click.echo(self.message)
            return self.selection_list[test_input - 1]
        prompt_input = click.prompt(self.message, show_choices=True, type=int)
        if prompt_input == 0:
            return None
        return self.selection_list[prompt_input - 1]
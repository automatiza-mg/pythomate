import click
from .run import run_flow


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
@click.pass_context
@click.version_option()
def cli(ctx):
  """
    CLI para iniciar fluxo(s) do Power Automate via linha de comando.
    Aliado ao agendador de tarefas Windows cria-se gatilho(s) de fluxo(s),
    não permitidos nas versões gratúitas do Power Automate.
  """

@cli.group()
@click.argument('flow', required=True)
def run(flow):
  """
    Executa fluxo desejado:
    pythomate run <nome-fluxo>
  """
  pass

run.add_command(run_flow)

import click
from pythomate.run import run_flow

@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
@click.pass_context
@click.argument('flow', required=True)
@click.version_option()
def cli(ctx):
  """
    CLI para iniciar fluxo(s) do Power Automate via linha de comando.
    Aliado ao agendador de tarefas Windows cria-se gatilho(s) de fluxo(s), 
    não permitidos nas versões gratúitas do Power Automate.
  """

run.add_command(run_flow)

@cli.group()
@click.version_option()
@click.argument('flow', required=True)
def run(flow):
  """
    Executa fluxos
  """	
  pass

# @cli.group()
# @click.argument('flow', required=True)
# def run(flow):
#   """
#     Executa fluxos
#   """	
#   pass

run.add_command(run_flow)
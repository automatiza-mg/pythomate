# Pythomate

Pacote [pythomate](https://pypi.org/project/pythomate/) inicia fluxo(s) do Power Automate via linha de comando.
Aliado ao agendador de tarefas Windows cria-se gatilho(s) de fluxo(s)[^1].

## Instalação

O `pythomate` está disponível no Python Package Index - [PyPI](https://pypi.org/project/pythomate/), sendo **compatível apenas com sistema operacional Windows**.
Ele pode ser instalado utilizando-se o comando[^2]:

```bash
# Sugerimos a instalação em ambiente virtual
$ pip install pythomate
```

Necessário adicionar ao `PATH` do Windows caminho de instalação da ferramenta Power Automate[^3].

## Uso

Diretamente na linha de comando:

```bash
# Não copie e cole cegamente o comando abaixo.
# Substituo <nome-fluxo> pelo nome do fluxo que deseja iniciar.
$ pythomate run <nome-fluxo>
```

## Contribuições

Veja o arquivo [`CONTRIBUTING.md`](CONTRIBUTING.md) para mais detalhes.

## Licença

O **pythomete** é licenciado sob a licença MIT.
Veja o arquivo [`LICENSE.txt`](LICENSE.txt) para mais detalhes.

Teste push.

[^1]: Gatilhos automáticos de fluxo(s) não são permitidos nas versões gratúitas do Power Automate.
[^2]: Sugerimos a utilização da Git Bash disponível na instalação do programa [Git for Windows](https://gitforwindows.org/). 
[^3]: Power Automate, em geral, encontra-sem instalado em `C:/Program Files (x86)/Power Automate Desktop/`.

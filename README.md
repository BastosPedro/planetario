# planetario
Projeto de um planetário para a seleção do lccv.

Versão do Python: 3.7.3

Módulos Utilizados:
- numpy (1.16.3)
- scipy (1.2.1)
- pandas (0.24.2)
- openpyxl (2.6.2)
- xlrd (1.2.0)
- matplotlib (3.0.3)

Para usar o programa basta, com os módulos corretos instalados, rodar o script _main.py_. A leitura inicial de dados é a partir de um arquivo .txt dentro do formato estipulado pelo exercício.

Alternativamente, o usuário pode optar por instanciar as classes, de preferência na ordem: 
- Data, que recebe o diretório do arquivo .txt com os dados
- EulerModule, que recebe uma instância de Data, e pode retornar um arquivo .xlsx através do comando _spreadSheet_
- Plotter, que recebe o diretório de um arquivo .xlsx gerado por uma instância do _EulerModule_ e pode plotar a partir do comando _plot2d_

Os métodos estão documentados para a facilitar o entedimento.

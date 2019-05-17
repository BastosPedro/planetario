# planetario
Projeto de um planetário para o processo seletivo do LCCV-UFAL 2019.

Versão do Python: 3.7.3

Módulos Utilizados:
- numpy (1.16.3);
- scipy (1.2.1);
- pandas (0.24.2);
- openpyxl (2.6.2);
- xlrd (1.2.0);
- matplotlib (3.0.3);

Para usar o programa basta, com os módulos corretos instalados, instanciar a classe MainModule, e rodar um de seus testes demonstrativos (_simples_, _complicado_, _batida_), ou então um teste 
customizado (_custom2d_ ou _custom3d_) para usar as informações . 

A leitura inicial de dados é a partir de um arquivo .txt dentro do formato estipulado pelo exercício.

Alternativamente, o usuário pode optar por instanciar as classes, de preferência na ordem: 
- Data, que recebe o diretório do arquivo .txt com os dados;
- EulerModule, que recebe uma instância de Data, e pode retornar um arquivo .xlsx através do método _spreadSheet_;
- Plotter, que recebe o diretório de um arquivo .xlsx gerado por uma instância do _EulerModule_ e pode plotar a partir do método _plot2d_ ou _plot3d_ (com as alternativas _plot2dToFile_ e _plot3dToFile_ que armazenam o resultado na memória secundária).

Os métodos estão documentados para a facilitar o entedimento.

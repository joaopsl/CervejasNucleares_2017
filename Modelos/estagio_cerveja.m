% Cerveja

clear all;

% dados obtidos com pot�ncia m�xima (supomos que seja 100W)
data = read_csv('Teste_balde_3.csv');

% temperatura do balde
beer = data.beer;

% entrada do sistema (step de 100W)
pot_in = (100*ones(8380,1));
pot_in(1) = 0;

% resposta do sistema (apenas parte do arrefecimento)
beer_out = beer(1:8380);

% fun��o de transfer�ncia (obtida com toolbox de identifica��o de sistemas)
tf = load('tf.mat');
tr_funct = tf.tf1;
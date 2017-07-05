% Cerveja

clear all;

% constants
Ts = 1;

% import data

data = read_csv('Teste_balde_3.csv');

beer = data.beer;
fridge = data.fridge;
sala = data.sala;

% modelo aquecimento

Phi = [beer(8925:end-1)-fridge(8925:end-1) beer(8925:end-1)];
Y = beer(8926:end);

Theta = inv(Phi'*Phi)*Phi'*Y;

K_loss = -Theta(1)/Ts;

% modelo arrefecimento

Phi = [beer(1:8925-1)-fridge(1:8925-1) beer(1:8925-1)];
Y = beer(2:8925);

Theta = inv(Phi'*Phi)*Phi'*Y;

K_loss_a = -Theta(1)/Ts;

% arrefecimento
% t=1:14477;
% p = polyfit(t',fridge(1:14477),2);
% 
% tf_1 = 25;
% tf_2 = 18;
% 
% arrefece = polyval(p,-15000:20000);
% 
% tmp1 = abs(arrefece-tf_1);
% [idx1 idx1] = min(tmp1);
% closest1 = arrefece(idx1);
% 
% tmp2 = abs(arrefece-tf_2);
% [idx2 idx2] = min(tmp2);
% closest2 = arrefece(idx2);
% 
% delta = (idx2-idx1)*10.5;
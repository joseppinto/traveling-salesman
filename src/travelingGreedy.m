function [Tdist,town]=greedy(D)

% A simple "greedy" algorithm for the Traveling Salesman Problem. Given  
% n points by its (x,y) coordinates, D(i,j) holds the distance between the 
% 2 points (x(i),y(i)) and (x(j),y(j)). The code uses a "greedy" approach 
% in trying to find the shortest route that starts at one of the points 
% ("towns"), randomly choosen, goes once through everyone of the others 
% and returns to the starting point. For each journey, the closest town 
% not yet visited, is always choosen.

n=length(D);
town(1)=randi(n);  % starting point
to_visit=setdiff(1:n,town(1)); 
Tdist=0;
for i=1:n-1        % ith journey
     [dist, pos]=min(D(town(i),to_visit));
     town(i+1)=to_visit(pos);
     Tdist=Tdist+dist;
     to_visit=setdiff(to_visit,town(i+1));
end
Tdist=Tdist+D(town(1),town(n));





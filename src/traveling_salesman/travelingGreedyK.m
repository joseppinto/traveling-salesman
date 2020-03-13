function [Tdist,town]=greedyK(D, r, K)

% A simple "greedy" algorithm for the Traveling Salesman Problem. Given  
% n points by its (x,y) coordinates, D(i,j) holds the distance between the 
% 2 points (x(i),y(i)) and (x(j),y(j)). The code uses a "greedy" approach 
% in trying to find the shortest route that starts at one of the points 
% ("towns"), randomly choosen, goes once through everyone of the others 
% and returns to the starting point. For each journey, the closest town 
% not yet visited, is always choosen.

n=length(D);
town(1)=r;  % starting point
to_visit= 1:n;
Tdist=0;
poss = [town(1)];
i = 1;
while i < n        
     to_visit = setdiff(to_visit,to_visit(poss));
     [~, poss]=mink(D(town(i),to_visit), K);
     town = [town to_visit(poss)];
     i = i + length(poss);
end
for i=1:n-1
     Tdist = Tdist + D(town(i), town(i+1));
end
Tdist=Tdist+D(town(1),town(n));
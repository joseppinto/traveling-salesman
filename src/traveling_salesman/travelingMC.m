function [Tdist,town]=travelingMC(D)

% A simple Monte-Carlo algorithm for the Traveling Salesman Problem. Given  
% n points by its (x,y) coordinates, D(i,j) holds the distance between the 
% 2 points (x(i),y(i)) and (x(j),y(j)). The code tries to find the shortest  
% route that starts at one of the points ("towns"), goes once through 
% everyone of the others and returns to the starting point. It starts with
% an initial random route (a random permutation of the first n integer 
% numbers), and then shortens the total distance through successive swaps 
% in the order of 2 neighbouring towns

n=length(D);
% FIRST tentative route 
town=randperm(n);           % a random permutation of the first n integers  
Tdist=D(town(n),town(1));
for i=1:n-1                               % initial length
    Tdist=Tdist+D(town(i),town(i+1));     % of route
end

i=0;
while i < 100          % stop if no changes occur for 100 trials
    c=randi(n);        % randomly chooses a town (at position c in route)
    if c==1  
        previous=n; next1=2; next2=3;
    elseif c==n-1
        previous=n-2; next1=n; next2=1;
    elseif c==n
        previous=n-1; next1=1; next2=2;
    else
        previous=c-1; next1=c+1; next2=c+2;
    end

    % delta=increment in length of route
    
    delta=D(town(previous),town(next1))+D(town(c),town(next2))-D(town(previous),town(c))-D(town(next1),town(next2)); 
    % accept or discard change to route 
    if delta<0 
        temp=town(c); town(c)=town(next1); town(next1)=temp; % swap order of town(c) and town(c+1) in route                 
        Tdist=Tdist+delta;   
        i=0;
    else i=i+1;
    end
   
end




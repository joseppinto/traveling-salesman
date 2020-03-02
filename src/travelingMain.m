function travelingMain(n,procs)

% This is a simulation of a parallel execution on p processors of the codes
% traveling, travelingSA and travelingGreedy
% The parallel solution is thus the answer with smaller cost.

% generates the position of each town in a square of side 10...
x=10*rand(1,n); y=10*rand(1,n); 
% ... and computes the distances between them 
for i=1:n
    for j=1:n
        D(i,j)=sqrt((x(i)-x(j))^2+(y(i)-y(j))^2);
    end
end
clf  % clear current figure window

% Run greedy algorithm
for p=1:procs
    [Tdist3(p),route3]=travelingGreedy(D);
    subplot(3,procs,p);
    plot([x(route3),x(route3(1))],[y(route3),y(route3(1))],'k',x(route3),y(route3),'o',x(route3(1)),y(route3(1)),'*')
    legend('Greedy',num2str(Tdist3(p)),'start')
end

% Run MC simulation  
for p=1:procs
    [Tdist2(p),route2]=travelingMC(D);
    subplot(3,procs,procs+p);
    plot([x(route2),x(route2(1))],[y(route2),y(route2(1))],'k',x(route2),y(route2),'o',x(route2(1)),y(route2(1)),'*')
    legend('MC',num2str(Tdist2(p)),'start')
    
% Run simulated annealing
for p=1:procs
    [Tdist(p),route]=travelingSA(D);
    subplot(3,procs,2*procs+p);
    plot([x(route),x(route(1))],[y(route),y(route(1))],'r',x(route),y(route),'o',x(route(1)),y(route(1)),'*')
    legend('SA', num2str(Tdist(p)),'start')
end

 

end


[Tdist' Tdist2' Tdist3']




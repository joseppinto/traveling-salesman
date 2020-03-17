function travelingMain(n,procs, area, circle)

    % This is a simulation of a parallel execution on p processors of the codes
    % traveling, travelingSA and travelingGreedy
    % The parallel solution is thus the answer with smaller cost.
    
    % generates the position of each town in a square of side 10...
    if circle
        radius = sqrt(area/pi);
        x = [];
        y = [];
        for i=1:n
            xx = radius;
            yy = radius;
            while xx^2 + yy^2 > radius^2
                xx = rand()*radius;
                yy = rand()*radius;
            end
            x(end + 1) = xx;
            y(end + 1) = yy;
        end
    else
        x=sqrt(area)*rand(1,n); 
        y=sqrt(area)*rand(1,n); 
    end
% ... and computes the distances between them 
for i=1:n
    for j=1:n
        D(i,j)=sqrt((x(i)-x(j))^2+(y(i)-y(j))^2);
    end
end
clf  % clear current figure window

r = randi(n);

% Run greedy2 algorithm
for p=1:procs
    tic
    [Tdist4(p),route4]=travelingGreedyK(D, r, fix(n/30) + 10);
    [Times4(p)] = toc;
    %subplot(3,procs,p);
    %plot([x(route3),x(route3(1))],[y(route3),y(route3(1))],'k',x(route3),y(route3),'o',x(route3(1)),y(route3(1)),'*')
    %legend('Greedy',num2str(Tdist3(p)),'start')
end

% Run greedy algorithm
for p=1:procs
    tic
    [Tdist3(p),route3]=travelingGreedy(D, r);
    [Times3(p)] = toc;
    %subplot(3,procs,p);
    %plot([x(route3),x(route3(1))],[y(route3),y(route3(1))],'k',x(route3),y(route3),'o',x(route3(1)),y(route3(1)),'*')
    %legend('Greedy',num2str(Tdist3(p)),'start')
end

% Run MC simulation  
for p=1:procs
    tic
    [Tdist2(p),route2]=travelingMC(D);
    [Times2(p)] = toc;
    %subplot(3,procs,procs+p);
    %plot([x(route2),x(route2(1))],[y(route2),y(route2(1))],'k',x(route2),y(route2),'o',x(route2(1)),y(route2(1)),'*')
    %legend('MC',num2str(Tdist2(p)),'start')
    
% Run simulated annealing
for p=1:procs
    tic
    [Tdist(p),route]=travelingSA(D);
    [Times(p)] = toc;
    %subplot(3,procs,2*procs+p);
    %plot([x(route),x(route(1))],[y(route),y(route(1))],'r',x(route),y(route),'o',x(route(1)),y(route(1)),'*')
    %legend('SA', num2str(Tdist(p)),'start')
end

 

end


[Tdist' Tdist2' Tdist3' Tdist4']
disp("tempos")
[Times' Times2' Times3' Times4']




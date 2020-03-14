function [Tdist,town]=greedyK(D, r, K)


n=length(D);
town(1)=r;  % starting point
to_visit= 1:n;
Tdist=0;
poss = [town(1)];
i = 1;
while i < n        
     to_visit = setdiff(to_visit,to_visit(poss));
     [~, poss]=mink(D(town(i),to_visit), K);
     if length(poss) > 2
          for j=1:length(poss)-2
               [~, newps] = mink(D( to_visit(poss(j)) , to_visit(poss(j+1:end))), K);
               poss(j+1:end) = poss(newps + j);
          end
     end
     town = [town to_visit(poss)];
     i = i + length(poss);
end
for i=1:n-1
     Tdist = Tdist + D(town(i), town(i+1));
end
Tdist=Tdist+D(town(1),town(n));
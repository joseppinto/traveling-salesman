function [Tdist,town]=greedyK(D, r, K)

n=length(D);

town(1)=r;  % starting point
to_visit= 1:n;
Tdist=0;
i = 1;
count = 0;
mn = 0;
poss = [town(1)];
while i < n        
     to_visit = setdiff(to_visit,to_visit(poss));
     [dists, poss]=mink(D(town(i),to_visit), K);
     count = count + 1;
     mn = (mn * (count - 1) + dists(1))/count; 
     if length(poss) > 2
          for j=1:length(poss)-2
               [dists, newps] = mink(D( to_visit(poss(j)) , to_visit(poss(j+1:end))), K);
               if abs(dists(1) - mn) > 3*mn
                    poss(j+1:end) = [];
                    break
               end
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
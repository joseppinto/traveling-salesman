function [ks,indices]=mink(array, k)
if k > length(array)
    [ks, indices] = sort(array);
    return
end
[ks, indices] = sort(array);
ks = ks(1:k);
indices = indices(1:k);

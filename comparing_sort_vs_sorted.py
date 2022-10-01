x = [4,5,7,1,0,2]
%timeit sorted(x)
#134 ns ± 0.744 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
%timeit x.sort()
#48.4 ns ± 0.527 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
x = [4,5,7,1,0,2,55,45,33,87,100000,65,11,12,10]
%timeit sorted(x)
#207 ns ± 1.79 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
%timeit x.sort()
#69.1 ns ± 0.689 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

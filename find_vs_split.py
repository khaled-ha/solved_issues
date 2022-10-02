data = "blablabla:sijhdosqnhfdklsfdnsq"
%timeit data[data.find(':')+1:]
# 122 ns ± 0.976 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
%timeit data.split(':')[1]
# 108 ns ± 2.14 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

%timeit data.split(':')[1]
# 94 ns ± 0.723 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

%timeit data[data.find(':')+1:]
# 115 ns ± 2.5 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
# pip install memory_profiler

%load_ext memory_profiler

%mprun -f convert_units convert_units(heroes, hts, wts)
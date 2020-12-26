# pip install line_profiler

import line_profiler

%load_ext line_profiler

%lprun -f convert_units convert_units(heroes, hts, wts)
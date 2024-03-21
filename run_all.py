import os, sys
import subprocess
import shutil
import time
run_name = sys.argv[1]
only_run = None
extra_flags = ""
if len(sys.argv) > 2:
    only_run = "".join(sys.argv[2])
if len(sys.argv) > 3:
    extra_flags = "".join(sys.argv[3])

print("only run is", only_run)

output_dir =f"outputs/{run_name}"
os.makedirs(output_dir, exist_ok=True)

subprocess.run(f"nim compile --verbosity:0 --hints:off -w:off --deepcopy:on -d:debugging --opt:speed {extra_flags} solve.nim", shell=True, text=True)

start = (time.time())
processes = []
for file_num, file in enumerate(os.listdir("inputs")):
    # if os.path.isfile(file):
    if only_run is not None:
        if file[0] not in only_run:
            continue
    print("running", file)
    current = subprocess.Popen(f"solve.exe < inputs/{file} > {output_dir}/{file[0]}_{run_name}.txt", shell=True, text=True)
    # current.wait()
    processes.append(current)
    

for i, process in enumerate(processes):
    process.wait()
    print(i, "done")
end = time.time() - start
print(end)
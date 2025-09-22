Instruction-Level Parallelism (ILP) Exploration using gem5
Project Overview

This repository contains a practical exploration of Instruction-Level Parallelism (ILP) using the gem5 simulator. The project demonstrates how modern CPU architectures exploit parallelism to improve instruction throughput and reduce latency. The experiments cover:

Basic Pipeline Simulation – A standard 5-stage pipeline (Fetch, Decode, Execute, Memory, Writeback).

Branch Prediction – Implementation of a dynamic branch predictor to reduce pipeline stalls.

Superscalar Execution – Multiple instructions issued per cycle to improve throughput.

Simultaneous Multithreading (SMT) – Multiple threads sharing processor resources to maximize utilization.

The project includes gem5 configuration scripts, benchmark workloads, and simulation results with detailed instructions for reproducing the experiments.

Repository Structure:
gem5/
├── configs/
│   ├── ilp_exploration.py        # Main gem5 configuration script
├── tests/
│   └── test-progs/
│       └── hello/bin/x86/linux/hello   # Sample workload
├── m5out/                        # Directory for gem5 output files
├── README.md                      # Project documentation

Installation

Clone this repository: 
git clone (https://github.com/Boogie3586/Assignment-4-Exploring-Instruction-Level-Parallelism-ILP-in-Modern-Processors/blob/main/ilp_exploration.py)
cd ILP-gem5

Set up gem5 (if not already installed):
# Navigate to your gem5 source folder
cd /path/to/gem5
scons build/X86/gem5.opt -j$(nproc)
Use system.cpu.width = 1 and system.cpu.numThreads = 1 for single-issue pipeline.

2. Branch Prediction

Enable dynamic branch prediction by using system.cpu.branchPred = TournamentBP() in ilp_exploration.py.

Run the same simulation as above.

Compare the IPC and latency with and without branch prediction.

3. Superscalar Execution

Set system.cpu.width = 2 (or higher) in the configuration script.

Run benchmarks to observe improved instruction throughput.

Compare single-issue vs. superscalar IPC.

4. Simultaneous Multithreading (SMT)

Set system.cpu.numThreads = 2 in ilp_exploration.py.

Run simulations to observe shared pipeline utilization and overall throughput.

Monitor any bottlenecks in functional units.

Viewing Statistics

After each simulation, gem5 generates a stats.txt file in the m5out folder. You can filter key performance metrics:
Ensure workloads are executable:
chmod +x tests/test-progs/hello/bin/x86/linux/hello

Running the Simulations
1. Basic Pipeline

Navigate to the configs folder:
cd /mnt/c/Users/yourname/gem5/configs

Run the simulation:
/mnt/c/Users/yourname/gem5/build/X86/gem5.opt ilp_exploration.py

cat m5out/stats.txt | grep -E "ipc|instructions|branch"

Metrics include:

IPC (Instructions per Cycle)

Average Instruction Latency

Branch Prediction Accuracy

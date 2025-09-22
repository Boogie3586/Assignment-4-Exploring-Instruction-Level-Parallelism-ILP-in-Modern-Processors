# ilp_exploration.py
# gem5 configuration file for exploring Instruction-Level Parallelism (ILP)
# Supports: Basic Pipeline, Branch Prediction, Superscalar, and SMT

from m5.objects import *
import m5
from m5.util import addToPath

# ---------------------------
# System Configuration
# ---------------------------
system = System()
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '1GHz'
system.clk_domain.voltage_domain = VoltageDomain()
system.mem_mode = 'timing'          # Use timing memory mode
system.mem_ranges = [AddrRange('512MB')]

# ---------------------------
# CPU Configuration
# ---------------------------
system.cpu = DerivO3CPU()  # Out-of-order CPU for maximum ILP support

# Pipeline width and issue
system.cpu.width = 1          # 1 for single-issue pipeline
system.cpu.numROBEntries = 32 # Reorder buffer entries
system.cpu.numIQEntries = 16  # Instruction Queue
system.cpu.numLSQEntries = 16 # Load-store queue

# Branch Predictor Configuration
system.cpu.branchPred = TournamentBP()  # Dynamic predictor (can switch to StaticBP)

# ---------------------------
# Memory System
# ---------------------------
system.membus = SystemXBar()
system.cpu.icache = L1ICache(size='16kB')
system.cpu.dcache = L1DCache(size='16kB')
system.cpu.icache.port = system.membus.slave
system.cpu.dcache.port = system.membus.slave

# ---------------------------
# Workload / Process
# ---------------------------
process = Process()
process.cmd = ['/mnt/c/Users/carte/gem5/tests/test-progs/hello/bin/x86/linux/hello'] 
system.cpu.workload = process
system.cpu.createThreads()

# ---------------------------
# System Port and Memory
# ---------------------------
system.system_port = system.membus.slave

# ---------------------------
# Root Simulation Object
# ---------------------------
root = Root(full_system=False, system=system)

# ---------------------------
# Superscalar / SMT Options
# ---------------------------
# Modify these values to experiment
# For superscalar, set width > 1
# For SMT, set numThreads > 1
system.cpu.width = 2         # 2 instructions per cycle
system.cpu.numThreads = 2    # Enable 2 threads for SMT

# ---------------------------
# Run the Simulation
# ---------------------------
print("Starting ILP simulation with gem5...")
m5.instantiate()
exit_event = m5.simulate()
print("Simulation ended at tick {}: {}".format(m5.curTick(), exit_event.getCause()))

# ---------------------------
# Display Statistics
# ---------------------------
print("\n===== Simulation Statistics =====\n")
stats = m5.stats
stats.dump()
stats.reset()
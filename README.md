# Cocotb Dual-Sim Template

Reusable Verilog-2001/SystemVerilog starter with automated **Verilator + Icarus Verilog** Cocotb CI on every push.

[[https://github.com/nk-verif-labs/cocotb-dual-sim-template/actions/workflows/ci.yml/badge.svg]](https://github.com/nk-verif-labs/cocotb-dual-sim-template/actions/workflows/ci.yml)

## Results

| Metric | Value |
| --- | --- |
| Simulators in CI | Verilator + Icarus Verilog (Ubuntu 24.04) |
| Framework | Cocotb 1.9.2 + pytest |
| Test coverage | 32-beat randomized ready/valid backpressure |

## Quick start

    git clone https://github.com/nk-verif-labs/cocotb-dual-sim-template.git
    cd cocotb-dual-sim-template
    make SIM=verilator
    make SIM=icarus

## Need something similar?

NK Verif Labs offers verification and RTL-to-GDSII services. Email **nkveriflabs@gmail.com**.

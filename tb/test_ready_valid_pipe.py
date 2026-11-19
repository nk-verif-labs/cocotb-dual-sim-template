import random, cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def test_backpressure(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())
    dut.rst_n.value = 0; dut.s_valid.value = 0; dut.m_ready.value = 0; dut.s_data.value = 0
    for _ in range(3): await RisingEdge(dut.clk)
    dut.rst_n.value = 1
    sent = [random.randint(0, 255) for _ in range(32)]
    got, idx = [], 0
    while len(got) < len(sent):
        dut.s_valid.value = int(idx < len(sent))
        dut.s_data.value = sent[idx] if idx < len(sent) else 0
        dut.m_ready.value = random.randint(0, 1)
        await RisingEdge(dut.clk)
        if dut.s_valid.value and dut.s_ready.value: idx += 1
        if dut.m_valid.value and dut.m_ready.value: got.append(int(dut.m_data.value))
    assert got == sent, f"Mismatch: {got} != {sent}"

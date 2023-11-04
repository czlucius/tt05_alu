import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles


segments = [ 63, 6, 91, 79, 102, 109, 125, 7, 127, 111 ]

@cocotb.test()
async def test_7seg(dut):
    dut._log.info("start")
                    #   yyyyxxxx
                    #   01230123
    dut.ui_in.value = 0b10111001

    dut.clk = 0
    dut.ena = 1
    dut._log.info("reset")
    dut.rst_n.value = 1

    dut.uio_in.value = 0
    assert dut.uo_out.value == 22

    # subtract may be a little finicky
    dut.uio_in.value = 1
    dut.log_info("subtract out")
    dut.log_info(dut.uo_out.value)
    assert dut.uo_out.value == 0b11111100

    dut.uio_in.value = 2
    assert dut.uo_out.value == 117

    dut.uio_in.value = 3
    dut.ui_in.value = 0b10011011
    dut.log_info("divide out")
    dut.log_info(dut.uo_out.value)
    assert dut.uo_out.value == 1

    dut.uio_in.value = 4
    dut.ui_in.value = 0b10011011
    assert dut.uo_out.value == 0b1001

    dut.uio_in.value = 5
    assert dut.uo_out.value == 0b1101


    dut.uio_in.value = 6
    assert dut.uo_out.value == 0b0100

    dut.uio_in.value = 7
    assert dut.uo_out.value == 0b0110

    dut.uio_in.value = 8
    assert dut.uo_out.value == 0b0010

    dut.uio_in.value = 9
    assert dut.uo_out.value == 0b01000110

    dut.uio_in.value = 10
    assert dut.uo_out.value == 4

    dut.ui_in.value = 11
    dut.ui_in.value = 0b1100_0110
    assert dut.uo_out.value == 48

    dut.ui_in.value = 12
    dut.ui_in.value = 0b1000_0110
    assert dut.uo_out.value == 3






    
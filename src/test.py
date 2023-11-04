import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles


segments = [ 63, 6, 91, 79, 102, 109, 125, 7, 127, 111 ]

@cocotb.test()
async def test_alu(dut):
    dut._log.info("start")
                    #   yyyyxxxx
                    #   32103210
    dut.clk.value = 0
    dut.ena.value = 1
    dut.uio_out.value = 0x0
    dut.uo_out.value = 0x0
    dut.uio_oe.value = 0x0

    dut._log.info("reset")
    dut.rst_n.value = 0
    dut.rst_n.value = 1

    dut.ui_in.value = 0b10111001

    dut.uio_in.value = 0
    await Timer(20, units="ns")
    assert dut.uo_out.value == 20

    # subtract may be a little finicky
    dut.uio_in.value = 1
    await Timer(20, units="ns")
    assert dut.uo_out.value == 0b11111110

    dut.uio_in.value = 2
    await Timer(20, units="ns")
    assert dut.uo_out.value == 99

    dut.uio_in.value = 3
    dut.ui_in.value = 0b10011011
    await Timer(20, units="ns")
    assert dut.uo_out.value == 1

    dut.uio_in.value = 4
    dut.ui_in.value = 0b10011011
    await Timer(20, units="ns")
    assert dut.uo_out.value == 0b1001

    dut.uio_in.value = 5
    await Timer(20, units="ns")
    assert dut.uo_out.value == 0b1011


    dut.uio_in.value = 6
    await Timer(20, units="ns")
    assert dut.uo_out.value == 0b0010

    dut.uio_in.value = 7
    await Timer(20, units="ns")
    assert dut.uo_out.value == 0b0110

    dut.uio_in.value = 8
    await Timer(20, units="ns")
    assert dut.uo_out.value == 0b0100

    dut.uio_in.value = 9
    dut.ui_in.value = 0b10011011
    await Timer(20, units="ns")
    assert dut.uo_out.value == 0b01100100

    dut.uio_in.value = 10
    await Timer(20, units="ns")
    assert dut.uo_out.value == 2


    dut.ui_in.value = 0b01100111 
    dut.uio_in.value = 11
    
    #00000010
    # 
    # 0110
    # 1100
    # 1000
    # 0000

    #00000101

    await Timer(20, units="ns")
    assert dut.uo_out.value == 0b11000000

    
    dut.ui_in.value = 0b0001_0110
    dut.uio_in.value = 12
    
    
    await Timer(20, units="ns")
    assert dut.uo_out.value == 3






    
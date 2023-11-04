module tt_um_czlucius_alu (
    input  wire [7:0] ui_in,    // Dedicated inputs - connected to the input switches
    output wire [7:0] uo_out,   // Dedicated outputs - connected to the 7 segment display
    input  wire [7:0] uio_in,   // IOs: Bidirectional Input path
    output wire [7:0] uio_out,  // IOs: Bidirectional Output path
    output wire [7:0] uio_oe,   // IOs: Bidirectional Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // will go high when the design is enabled
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);
    wire[3:0] x, y; // declaration of variables
    wire[3:0] sel;
    reg [7:0] calculation;

    assign x = ui_in[3:0];
    assign y = ui_in[7:4];

    assign sel = uio_in[3:0];

    assign uo_out = calculation;

    assign uio_out = 8'h0;
    assign uio_oe = 8'h0;


    always @(*) begin
        case (sel)
            4'd0: calculation = x + y;
            4'd1: calculation = $signed(x) - $signed(y); // x and y are both unsigned. -15 <= calculation <= 15. (technically -16 can also be represented, but theres no way to achieve -16.)
            4'd2: calculation = x * y;
            4'd3: calculation = x / y;
            4'd4: calculation = {x[3]&y[3], x[2]&y[2], x[1]&y[1], x[0]&y[0]};
            4'd5: calculation = {x[3]|y[3], x[2]|y[2], x[1]|y[1], x[0]|y[0]};
            4'd6: calculation = {x[3]^y[3], x[2]^y[2], x[1]^y[1], x[0]^y[0]};
            4'd7: calculation = {~(x[3]&y[3]), ~(x[2]&y[2]), ~(x[1]&y[1]), ~(x[0]&y[0])};
            4'd8: calculation = {~(x[3]|y[3]), ~(x[2]|y[2]), ~(x[1]|y[1]), ~(x[0]|y[0])};
            4'd9: calculation = ~ui_in;
            4'd10: calculation = x % y;
            4'd11: calculation = x << y;
            4'd12: calculation = x >> y;
            default: calculation = ui_in; // no-op
        endcase
    end
endmodule

module test1(clk,out);
input clk;
output reg [3:0] out;
always @ (posedge clk)
    out=out+1;
endmodule
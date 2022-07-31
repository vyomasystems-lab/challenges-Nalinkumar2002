`timescale 1ns / 1ps

module rsa_main(
	 // input is what you want to encrypt or decrypt
    input [15:0] Input,
	 input [7:0]prime_p,
	 input [7:0]prime_q,
	 input clk,
    input start,
	 input start1,
	 input start2,
	 output [7:0]publicKey,
	 output [15:0]n,

	 output [15:0]Output,
	 output [15:0] privateKey,
	 output finish,
	 output fin1
    );
	
	 wire [15:0] MPower;
	 parameter InstructionSelector = 0;
	 
	 public_key_gen k1 (prime_p,prime_q,start,clk,publicKey,finish);
	 private_key_gen kd1 (prime_p,prime_q,publicKey,clk,start1,n,privateKey,fin1);
	 
	 generate
	 
	 if(InstructionSelector)
		begin
		mod_multi encryptor (Input,{8'b00000000,publicKey},n,start2,clk,finished,Mpower,Output);
		assign MPowerOutput = Mpower;
		end
	 else
		begin
	   mod_multi decryptor (Input,privateKey,n,start2,clk,finished,Mpower,Output);
		assign MPowerOutput = Mpower;
		end
	  
	  endgenerate
	  	 
endmodule


// PUBLIC KEY 


module public_key_gen(
input [7:0]p,
input [7:0]q,
input start,
input clk,
output [7:0]e1,
output reg finish
);
reg [15:0]e;
assign e1=e[7:0];
reg fin;
wire [15:0]phin;
wire outResult;

assign phin=(p-1)*(q-1);  //calculating phi(n)

reg [15:0]x,y,random,gcd;
wire [15:0]r,x1,y1;

div16 d2(x1,y1,outResult,r);
assign y1=y,x1=x;


always @(posedge clk)
begin

		if(start) 
		begin
		x<=phin;
		random<=3;  //start checking gcd from random number=3
		y<=3;
		gcd<=0;
		fin<=0;
		finish<=0;
		e<=0;
		end
		
		if((fin==1) & (gcd==1))  //output when gcd is 1
		begin
		e<=random;
		finish<=1;
		end
	
		if (r==0)       //gcd is found when remainder is 0(euclidean)
		begin
		gcd<=y;
		fin<=1;
		end
		
		
		if( fin==0)  //finding gcd
		begin
		x<=y;
		y<=r;
	
		end
	
		
		if ((fin==1) & (gcd!=1))  // check for another random number if gcd is not 1
		begin
		random<=random+2;
		y<=random+2;
		x<=phin;
		gcd<=0;
		fin<=0;
		end
end

endmodule


// PRIVATE KEY 

module private_key_gen(input [7:0] p,
    input [7:0] q,
    input [7:0] e1,
    input clk,
	 input start,
	 output reg [15:0] n,
    output [15:0] d,
	 output finished
    );
	reg [47:0] A,B,C;
	reg [15:0] G;
	reg [15:0]e;
	
	wire [15:0]outResult,Q;
	div16 d2(A[15:0],B[15:0],outResult,remainder);
	assign Q=outResult;
	always@(posedge clk)
	begin
		if(start)
			begin
			e={8'b00000000,e1};
			n=p*q;
			G=(p-1)*(q-1);
			A={16'h001,16'h000,G};
			B={16'h000,16'h001,e};
			end
		else if(B[15:0]!=1)

	 begin

	 C[47:32]=A[47:32]-Q*B[47:32];
	 C[31:16]=A[31:16]-Q*B[31:16];
	 C[15:0]=A[15:0]-Q*B[15:0];
	 A=B;
	 B=C;
	 end
	 
	 end
assign d=B[31:16];

assign finished=B[15:0]==1;
endmodule

// MODULAR MULTIPLICATION

module mod_multi(input [15:0]M,
input [15:0]e,
input [15:0]n,
input start,
input clk,
output finished,
output reg[31:0]Mpower,
output [15:0] rem_final
    );

reg [15:0] ncount;
reg [31:0]x,n1;
wire outResult;

div32 d1(x,n1,outResult,rem_final);

always @(posedge clk)
begin
		  // $display("start: %d", start);
		  if(start) begin
                ncount = e-1;
					 // $display("in start: ncount: %d; x: %d",ncount, x);
					 Mpower = M;
					 x=0;
					 n1={16'b0000000000000000,n};
        end
        else if(!finished) 
		  begin
					 Mpower = rem_final * M;
					 ncount = ncount - 1;
					 // $display("in not finished: ncount: %d; x: %d",ncount, x);

        end
		  x=Mpower;
		  // $display("out of condition: ncount: %d; x: %d",ncount, x);
		  
end

assign finished = (ncount == 0)?1:0;

endmodule

// DIV 16

module div16(A,B,Res,rem_fin);

    parameter size_width = 16;
    //input and output ports.
    input [size_width-1:0] A;
    input [size_width-1:0] B;
    output [size_width-1:0] Res;
	 output reg [size_width-1:0] rem_fin;
    //internal variables    
    reg [size_width-1:0] Res = 0;
    reg [size_width-1:0] a1,b1;
    reg [size_width:0] p1;      
	 reg [7:0]rem_finL;
    integer i;

    always@ (A or B)
    begin
        a1 = A;		
        b1 = B;		
        p1= 0;			
        for(i=0;i < size_width;i=i+1)    begin
            p1 = {p1[size_width-2:0],a1[size_width-1]};
            a1[size_width-1:1] = a1[size_width-2:0];
            p1 = p1-b1;
            if(p1[size_width-1] == 1)    begin
                a1[0] = 0;			
                p1 = p1 + b1;   end
            else
                a1[0] = 1;
        end
        Res = a1;   
		  {rem_finL,rem_fin} = p1;
	 
	 end 

endmodule

module div32(A,B,Res,rem_fin);

    parameter size_width = 32;
    //input and output ports.
    input [size_width-1:0] A;
    input [size_width-1:0] B;
    output [size_width-1:0] Res;
	 output reg [size_width-1:0] rem_fin;
    //internal variables    
    reg [size_width-1:0] Res = 0;
    reg [size_width-1:0] a1,b1;
    reg [size_width:0] p1;      
	 reg [7:0]rem_finL;
    integer i;

    always@ (A or B)
    begin
        a1 = A;		
        b1 = B;		
        p1= 0;			
        for(i=0;i < size_width;i=i+1)    begin
            p1 = {p1[size_width-2:0],a1[size_width-1]};
            a1[size_width-1:1] = a1[size_width-2:0];
            p1 = p1-b1;
            if(p1[size_width-1] == 1)    begin
                a1[0] = 0;			
                p1 = p1 + b1;   end
            else
                a1[0] = 1;
        end
        Res = a1;   
		  {rem_finL,rem_fin} = p1;
	 
	 end 

endmodule

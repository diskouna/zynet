
module ELU_ROM 
#(
    parameter int    inWidth=10,
    parameter int  dataWidth=16
) 
(
    input                 clk,
    input   [inWidth-1:0]   x,
    output  [dataWidth-1:0]  out
);
    
    reg [dataWidth-1:0] mem [2**inWidth-1:0];
    reg [inWidth-1:0] y;
	
	initial
	begin
		$readmemb("ELUContent.mif",mem);
	end

    // TODO : investigate  
    always @(posedge clk)
    begin
        if($signed(x) >= 0)
            y <= x+(2**(inWidth-1));
        else 
            y <= x-(2**(inWidth-1));      
    end
    
    assign out = mem[y];
    
endmodule

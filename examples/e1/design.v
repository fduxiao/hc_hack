module top (
    input a1,
    input a2,
    output o1,
    output o2,
    output o3,
    output o4,
    output o5
);
    assign o1 = a1 ^ a2;

    assign o2 = a1;
    assign o3 = a2;
    assign o4 = 1;
    assign o5 = 0;

endmodule

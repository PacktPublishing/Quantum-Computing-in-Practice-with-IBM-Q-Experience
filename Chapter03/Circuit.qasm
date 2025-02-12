OPENQASM 2.0;
include "qelib1.inc";
gate ryy(param0) q0,q1 { rx(pi/2) q0; rx(pi/2) q1; cx q0,q1; rz(param0) q1; cx q0,q1; rx(-pi/2) q0; rx(-pi/2) q1; }
qreg q[2];
creg c[2];
cz q[1],q[0];
ryy(3.712927889081498) q[1],q[0];
measure q[0] -> c[0];
measure q[1] -> c[1];

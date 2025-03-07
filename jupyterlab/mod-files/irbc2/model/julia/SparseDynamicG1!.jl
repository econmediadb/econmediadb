function SparseDynamicG1!(T::Vector{<: Real}, g1_v::Vector{<: Real}, y::Vector{<: Real}, x::Vector{<: Real}, params::Vector{<: Real}, steady_state::Vector{<: Real})
    @assert length(T) >= 12
    @assert length(g1_v) == 59
    @assert length(y) == 45
    @assert length(x) == 3
    @assert length(params) == 15
@inbounds begin
g1_v[1]=(-(params[14]*params[9]*exp(params[9]*y[3]+(1-params[9])*y[17])));
g1_v[2]=y[30]*params[12]*(-(y[19]*exp(y[3])))/(exp(y[3])*exp(y[3]));
g1_v[3]=(-(exp(y[3])*(1-params[11])));
g1_v[4]=(-(T[8]+T[7]*(-(y[19]*exp(y[3])))/(exp(y[3])*exp(y[3]))*2*T[1]-exp(y[3])*params[11]));
g1_v[5]=(-params[13]);
g1_v[6]=(-(params[14]*params[9]*exp(params[9]*y[10]+(1-params[9])*y[24])));
g1_v[7]=y[30]*params[12]*(-(y[26]*exp(y[10])))/(exp(y[10])*exp(y[10]));
g1_v[8]=(-((1-params[11])*exp(y[10])));
g1_v[9]=(-(T[10]+T[9]*(-(y[26]*exp(y[10])))/(exp(y[10])*exp(y[10]))*2*T[4]-params[11]*exp(y[10])));
g1_v[10]=(-params[13]);
g1_v[11]=params[4]*exp(y[16])*get_power_deriv(exp(y[16]),(-1)/params[2],1);
g1_v[12]=(-exp(y[16]));
g1_v[13]=(-(params[14]*(1-params[9])*exp(params[9]*y[3]+(1-params[9])*y[17])));
g1_v[14]=params[4]*params[1]*exp(y[17])*get_power_deriv(exp(y[17]),1/params[3],1)-(-(exp(y[17])*y[21]*(1-params[9])*y[30]*exp(y[20])))/(exp(y[17])*exp(y[17]));
g1_v[15]=(-(params[10]*y[45]*((-(params[9]*exp(y[35])*y[36]*exp(y[18])))/(exp(y[18])*exp(y[18]))+T[3]*T[11]+T[2]*params[12]*(T[11]-0.5*T[11]))));
g1_v[16]=exp(y[18]);
g1_v[17]=y[30]*params[12]*1/exp(y[3]);
g1_v[18]=(-1);
g1_v[19]=(-(1+T[7]*2*T[1]*1/exp(y[3])));
g1_v[20]=(-(y[21]*(1-params[9])*y[30]*exp(y[20])/exp(y[17])));
g1_v[21]=1;
g1_v[22]=1;
g1_v[23]=(-((1-params[9])*y[30]*exp(y[20])/exp(y[17])));
g1_v[24]=1;
g1_v[25]=1;
g1_v[26]=(-1);
g1_v[27]=params[8]*exp(y[23])*get_power_deriv(exp(y[23]),(-1)/params[6],1);
g1_v[28]=(-exp(y[23]));
g1_v[29]=(-(params[14]*(1-params[9])*exp(params[9]*y[10]+(1-params[9])*y[24])));
g1_v[30]=params[8]*params[5]*exp(y[24])*get_power_deriv(exp(y[24]),1/params[7],1)-(-(exp(y[24])*y[28]*(1-params[9])*y[30]*exp(y[27])))/(exp(y[24])*exp(y[24]));
g1_v[31]=(-(params[10]*y[45]*((-(params[9]*exp(y[42])*y[43]*exp(y[25])))/(exp(y[25])*exp(y[25]))+T[6]*T[12]+T[5]*params[12]*(T[12]-0.5*T[12]))));
g1_v[32]=exp(y[25]);
g1_v[33]=y[30]*params[12]*1/exp(y[10]);
g1_v[34]=(-1);
g1_v[35]=(-(1+T[9]*2*T[4]*1/exp(y[10])));
g1_v[36]=(-(y[28]*(1-params[9])*y[30]*exp(y[27])/exp(y[24])));
g1_v[37]=1;
g1_v[38]=1;
g1_v[39]=(-((1-params[9])*y[30]*exp(y[27])/exp(y[24])));
g1_v[40]=1;
g1_v[41]=1;
g1_v[42]=(-1);
g1_v[43]=(-(y[21]*(1-params[9])*exp(y[20])/exp(y[17])));
g1_v[44]=1+params[12]*T[1];
g1_v[45]=(-1);
g1_v[46]=(-(y[28]*(1-params[9])*exp(y[27])/exp(y[24])));
g1_v[47]=1+params[12]*T[4];
g1_v[48]=(-(params[10]*y[45]*(T[3]*1/exp(y[18])+T[2]*params[12]*(1/exp(y[18])-0.5*1/exp(y[18])))));
g1_v[49]=(-(params[10]*y[45]*params[9]*exp(y[35])*y[36]/exp(y[18])));
g1_v[50]=(-(params[10]*y[45]*params[9]*exp(y[35])/exp(y[18])));
g1_v[51]=(-(params[10]*y[45]*(T[6]*1/exp(y[25])+T[5]*params[12]*(1/exp(y[25])-0.5*1/exp(y[25])))));
g1_v[52]=(-(params[10]*y[45]*params[9]*exp(y[42])*y[43]/exp(y[25])));
g1_v[53]=(-(params[10]*y[45]*params[9]*exp(y[42])/exp(y[25])));
g1_v[54]=(-(params[10]*(1+params[9]*exp(y[35])*y[36]/exp(y[18])+T[2]*T[3])));
g1_v[55]=(-(params[10]*(1+params[9]*exp(y[42])*y[43]/exp(y[25])+T[5]*T[6])));
g1_v[56]=(-params[15]);
g1_v[57]=(-params[15]);
g1_v[58]=(-params[15]);
g1_v[59]=(-params[15]);
end
    return nothing
end


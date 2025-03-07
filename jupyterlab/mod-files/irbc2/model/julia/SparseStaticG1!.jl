function SparseStaticG1!(T::Vector{<: Real}, g1_v::Vector{<: Real}, y::Vector{<: Real}, x::Vector{<: Real}, params::Vector{<: Real})
    @assert length(T) >= 12
    @assert length(g1_v) == 45
    @assert length(y) == 15
    @assert length(x) == 3
    @assert length(params) == 15
@inbounds begin
g1_v[1]=params[4]*exp(y[1])*get_power_deriv(exp(y[1]),(-1)/params[2],1);
g1_v[2]=(-exp(y[1]));
g1_v[3]=(-(params[14]*(1-params[9])*exp(params[9]*y[3]+(1-params[9])*y[2])));
g1_v[4]=params[4]*params[1]*exp(y[2])*get_power_deriv(exp(y[2]),1/params[3],1)-(-(exp(y[2])*y[6]*(1-params[9])*y[15]*exp(y[5])))/(exp(y[2])*exp(y[2]));
g1_v[5]=(-(params[14]*params[9]*exp(params[9]*y[3]+(1-params[9])*y[2])));
g1_v[6]=y[15]*params[12]*T[9]-y[15]*params[10]*((-(exp(y[3])*y[6]*params[9]*exp(y[5])))/(exp(y[3])*exp(y[3]))+T[2]*T[9]+T[1]*params[12]*(T[9]-0.5*T[9]));
g1_v[7]=exp(y[3])-exp(y[3])*(1-params[11]);
g1_v[8]=(-(T[6]+T[5]*T[9]*2*T[1]-exp(y[3])*params[11]));
g1_v[9]=y[15]*params[12]*T[10]-y[15]*params[10]*(T[2]*T[10]+T[1]*params[12]*(T[10]-0.5*T[10]));
g1_v[10]=(-1);
g1_v[11]=(-(1+T[5]*2*T[1]*T[10]));
g1_v[12]=(-(y[6]*(1-params[9])*y[15]*exp(y[5])/exp(y[2])));
g1_v[13]=(-(y[15]*params[10]*y[6]*params[9]*exp(y[5])/exp(y[3])));
g1_v[14]=1-params[13];
g1_v[15]=1;
g1_v[16]=(-((1-params[9])*y[15]*exp(y[5])/exp(y[2])));
g1_v[17]=(-(y[15]*params[10]*params[9]*exp(y[5])/exp(y[3])));
g1_v[18]=1;
g1_v[19]=1;
g1_v[20]=(-1);
g1_v[21]=params[8]*exp(y[8])*get_power_deriv(exp(y[8]),(-1)/params[6],1);
g1_v[22]=(-exp(y[8]));
g1_v[23]=(-(params[14]*(1-params[9])*exp(params[9]*y[10]+(1-params[9])*y[9])));
g1_v[24]=params[8]*params[5]*exp(y[9])*get_power_deriv(exp(y[9]),1/params[7],1)-(-(exp(y[9])*y[13]*(1-params[9])*y[15]*exp(y[12])))/(exp(y[9])*exp(y[9]));
g1_v[25]=(-(params[14]*params[9]*exp(params[9]*y[10]+(1-params[9])*y[9])));
g1_v[26]=y[15]*params[12]*T[11]-y[15]*params[10]*((-(exp(y[10])*y[13]*params[9]*exp(y[12])))/(exp(y[10])*exp(y[10]))+T[4]*T[11]+T[3]*params[12]*(T[11]-0.5*T[11]));
g1_v[27]=exp(y[10])-(1-params[11])*exp(y[10]);
g1_v[28]=(-(T[8]+T[7]*T[11]*2*T[3]-params[11]*exp(y[10])));
g1_v[29]=y[15]*params[12]*T[12]-y[15]*params[10]*(T[4]*T[12]+T[3]*params[12]*(T[12]-0.5*T[12]));
g1_v[30]=(-1);
g1_v[31]=(-(1+T[7]*2*T[3]*T[12]));
g1_v[32]=(-(y[13]*(1-params[9])*y[15]*exp(y[12])/exp(y[9])));
g1_v[33]=(-(y[15]*params[10]*y[13]*params[9]*exp(y[12])/exp(y[10])));
g1_v[34]=1-params[13];
g1_v[35]=1;
g1_v[36]=(-((1-params[9])*y[15]*exp(y[12])/exp(y[9])));
g1_v[37]=(-(y[15]*params[10]*params[9]*exp(y[12])/exp(y[10])));
g1_v[38]=1;
g1_v[39]=1;
g1_v[40]=(-1);
g1_v[41]=(-(y[6]*(1-params[9])*exp(y[5])/exp(y[2])));
g1_v[42]=1+params[12]*T[1]-params[10]*(1+y[6]*params[9]*exp(y[5])/exp(y[3])+T[1]*T[2]);
g1_v[43]=(-1);
g1_v[44]=(-(y[13]*(1-params[9])*exp(y[12])/exp(y[9])));
g1_v[45]=1+params[12]*T[3]-params[10]*(1+y[13]*params[9]*exp(y[12])/exp(y[10])+T[3]*T[4]);
end
    if ~isreal(g1_v)
        g1_v = real(g1_v)+2*imag(g1_v);
    end
    return nothing
end


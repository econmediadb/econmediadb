function SparseDynamicResid!(T::Vector{<: Real}, residual::AbstractVector{<: Real}, y::Vector{<: Real}, x::Vector{<: Real}, params::Vector{<: Real}, steady_state::Vector{<: Real})
    @assert length(T) >= 10
    @assert length(residual) == 15
    @assert length(y) == 45
    @assert length(x) == 3
    @assert length(params) == 15
@inbounds begin
    residual[1] = (y[21]) - (params[14]*exp(params[9]*y[3]+(1-params[9])*y[17]));
    residual[2] = (params[4]*exp(y[16])^((-1)/params[2])) - (y[30]);
    residual[3] = (params[4]*params[1]*exp(y[17])^(1/params[3])) - (y[21]*(1-params[9])*y[30]*exp(y[20])/exp(y[17]));
    residual[4] = (y[30]*(1+params[12]*T[1])) - (params[10]*y[45]*(1+params[9]*exp(y[35])*y[36]/exp(y[18])+T[2]*T[3]));
    residual[5] = (exp(y[18])) - (y[19]+exp(y[3])*(1-params[11]));
    residual[6] = (y[20]) - (params[13]*y[5]+params[15]*(x[3]+x[1]));
    residual[7] = (y[28]) - (params[14]*exp(params[9]*y[10]+(1-params[9])*y[24]));
    residual[8] = (params[8]*exp(y[23])^((-1)/params[6])) - (y[30]);
    residual[9] = (params[8]*params[5]*exp(y[24])^(1/params[7])) - (y[28]*(1-params[9])*y[30]*exp(y[27])/exp(y[24]));
    residual[10] = (y[30]*(1+params[12]*T[4])) - (params[10]*y[45]*(1+params[9]*exp(y[42])*y[43]/exp(y[25])+T[5]*T[6]));
    residual[11] = (exp(y[25])) - (y[26]+(1-params[11])*exp(y[10]));
    residual[12] = (y[27]) - (params[13]*y[12]+params[15]*(x[3]+x[2]));
    residual[13] = (y[22]) - (exp(y[16])+y[19]-exp(y[3])*params[11]-y[21]+T[8]);
    residual[14] = (0) - (y[26]+exp(y[23])+y[22]-params[11]*exp(y[10])-y[28]+T[10]);
residual[15] = y[29];
end
    return nothing
end


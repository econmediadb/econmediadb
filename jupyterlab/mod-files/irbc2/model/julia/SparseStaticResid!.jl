function SparseStaticResid!(T::Vector{<: Real}, residual::AbstractVector{<: Real}, y::Vector{<: Real}, x::Vector{<: Real}, params::Vector{<: Real})
    @assert length(T) >= 8
    @assert length(residual) == 15
    @assert length(y) == 15
    @assert length(x) == 3
    @assert length(params) == 15
@inbounds begin
    residual[1] = (y[6]) - (params[14]*exp(params[9]*y[3]+(1-params[9])*y[2]));
    residual[2] = (params[4]*exp(y[1])^((-1)/params[2])) - (y[15]);
    residual[3] = (params[4]*params[1]*exp(y[2])^(1/params[3])) - (y[6]*(1-params[9])*y[15]*exp(y[5])/exp(y[2]));
    residual[4] = (y[15]*(1+params[12]*T[1])) - (y[15]*params[10]*(1+y[6]*params[9]*exp(y[5])/exp(y[3])+T[1]*T[2]));
    residual[5] = (exp(y[3])) - (y[4]+exp(y[3])*(1-params[11]));
    residual[6] = (y[5]) - (y[5]*params[13]+params[15]*(x[3]+x[1]));
    residual[7] = (y[13]) - (params[14]*exp(params[9]*y[10]+(1-params[9])*y[9]));
    residual[8] = (params[8]*exp(y[8])^((-1)/params[6])) - (y[15]);
    residual[9] = (params[8]*params[5]*exp(y[9])^(1/params[7])) - (y[13]*(1-params[9])*y[15]*exp(y[12])/exp(y[9]));
    residual[10] = (y[15]*(1+params[12]*T[3])) - (y[15]*params[10]*(1+y[13]*params[9]*exp(y[12])/exp(y[10])+T[3]*T[4]));
    residual[11] = (exp(y[10])) - (y[11]+(1-params[11])*exp(y[10]));
    residual[12] = (y[12]) - (params[13]*y[12]+params[15]*(x[3]+x[2]));
    residual[13] = (y[7]) - (exp(y[1])+y[4]-exp(y[3])*params[11]-y[6]+T[6]);
    residual[14] = (0) - (y[11]+exp(y[8])+y[7]-params[11]*exp(y[10])-y[13]+T[8]);
residual[15] = y[14];
end
    if ~isreal(residual)
        residual = real(residual)+imag(residual).^2;
    end
    return nothing
end


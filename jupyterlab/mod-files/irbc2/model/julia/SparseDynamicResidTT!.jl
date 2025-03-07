function SparseDynamicResidTT!(T::Vector{<: Real}, y::Vector{<: Real}, x::Vector{<: Real}, params::Vector{<: Real}, steady_state::Vector{<: Real})
@inbounds begin
T[1] = y[19]/exp(y[3])-params[11]
T[2] = y[34]/exp(y[18])-params[11]
T[3] = params[12]*(1-params[11]+y[34]/exp(y[18])-0.5*T[2])
T[4] = y[26]/exp(y[10])-params[11]
T[5] = y[41]/exp(y[25])-params[11]
T[6] = params[12]*(1-params[11]+y[41]/exp(y[25])-0.5*T[5])
T[7] = exp(y[3])*params[12]/2
T[8] = T[7]*T[1]^2
T[9] = exp(y[10])*params[12]/2
T[10] = T[9]*T[4]^2
end
    return nothing
end


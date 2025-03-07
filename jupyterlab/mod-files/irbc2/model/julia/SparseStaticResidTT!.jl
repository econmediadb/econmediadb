function SparseStaticResidTT!(T::Vector{<: Real}, y::Vector{<: Real}, x::Vector{<: Real}, params::Vector{<: Real})
@inbounds begin
T[1] = y[4]/exp(y[3])-params[11]
T[2] = params[12]*(y[4]/exp(y[3])+1-params[11]-T[1]*0.5)
T[3] = y[11]/exp(y[10])-params[11]
T[4] = params[12]*(1-params[11]+y[11]/exp(y[10])-0.5*T[3])
T[5] = exp(y[3])*params[12]/2
T[6] = T[5]*T[1]^2
T[7] = exp(y[10])*params[12]/2
T[8] = T[7]*T[3]^2
end
    return nothing
end


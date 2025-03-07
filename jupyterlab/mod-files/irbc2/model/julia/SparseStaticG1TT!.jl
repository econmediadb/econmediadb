function SparseStaticG1TT!(T::Vector{<: Real}, y::Vector{<: Real}, x::Vector{<: Real}, params::Vector{<: Real})
    SparseStaticResidTT!(T, y, x, params)
@inbounds begin
T[9] = (-(y[4]*exp(y[3])))/(exp(y[3])*exp(y[3]))
T[10] = 1/exp(y[3])
T[11] = (-(y[11]*exp(y[10])))/(exp(y[10])*exp(y[10]))
T[12] = 1/exp(y[10])
end
    return nothing
end


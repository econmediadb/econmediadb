function SparseDynamicG1TT!(T::Vector{<: Real}, y::Vector{<: Real}, x::Vector{<: Real}, params::Vector{<: Real}, steady_state::Vector{<: Real})
    SparseDynamicResidTT!(T, y, x, params, steady_state)
@inbounds begin
T[11] = (-(exp(y[18])*y[34]))/(exp(y[18])*exp(y[18]))
T[12] = (-(exp(y[25])*y[41]))/(exp(y[25])*exp(y[25]))
end
    return nothing
end


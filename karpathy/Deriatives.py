def forwardMultiplyGate(a, b):
    return a * b


def forwardAddGate(a, b):
    return a + b


def forwardCircuit(x, y, z):
    return forwardMultiplyGate(forwardAddGate(x, y), z)



if '__main__' == __name__:
    x, y, z = -2, 5, -4
    q = forwardAddGate(x, y)
    derivative_q_wrt_x = 1
    derivative_q_wrt_y = 1

    f = forwardAddGate(q, z)
    derivative_f_wrt_q = z
    derivative_f_wrt_z = q
    derivative_f_wrt_x = derivative_f_wrt_q * derivative_q_wrt_x
    derivative_f_wrt_y = derivative_f_wrt_q * derivative_q_wrt_y

    print("derivative_f_wrt_x = ", derivative_f_wrt_x)
    print("derivative_f_wrt_y = ", derivative_f_wrt_y)
    print("derivative_f_wrt_z = ", derivative_f_wrt_z)

    step_size = 0.01
    x = x + step_size * derivative_f_wrt_x
    y = y + step_size * derivative_f_wrt_y
    z = z + step_size * derivative_f_wrt_z

    print("updated circuit is: " , forwardCircuit(x, y, z))

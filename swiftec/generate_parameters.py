from config import *

def conic_point(a, b, q, signs=[1,1,1,1,1,1]):
    """ Returns the coordinates of a point in the conic C(u): X^2 + (3u^2+4a)Y^2 + (u^3+au+b)Z^2 as polynomials in u"""
    # Compute radicals
    try:
        sqrt_det = (-16*(4*a**3 + 27*b**2)).nth_root(2)
    except ValueError:
        raise ValueError("Determinant is not a square")
    try:
        sqrt_m3 = F(-3).nth_root(2)
    except ValueError:
        raise ValueError("q != 1 mod 3")
    try:
        cbrt_1 = F(1).nth_root(3)
    except ValueError:
        raise ValueError("Can't find 3rd root of 1")
    if not (-b/2 + sqrt_det/(24*sqrt_m3)).is_square() and not (-b/2 - sqrt_det/(24*sqrt_m3)).is_square():
        raise ValueError("Neither nu is a square")

    # f is irreducible iff a is a square, and g is irreducible iff either nu is a cube
    try:
        sqrt_a = a.nth_root(2)
    except ValueError:
        sqrt_a = None
    try:
        cbrt_nu = (-b/2 + sqrt_det/(24*sqrt_m3)).nth_root(3)
    except ValueError:
        try:
            cbrt_nu = (-b/2 - sqrt_det/(24*sqrt_m3)).nth_root(3)
        except ValueError:
            cbrt_nu = None

    # Special case a = 0
    # In this case the polynomials X0(u), Y0(u) are not needed.
    # Instead, we use this space to store some precomputed constants
    if a == 0:
        print("Special case a = 0. In this case the polynomials X0(u), Y0(u) are not needed. Instead, we use this space to store some precomputed constants.")
        X = [sqrt_m3, 1/F(2), 0]
        Y = [0, 0]
        Z = [1]
        print("X = " + str(X))
        print("Y = " + str(Y))
        print("Z = " + str(Z))
        return X,Y,Z,5

    # Case 1
    if not sqrt_a and not cbrt_nu:
        case = 1
        # Coefficients of -1/sqrt(g) mod f
        # At this point exactly one choice of sign for sqrt_det will work
        try:
            alpha = -3*((-36*b-sqrt_m3*sqrt_det) / (2*a*sqrt_det**2)).nth_root(2)
        except ValueError:
            sqrt_det = -sqrt_det
            alpha = -3*((-36*b-sqrt_m3*sqrt_det) / (2*a*sqrt_det**2)).nth_root(2)
        beta = alpha * (36*b - sqrt_m3*sqrt_det) / (12*a)
        # At this point either choice of sqrt_det will work
        alpha = alpha*signs[0]
        beta = beta*signs[0]
        sqrt_det = sqrt_det * signs[1]
        # Output polynomial coefficients
        X = [-6*a*beta*sqrt_det, -6*a*alpha*sqrt_det, -9*beta*sqrt_det]
        Y = [72*a*b*alpha - 24*a**2*beta, 48*a**2*alpha + 108*b*beta]
        Z = [2*a*(4*a*alpha**2 + 3*beta**2)*sqrt_det]

        # A = −9 * β * sqrt_det
        A = -9*beta*sqrt_det
        # B = −6 * a * α * sqrt_det
        B = -6*a*alpha*sqrt_det
        # C = −6 * a * β * sqrt_det
        C = -6*a*beta*sqrt_det
        # D = 48 * a**2 * α + 108 * b * β
        D = 48*(a*a)*alpha + 108*b*beta
        # E = 72 * a * b * α − 24 * a**2 * β
        E = 72*a*b**alpha - 24*(a*a)*beta
        # Z = 2 * a * (4 * a * α**2 + 3 * β**2) * sqrt_det
        Z = 2*a * (4*a*alpha*alpha + 3*beta*beta) * sqrt_det
        print("A = " + str(A))
        print("B = " + str(B))
        print("C = " + str(C))
        print("D = " + str(D))
        print("E = " + str(E))
        print("Z = " + str(Z))

        # Output polynomial coefficients
        X = [-6*a*beta*sqrt_det, -6*a*alpha*sqrt_det, -9*beta*sqrt_det]
        Y = [72*a*b*alpha - 24*a**2*beta, 48*a**2*alpha + 108*b*beta]
        Z = [2*a*(4*a*alpha**2 + 3*beta**2)*sqrt_det]
        print("X[0] = " + str(X[0]))
        print("X[1] = " + str(X[1]))
        print("X[2] = " + str(X[2]))
        print("Y[0] = " + str(Y[0]))
        print("Y[1] = " + str(Y[1]))
        print("Z = " + str(Z))

    # Case 2
    if sqrt_a and not cbrt_nu:
        case = 2
        s = 2*sqrt_a/sqrt_m3                     # the +/- root of f
        ub1 = (-1/(b-a*s/3)).nth_root(2)        # -1/sqrt(g) evaluated at the roots of f
        ub2 = (-1/(b+a*s/3)).nth_root(2)
        # Any choice of signs will work
        sqrt_det = sqrt_det*signs[0]
        ub1 = ub1*signs[1]
        ub2 = ub2*signs[2]
        # Output polynomial coefficients
        A = -3*s*(ub1+ub2)*sqrt_det
        B = -2*a*(ub1-ub2)*sqrt_det
        C = -2*a*s*(ub1+ub2)*sqrt_det
        print("A = " + str(A))
        print("B = " + str(B))
        print("C = " + str(C))
        D = -16*a**2*(ub2-ub1) + 36*b*s*(ub1+ub2)
        E = -24*a*b*(ub2-ub1) - 8*a**2*s*(ub1+ub2)
        Z = 4*a*s*ub1*ub2*sqrt_det
        print("D = " + str(D))
        print("E = " + str(E))
        print("Z = " + str(Z))
        print("A/Z = " + str(A/Z))
        print("B/Z = " + str(B/Z))
        print("C/Z = " + str(C/Z))
        print("D/Z = " + str(D/Z))
        print("E/Z = " + str(E/Z))

        X = [-2*a*s*(ub1+ub2)*sqrt_det, -2*a*(ub1-ub2)*sqrt_det, -3*s*(ub1+ub2)*sqrt_det]
        Y = [-24*a*b*(ub2-ub1) - 8*a**2*s*(ub1+ub2), -16*a**2*(ub2-ub1) + 36*b*s*(ub1+ub2)]
        Z = [4*a*s*ub1*ub2*sqrt_det]

    # Case 3
    if not sqrt_a and cbrt_nu:
        case = 3
        # Coefficients of -1/sqrt(g) mod f
        # At this point exactly one choice of sign for sqrt_det will work
        try:
            alpha = -3*((-36*b-sqrt_m3*sqrt_det) / (2*a*sqrt_det**2)).nth_root(2)
        except ValueError:
            sqrt_det = -sqrt_det
            alpha = -3*((-36*b-sqrt_m3*sqrt_det) / (2*a*sqrt_det**2)).nth_root(2)
        beta = alpha * (36*b - sqrt_m3*sqrt_det) / (12*a)
        # Roots of g
        r1 = cbrt_nu - a/(3*cbrt_nu)
        r2 = cbrt_1*cbrt_nu - a/(3*cbrt_1*cbrt_nu)
        r3 = cbrt_1**2*cbrt_nu - a/(3*cbrt_1**2*cbrt_nu)
        # -sqrt(f) evaluated at the roots of g
        uc1 = (r2 - r3)
        uc2 = (r3 - r1)
        uc3 = (r1 - r2)
        # Any choice of signs will work
        alpha = alpha*signs[0]
        beta = beta*signs[0]
        uc1 = uc1*signs[1]
        uc2 = uc2*signs[2]
        uc3 = uc3*signs[3]

        # A = 3 sqrt_det  (r1 + r2 + r3) * alpha - 3*beta)
        # B = −3 sqrt_det * alpha * (4 * a + r1**2 + r2**2 + r3**2)
        # C = sqrt_det * (4 * a * alpha (r1 + r2 + r3) + 3 * beta (r1**2 + r2**2 + r3**2))
        # D = −32*a * r1**2 * alpha + 32ar1r2 * alpha + 12 * r1**3 * r2 * alpha - 32 * a * r2**2 * alpha − 24 * r1**2 * r2**2 * alpha + 12 * r1 * r2**3 * alpha
        # + 32* a * r1r3α + 12r3 1r3α + 32ar2r3α + 12r3 2r3α − 32ar2 3α − 24r2 1r2 3α
        # − 24r2 2r2 3α + 12r1r3 3α + 12r2r3 3α − 24r3 1β + 12r2 1r2β + 12r1r2 2β
        # − 24r3 2β + 12r2 1r3β + 12r2 2r3β + 12r1r2 3β + 12r2r2 3β − 24r3 3β

        # E = 16ar2 1r2α + 16ar1r2 2α + 16ar2 1r3α − 96ar1r2r3α
        # − 24r3 1r2r3α + 16ar2 2r3α + 24r2 1r2 2r3α − 24r1r3 2 r3 α
        # + 16ar1r2 3α + 16ar2r2 3α + 24r2 1 r2 r2 3α + 24r1r2 2r2 3α
        # − 24r1r2r3 3α + 12r3 1r2β + 12r1r3 2β + 12r3 1r3β − 24r2 1r2r3β − 24r1r2 2 r3 β
        # + 12r3 2r3β − 24r1r2r2 3β + 12r1r3 3β + 12r2r3 3β

        # Z = sqrt_det * (4a + r1**2 + r2**2 + r3**2) * (4 * a * alpha**2 + 3* beta**2)

        # Output polynomial coefficients
        X = [9*beta*r1*r3**2*uc1*uc2 - 9*beta*r2*r3**2*uc1*uc2 + 12*a*alpha*r1*r3*uc2*(uc1 - uc3) - 9*beta*r1*r2**2*uc1*uc3 + 9*beta*r2**2*r3*uc1*uc3 + 9*beta*r1**2*(r2 - r3)*uc2*uc3 + 12*a*alpha*r1*r2*(-uc1 + uc2)*uc3 + 12*a*alpha*r2*r3*uc1*(-uc2 + uc3),-9*alpha*r1*r3**2*uc1*uc2 + 9*alpha*r2*r3**2*uc1*uc2 + 12*a*alpha*r2*uc2*(uc1 - uc3) + 9*alpha*r1*r2**2*uc1*uc3 - 9*alpha*r2**2*r3*uc1*uc3 - 9*alpha*r1**2*(r2 - r3)*uc2*uc3 + 12*a*alpha*r3*(-uc1 + uc2)*uc3 + 12*a*alpha*r1*uc1*(-uc2 + uc3),-9*beta*r1*uc1*(uc2 - uc3) - 9*alpha*r2*r3*uc1*(uc2 - uc3) - 9*alpha*r1*r2*(uc1 - uc2)*uc3 - 9*beta*r3*(uc1 - uc2)*uc3 - 9*beta*r2*uc2*(-uc1 + uc3) - 9*alpha*r1*r3*uc2*(-uc1 + uc3)]
        Y = [-9*beta*r1*r2**2*uc1 + 12*a*alpha*r1*r3*uc1 + 9*beta*r1*r3**2*uc1 - 12*a*alpha*r1*r2*(uc1 - uc2) - 9*alpha*r1*r2*r3**2*(uc1 - uc2) + 9*beta*r1**2*r2*uc2 - 12*a*alpha*r2*r3*uc2 - 9*beta*r2*r3**2*uc2 - 9*alpha*r1**2*r2*r3*(uc2 - uc3) - 12*a*alpha*r1*r3*uc3 - 9*beta*r1**2*r3*uc3 + 12*a*alpha*r2*r3*uc3 + 9*beta*r2**2*r3*uc3 - 9*alpha*r1*r2**2*r3*(-uc1 + uc3),12*a*alpha*r2*uc1 + 9*beta*r2**2*uc1 - 9*alpha*r2**2*r3*uc1 + 9*alpha*r2*r3**2*uc1 - 12*a*alpha*r3*(uc1 - uc2) - 9*beta*r3**2*(uc1 - uc2) - 12*a*alpha*r1*uc2 - 9*beta*r1**2*uc2 + 9*alpha*r1**2*r3*uc2 - 9*alpha*r1*r3**2*uc2 + 12*a*alpha*r1*uc3 + 9*beta*r1**2*uc3 - 12*a*alpha*r2*uc3 - 9*alpha*r1**2*r2*uc3 - 9*beta*r2**2*uc3 + 9*alpha*r1*r2**2*uc3]
        Z = [(4*a*alpha**2 + 3*beta**2)*(4*a*(r1*uc1*(uc2 - uc3) + r3*(uc1 - uc2)*uc3 + r2*uc2*(-uc1 + uc3)) + 3*(r1**2*(r2 - r3)*uc2*uc3 + r2*r3*uc1*(-(r3*uc2) + r2*uc3) + r1*uc1*(r3**2*uc2 - r2**2*uc3)))]

    # Case 4
    if sqrt_a and cbrt_nu:
        case = 4
        s = 2*sqrt_a/sqrt_m3                     # the +/- root of f
        ub1 = (-1/(b-a*s/3)).nth_root(2)        # -1/sqrt(g) evaluated at the roots of f
        ub2 = (-1/(b+a*s/3)).nth_root(2)
        # Roots of g
        r1 = cbrt_nu - a/(3*cbrt_nu)
        r2 = cbrt_1*cbrt_nu - a/(3*cbrt_1*cbrt_nu)
        r3 = cbrt_1**2*cbrt_nu - a/(3*cbrt_1**2*cbrt_nu)
        # -sqrt(f) evaluated at the roots of g
        uc1 = (r2 - r3)
        uc2 = (r3 - r1)
        uc3 = (r1 - r2)
        # Any choice of signs will work
        ub1 = ub1*signs[0]
        ub2 = ub2*signs[1]
        uc1 = uc1*signs[2]
        uc2 = uc2*signs[3]
        uc3 = uc3*signs[4]


        # A = 3 * sqrt_det *  (r1 + r2 + r3) * (ξ+ − ξ−) − 3 * s * (ξ+ + ξ−)
        A = 3 * sqrt_det * ((r1 + r2 + r3) * (ub1 - ub2) - 3 * s * (ub1 + ub2))
        # B = −3 * sqrt_det (r1**2 + r2**2 + r3**2 + 4a)(ξ+ − ξ−)
        B = -3 * sqrt_det * (r1**2 + r2**2 + r3**2 + 4*a) * (ub1 - ub2)
        # C = 3 * sqrt_det * ( s(r1**2 + r2**2 + r3**2)(ξ+ + ξ−) + 4a(r1 + r2 + r3)(ξ+ − ξ−)
        C = 3 * sqrt_det * (s * (r1**2 + r2**2 + r3**2) * (ub1 + ub2) + 4 * a * (r1 + r2 + r3) * (ub1 - ub2))

        # D = 12 * s * ( ξ+ + ξ− ) * (− 2 * r1**3 + r1**2 * r2 + r1 * r2**2 − 2 * r2**3 + r1**2 * r3 + r2**2 * r3 + r1 * r3**2 + r2 * r3**2 − 2 * r3**3
        # + 4 * ( ξ+ − ξ− ) * ( − 8 * a * r1**2 + 8 * a * r1 * r2 + 3 * r1**3 * r2 − 8 * a * r2**2 − 6 * r1**2 * r2**2 + 3 * r1 * r2**3 + 8 * a * r1 * r3 + 3 * r1**3 * r3
        # + 8 * a * r2 * r3 + 3 * r2**3 * r3 − 8 * a * r3**2 − 6 * r2**2 * r3**2 − 6 * r2**2 * r3**2 + 3*r1*r3**3 + 3 * r2 * r3**3
        D = 12*s*(ub1 + ub2) * (-2*r1**3 + (r1**2)*r2 + r1*(r2**2) - 2*r2**3 + (r1**2)*r3 + (r2**2)*r3 + r1*(r3**2) + r2*(r3**2) - 2*(r3**3)) + 4*(ub1 - ub2) * (-8*a*(r1**2) + 8*a*r1*r2 + 3*(r1**3)*r2 - 8*a*(r2**2) - 6*(r1**2)*(r2**2) + 3*r1*(r2**3) + 8*a*r1*r3 + 3*(r1**3)*r3
+ 8*a*r2*r3 + 3*(r2**3)*r3 - 8*a*(r3**2) - 6*(r1**2)*(r3**2) - 6*(r2**2)*(r3**2) + 3*r1*(r3**3) + 3*r2*(r3**3))

        # E = 12s * ( ξ+ + ξ− ) * ( r3 1r2 + r1r3 2 + r3 1r3 − 2r2 1r2r3 − 2r1r2 2r3 + r3 2r3 − 2r1r2r2 3 + r1r3 3 + r2r3 3 )
        # + 8 * ( ξ+ − ξ− ) * ( 2ar2 1r2 + 2ar1r2 2 + 2ar2 1r3 − 12ar1r2r3 − 3r3 1r2r3 + 2ar2 2r3 + 3r2 1r2 2 r3
        # − 3r1r3 2r3 + 2ar1r2 3 + 2ar2r2 3 + 3r2 1 r2 r2 3 + 3r1r2 2r2 3 − 3r1r2r3 3 )
        E = 12*s*(ub1 + ub2) * ((r1**3)*r2 + r1*(r2**3) + (r1**3)*r3 - 2*(r1**2)*r2*r3 - 2*r1*(r2**2)*r3 + (r2**3)*r3 - 2*r1*r2*(r3**2) + r1*(r3**3) + r2*(r3**3)) + 8*(ub1 - ub2) * ( 2*a*(r1**2)*r2 + 2*a*r1*(r2**2) + 2*a*(r1**2)*r3 - 12*a*r1*r2*r3 - 3*(r1**3)*r2*r3 + 2*a*(r2**2)*r3 + 3*(r1**2)*(r2**2)*r3 - 3*r1*(r2**3)*r3 + 2*a*r1*(r3**2) + 2*a*r2*(r3**2) + 3*(r1**2)*r2*(r3**2) + 3*r1*(r2**2)*(r3**2) - 3*r1*r2*(r3**3))

        # Z = 6 * sqrt_det * (r1**2 + r2**2 + r3**2 + 4a) * s * ξ+ * ξ−
        Z = 6 * sqrt_det * (r1**2 + r2**2 + r3**2 + 4*a) * s * ub1 * ub2

        print("A = " + str(A))
        print("B = " + str(B))
        print("C = " + str(C))
        print("D = " + str(D))
        print("E = " + str(E))
        print("Z = " + str(Z))

        # Output polynomial coefficients
        X = [3*r1*r3**2*s*(ub1 + ub2)*uc1*uc2 - 3*r2*r3**2*s*(ub1 + ub2)*uc1*uc2 + 4*a*r1*r3*(ub1 - ub2)*uc2*(uc1 - uc3) - 3*r1*r2**2*s*(ub1 + ub2)*uc1*uc3 + 3*r2**2*r3*s*(ub1 + ub2)*uc1*uc3 + 3*r1**2*(r2 - r3)*s*(ub1 + ub2)*uc2*uc3 + 4*a*r1*r2*(ub1 - ub2)*(-uc1 + uc2)*uc3 + 4*a*r2*r3*(ub1 - ub2)*uc1*(-uc2 + uc3),3*r1*r3**2*(-ub1 + ub2)*uc1*uc2 - 3*r2*r3**2*(-ub1 + ub2)*uc1*uc2 + 4*a*r2*(ub1 - ub2)*uc2*(uc1 - uc3) + 3*r1*r2**2*(ub1 - ub2)*uc1*uc3 + 3*r2**2*r3*(-ub1 + ub2)*uc1*uc3 + 3*r1**2*(r2 - r3)*(-ub1 + ub2)*uc2*uc3 + 4*a*r3*(ub1 - ub2)*(-uc1 + uc2)*uc3 + 4*a*r1*(ub1 - ub2)*uc1*(-uc2 + uc3),3*r1*r3*(ub1 - ub2)*uc2*(uc1 - uc3) + 3*r2*s*(ub1 + ub2)*uc2*(uc1 - uc3) - 3*r2*r3*(ub1 - ub2)*uc1*(uc2 - uc3) - 3*r1*s*(ub1 + ub2)*uc1*(uc2 - uc3) - 3*r3*s*(ub1 + ub2)*(uc1 - uc2)*uc3 + 3*r1*r2*(ub1 - ub2)*(-uc1 + uc2)*uc3]
        Y = [4*a*r1*r3*(ub1 - ub2)*uc1 - 3*r1*r2**2*s*(ub1 + ub2)*uc1 + 3*r1*r3**2*s*(ub1 + ub2)*uc1 - 4*a*r1*r2*(ub1 - ub2)*(uc1 - uc2) - 3*r1*r2*r3**2*(ub1 - ub2)*(uc1 - uc2) - 4*a*r2*r3*(ub1 - ub2)*uc2 + 3*r1**2*r2*s*(ub1 + ub2)*uc2 - 3*r2*r3**2*s*(ub1 + ub2)*uc2 + 3*r1*r2**2*r3*(ub1 - ub2)*(uc1 - uc3) - 3*r1**2*r2*r3*(ub1 - ub2)*(uc2 - uc3) - 4*a*r1*r3*(ub1 - ub2)*uc3 + 4*a*r2*r3*(ub1 - ub2)*uc3 - 3*r1**2*r3*s*(ub1 + ub2)*uc3 + 3*r2**2*r3*s*(ub1 + ub2)*uc3,4*a*r2*(ub1 - ub2)*uc1 - 3*r2**2*r3*(ub1 - ub2)*uc1 - 3*r2*r3**2*(-ub1 + ub2)*uc1 - 4*a*r3*(ub1 - ub2)*(uc1 - uc2) - 3*r3**2*s*(ub1 + ub2)*(uc1 - uc2) - 4*a*r1*(ub1 - ub2)*uc2 - 3*r1**2*r3*(-ub1 + ub2)*uc2 + 3*r1*r3**2*(-ub1 + ub2)*uc2 + 3*r2**2*s*(ub1 + ub2)*(uc1 - uc3) - 3*r1**2*s*(ub1 + ub2)*(uc2 - uc3) + 4*a*r1*(ub1 - ub2)*uc3 - 4*a*r2*(ub1 - ub2)*uc3 - 3*r1**2*r2*(ub1 - ub2)*uc3 - 3*r1*r2**2*(-ub1 + ub2)*uc3]
        Z = [2*s*ub1*ub2*(4*a*(r1*uc1*(uc2 - uc3) + r3*(uc1 - uc2)*uc3 + r2*uc2*(-uc1 + uc3)) + 3*(r1**2*(r2 - r3)*uc2*uc3 + r2*r3*uc1*(-(r3*uc2) + r2*uc3) + r1*uc1*(r3**2*uc2 - r2**2*uc3)))]

    return X,Y,Z,case

def conic_parametrization(X, Y, Z, a, b):
    """ Given a point X(u),Y(u),Z(u) in C(u), returns a parametrization alpha(t,u),beta(t,u),gamma(t,u) for Cu"""
    alpha = [[4*a*X[0]*Y[0]*Z[0],4*a*X[0]*Y[1] + 4*a*X[1]*Y[0]*Z[0],4*a*X[1]*Y[1] + 3*X[0]*Y[0]*Z[0] + 4*a*X[2]*Y[0]*Z[0],3*X[0]*Y[1] + 4*a*X[2]*Y[1] + 3*X[1]*Y[0]*Z[0],3*X[1]*Y[1] + 3*X[2]*Y[0]*Z[0],3*X[2]*Y[1]],[X[0]**2 + b*Z[0]**2 - 4*a*Y[0]**2*Z[0]**2,2*X[0]*X[1] - 8*a*Y[0]*Y[1]*Z[0] + a*Z[0]**2,X[1]**2 + 2*X[0]*X[2] - 4*a*Y[1]**2 - 3*Y[0]**2*Z[0]**2,2*X[1]*X[2] - 6*Y[0]*Y[1]*Z[0] + Z[0]**2,X[2]**2 - 3*Y[1]**2],[-(X[0]*Y[0]*Z[0]),-(X[0]*Y[1]) - X[1]*Y[0]*Z[0],-(X[1]*Y[1]) - X[2]*Y[0]*Z[0],-(X[2]*Y[1])]]
    beta = [[X[0]**2 + b*Z[0]**2,2*X[0]*X[1] + a*Z[0]**2,X[1]**2 + 2*X[0]*X[2],2*X[1]*X[2] + Z[0]**2,X[2]**2],[-2*X[0]*Y[0]*Z[0],-2*X[0]*Y[1] - 2*X[1]*Y[0]*Z[0],-2*X[1]*Y[1] - 2*X[2]*Y[0]*Z[0],-2*X[2]*Y[1]],[Y[0]**2*Z[0]**2,2*Y[0]*Y[1]*Z[0],Y[1]**2]]
    gamma = [[4*a*Y[0]*Z[0]**2,4*a*Y[1]*Z[0],3*Y[0]*Z[0]**2,3*Y[1]*Z[0]],[],[Y[0]*Z[0]**2,Y[1]*Z[0]]]
    return alpha, beta, gamma

# def iota(polys):
#     """ Change of variables from alpha,beta,gamma satisfying C(u)
#     to y, v, w satisfying S: y^2(w^2t^2 + wvt + v^2 + w^2a) = -w^4(t^2 + at + b)"""
#     v = [0]
#     v.extend(polys[1].copy())
#     for i in range(len(polys[0])):
#         v[i] = (polys[0][i]-v[i])*polys[2][0]
#     y = [4*polys[1][0]**2, 8*polys[1][0]*polys[1][1], 4*polys[1][1]**2]
#     w = polys[1].copy()
#     for i in range(len(w)):
#         w[i] = w[i]*2*polys[2][0]
#     return [v, y, w]


def main():

    X,Y,Z,case = conic_point(a, b, p)
    print("++Case "+str(case)+"+++")

    f = open("parameters/"+curve,'w')
    for i in range(len(X)):
        f.write(str(int(X[i]/Z[0]))+"\n")
    for i in range(len(Y)):
        f.write(str(int(Y[i]/Z[0]))+"\n")

    f.write(str(4*a)+"\n")
    f.write(str((p-1)>>1)+"\n")
    f.write(str(math.ceil(math.log2(p)))+"\n")

    f.close()
    print("Precomputation parameters written to parameters/"+curve)

if __name__ == "__main__":
    main()
